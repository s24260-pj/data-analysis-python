import unittest
import pandas as pd

from command_types.group_types import GroupTypes
from command_types.sort_types import SortTypes
from handlers.data_handler import DataHandler


class TestDataHandler(unittest.TestCase):
    def setUp(self):
        self.handler = DataHandler('test.csv')

    def test_filter_method(self):
        self.handler.filter('Name', 'Waldemar Anton')

        filtered_data = self.handler.data.reset_index(drop=True)
        expected_data = pd.DataFrame([
            ["Waldemar Anton", "Centre-Back", 27, "VfB Stuttgart", 189, "right", 2, 0, 20000000, "Germany"],
        ], columns=["Name", "Position", "Age", "Club", "Height", "Foot", "Caps", "Goals", "MarketValue", "Country"])

        pd.testing.assert_frame_equal(filtered_data, expected_data)

    def test_group_method_max(self):
        self.handler.group('Position', 'Age', GroupTypes.types['max'])

        grouped_data = self.handler.data.reset_index(drop=True)
        expected_data = pd.DataFrame([
            ["Attacking Midfield", 36],
            ["Central Midfield", 38],
            ["Centre-Back", 41],
            ["Centre-Forward", 39],
            ["Defensive Midfield", 34],
            ["Goalkeeper", 38],
            ["Left Midfield", 31],
            ["Left Winger", 36],
            ["Left-Back", 32],
            ["Right Midfield", 29],
            ["Right Winger", 34],
            ["Right-Back", 38],
            ["Second Striker", 34]
        ], columns=["Position", "Age"])

        pd.testing.assert_frame_equal(grouped_data, expected_data)

    def test_group_and_sort_method_asc(self):
        self.handler.group('Position', 'Age', GroupTypes.types['avg'])
        self.handler.sort_by_column('Age', SortTypes.types['asc'])

        sorted_data = self.handler.data.reset_index(drop=True)

        expected_data = pd.DataFrame([
            ["Second Striker", 24.400000],
            ["Right Winger", 25.285714],
            ["Attacking Midfield", 25.687500],
            ["Left Midfield", 25.750000],
            ["Left-Back", 26.151515],
            ["Central Midfield", 26.358025],
            ["Left Winger", 26.386364],
            ["Right Midfield", 26.500000],
            ["Centre-Forward", 27.116883],
            ["Centre-Back", 27.256000],
            ["Defensive Midfield", 27.260000],
            ["Right-Back", 28.860465],
            ["Goalkeeper", 28.972222]
        ], columns=["Position", "Age"])

        pd.testing.assert_frame_equal(sorted_data, expected_data)

    def test_refresh_data_method(self):
        original_data = self.handler.data
        self.handler.group('Position', 'Age', GroupTypes.types['avg'])
        self.handler.refresh_data()
        refreshed_data = self.handler.data

        pd.testing.assert_frame_equal(original_data, refreshed_data)


if __name__ == '__main__':
    unittest.main()
