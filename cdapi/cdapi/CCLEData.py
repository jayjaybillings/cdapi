import pandas as pd

class CCLEData:
    ''' This is a simple class for holding and searching CCLE data.'''

    def __init__(self, dataPath):
        ''' The constructor loads the dataset into a Pandas dataframe or
        fails.'''
        try:
            self.ccle_df = pd.read_csv(dataPath)
        except:
            raise Exception("Unable to load CCLE Data.")

    def df(self):
        ''' This is a convenience function for returning the entire
        dataframe. The dataframe is compressed for brevity as
        follows. Since the Entrez_id and DepMap_ID values only matter
        if the gene is a TCGA hotspot, all genes for which
        isTCGAhotspot is false can be discarded. Furthermore, all
        columns other than the Entrez_id and DepMap_ID columns can
        also be discarded. Thus the format of the entire compressed
        data frame is simply a long list of Entrez_id/DepMap_ID pairs
        for hot spots.'''
        return self.ccle_df

# Change to Entrez Gene Id to check if a gene is present m_df.loc[m_df.DepMap_ID.str.fullmatch('8')]
# Get all genes for cell line m_df.loc[m_df['DepMap_ID'] == 'ACH-002508']
# Get all cell lines for gene m_df.loc[m_df['Entrez_Gene_Id'] == 7157]

