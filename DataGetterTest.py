import unittest
import DataGetter

class TestGetDataPerPage(unittest.TestCase):
    dataGetter = DataGetter.DataGetter()
    
    """Tests for the get_data_per_page function.""" 
    def test_get_data_per_page_success(self):
        # Set up initial values for test
        previous_hash_list = []
        get_data_from_beat_saver_count = 0
        page_number = 1
        result = False
        if len(self.dataGetter.set_data().index) == 0:
            get_data_from_beat_saver_count, result = self.dataGetter.get_data_per_page(previous_hash_list, get_data_from_beat_saver_count, page_number)

        # Make assertions about the results
        self.assertTrue(result)
        self.assertNotEqual(len(self.dataGetter.idList), 0)

    def test_get_data_per_page_failure(self):

        # Set up initial values for test
        previous_hash_list = []
        get_data_from_beat_saver_count = 0
        page_number = 999999
        dataGetterFailure = DataGetter.DataGetter()

        # Call the function to be tested
        get_data_from_beat_saver_count, result = dataGetterFailure.get_data_per_page(previous_hash_list, get_data_from_beat_saver_count, page_number)

        # Make assertions about the results
        self.assertFalse(result)
        self.assertEqual(get_data_from_beat_saver_count, 0)
        self.assertEqual(len(dataGetterFailure.idList), 0)
        
    def test_set_data(self):
        # Set up initial values for test
        if len(self.dataGetter.set_data().index) == 0:
            previous_hash_list = []
            get_data_from_beat_saver_count = 0
            page_number = 1
            _ = self.dataGetter.get_data_per_page(previous_hash_list, get_data_from_beat_saver_count, page_number)

        # Call the function to be tested
        outcome_df = self.dataGetter.set_data()

        # Make assertions about the results
        self.assertIsNotNone(outcome_df.iloc[1, 0])

if __name__ == '__main__':
    unittest.main()