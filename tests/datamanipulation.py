import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal # <-- for testing dataframes


class DFTests(unittest.TestCase):

    """ class for running unittests """

    def setUp(self):
        """ Your setUp """
        TEST_DATA_DIR = 'data';
        test_file_name = 'flights.csv';

        TEST_INPUT_DIR = 'src/datamanipulation';
        test_input_name =  'testdata.csv'
        try:
            data = pd.read_csv(TEST_DATA_DIR + test_file_name)
        except IOError:
            print('cannot open file')
        self.fixture = data

    def test_dataFrame_constrcutedAsExpected(self):
        """ Test that the dataframe read in equals what you expect"""
        foo = pd.DataFrame()
        assert_frame_equal(self.fixture, foo)
