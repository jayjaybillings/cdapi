from cdapi.CCLEData import CCLEData

def test_init() -> None:
    ''' This is a simple test to make sure loading the PD data works.'''
    data = CCLEData('data/ccle_data_short.csv')
    data_frame = data.df()
    # Check both the length and the column names
    assert(len(data_frame) > 0)
    print(data_frame.index)
