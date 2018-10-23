import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal # <-- for testing dataframes


class DFTests(unittest.TestCase):

    """ class for running unittests """

    def test_up(self):
        """ Your setUp """
        TEST_DATA_DIR = '../data';
        test_file_name = 'flights.csv';

        TEST_INPUT_DIR = 'src/datamanipulation';
        test_input_name =  'testdata.csv'
        try:
            data = pd.read_csv('../data/flights.csv')
            print('cannot open filesd')
        except IOError:
            print('cannot open file')
        self.fixture = data


if __name__ == "__main__":
    unittest.main()
