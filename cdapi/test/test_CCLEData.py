from cdapi.CCLEData import CCLEData
import pytest

@pytest.fixture
def data() -> CCLEData:
    """ Data loader fixture for the test.
    """
    return CCLEData('data/ccle_data_short.csv')

class Test_CCLEData:
    """ Test CCLEData """

    def test_init(self,data) -> None:
        """ This is a simple test to make sure loading the PD data works.

        Parameters
        ----------
        data : CCLEData
            Test data pulled from the fixture
        """
        data_frame = data.df()
        # Check both the length and the column names
        assert(len(data_frame) > 0)
        assert(data_frame['DepMap_ID'][0] == 'ACH-000001')

    def test_is_tcga_hotspot(self,data) -> None:
        """ This tests the ability of CCLEData to check whether a given
        is part of a given cell line.

        Parameters
        ----------
        data : CCLEData
            Test data pulled from the fixture
        """
        # Check a few matches
        assert(data.is_tcga_hotspot(7157, "ACH-000001") == True)
        assert(data.is_tcga_hotspot(9582,"ACH-000111") == True)
        assert(data.is_tcga_hotspot(23506,"ACH-002512") == True)

        # Check a few mismatches - non-existent line
        assert(data.is_tcga_hotspot(7157, "Larry") == False)
        # Non-existent gene
        assert(data.is_tcga_hotspot(2,"ACH-000111") == False)
        # Both non-existent gene and line
        assert(data.is_tcga_hotspot(3,"Moe") == False)

    def test_get_tcga_genes(self,data) -> None:
        """ This tests the ability of CCLEData to get all available
            genes for a given cell line.

        Parameters
        ----------
        data : CCLEData
            Test data pulled from the fixture
        """
        # Look for a cell line that only has a few genes in the data
        # and compare exactly
        cell_line = "ACH-000001"
        genes = [7157,7029,5295,107,135941,654463]
        assert(data.get_tcga_genes(cell_line) == genes)

        # Make sure that if a cell line does exist an empty list is
        # returned.
        assert(data.get_tcga_genes("Inigo Montoya") == [])


    def test_get_cell_lines(self,data) -> None:
        """ This tests the ability of CCLEData to get all available
        cell lines for a given gene.

        Parameters
        ----------
        data : CCLEData
            Test data pulled from the fixture
        """

        # Look for a gene that only has a small number of cell lines
        # and compare exactly
        entrez_gene_id = 259249
        cell_lines = ['ACH-000450', 'ACH-000555', 'ACH-000835',
                      'ACH-000915', 'ACH-002097', 'ACH-002231',
                      'ACH-002309', 'ACH-002310', 'ACH-002338',
                      'ACH-002396', 'ACH-002510']
        assert(data.get_cell_lines(entrez_gene_id) == cell_lines)

        # Make sure that if a gene doesn't exist an empty list is
        # returned.
        assert(data.get_cell_lines(-1) == [])
