import pandas as pd

class CCLEData:
    """ This is a simple class for holding and searching CCLE data.
    """

    def __init__(self, dataPath):
        """ The constructor loads the dataset into a Pandas dataframe or
        fails.

        Parameters
        ----------
        dataPath : str
            The file path to the data file as a string
        """
        try:
            self.ccle_df = pd.read_csv(dataPath)
        except:
            raise Exception("Unable to load CCLE Data.")

    def df(self):
        """ This is a convenience function for returning the entire
        dataframe. The dataframe is compressed for brevity as
        follows. Since the Entrez_id and DepMap_ID values only matter
        if the gene is a TCGA hotspot, all genes for which
        isTCGAhotspot is false can be discarded. Furthermore, all
        columns other than the Entrez_id and DepMap_ID columns can
        also be discarded. Thus the format of the entire compressed
        data frame is simply a long list of Entrez_id/DepMap_ID pairs
        for hot spots.
        """
        return self.ccle_df

    def __get_sub_frame(self,column_name,value):
        """ This is a private utility function to get subframe of the
        full Pandas frame where entries in a specific column have a
        known value.

        The query for hotspot genes or cell lines is the same since
        they are both just columns from the data frame.Practically
        this helps keep the code clean and avoid bugs around key-value
        placement in the query.

        Parameters
        ----------
        column_name : str
            The column that should be searched for the known value
        value : str
            The value to find in the column

        Return
        ------
        subframe : dataframe
            The subframe with all rows eliminated that have different
            values of... er... value.
        """
        return self.ccle_df.loc[self.ccle_df[column_name] == value]

    def __get_list_from_dataframe(self,query_column_name,value,
                                  list_column_name):
        """ This is a private utility function to get a list from the
        Pandas data frame. See __get_sub_frame() for more info.

        Parameters
        ----------
        query_column_name : str
            The column that should be searched for the known value
        value : str
            The value to find in the column
        list_column_name : the name of the column that you want as a
            list

        Return
        ------
        list : []
            The values of the column as a list for which all entries in
            the query column equal value.
        """
        return self.__get_sub_frame(query_column_name, value)[list_column_name].to_list()

    def is_tcga_hotspot(self, gene_id, cell_line) -> bool:
        """ This function checks whether the named gene is a TCGA
        hotspot for the name cell line.

        Parameters
        ----------
        gene_id : int
            The Entrez Gene Id of the gene to check in the cell line
        cell_line : str
            The DepMap_ID of the cell line that make have the hotspot
            gene

        Return
        ------
        True if the gene is a TCGA hotspot gene in the cell line, and
        False if not.
        """
        # Grab all the cell lines for the specified gene
        lines = self.get_cell_lines(gene_id)
        return True if cell_line in lines else False

    def get_tcga_genes(self, cell_line) -> []:
        """ This function returns the tcga hotspot genes for the given
        cell line, if they exist. If not, it returns None.

        Parameters
        ----------
        cell_line : str
            The name of the cell line

        Return
        ------
        genes : str[]
            The list of tcga hotspot genes in the cell line. Empty if
            the cell_line isn't found ([]).

        """

        # Get all genes for cell line m_df.loc[m_df['DepMap_ID'] == 'ACH-002508']
        return self.__get_list_from_dataframe("DepMap_ID", cell_line,"Entrez_Gene_Id")

    def get_cell_lines(self,gene) -> []:
        """ This function returns all available cell lines for a given
        gene, if they exist.

        Parameters
        ----------
        gene : str
            The name of the gene

        Returns
        -------
        list : str[]
            The list of the cell lines for the gene if it exists.
            Otherwise this function returns an empty list ([]).

        """

        # Get all cell lines for the gene as subframe, then convert to a list
        return self.__get_list_from_dataframe("Entrez_Gene_Id",gene,"DepMap_ID")
