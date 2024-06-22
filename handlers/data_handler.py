import pandas as pd

from command_types.group_types import GroupTypes
from command_types.sort_types import SortTypes


class DataHandler:
    def __init__(self, file_path):
        self.data_backup = pd.read_csv(file_path)
        self.data = pd.read_csv(file_path)

    def print_data(self):
        print(self.data)

    def get_header(self):
        return self.data.columns

    def filter(self, column_name, column_value):
        condition = self.data[column_name] == column_value
        self.data = self.data[condition]

    def get_unique_column_values(self, column_name):
        return self.data[column_name].unique()

    def group(self, column_name, group_by_column_name, agg_type):
        grouped = self.data.groupby(column_name)[group_by_column_name]

        if agg_type == GroupTypes.types['min']:
            result = grouped.min()
        elif agg_type == GroupTypes.types['max']:
            result = grouped.max()
        elif agg_type == GroupTypes.types['avg']:
            result = grouped.mean()
        elif agg_type == GroupTypes.types['sum']:
            result = grouped.sum()
        else:
            raise ValueError(f"Unsupported aggregation type: {agg_type}")

        self.data = result.reset_index()

    def sort_by_column(self, column_name, sort_type):
        sorted_data = self.data.sort_values(by=column_name, ascending=(sort_type == SortTypes.types['asc']))
        self.data = sorted_data

    def get_numeric_columns(self, columns):
        valid_group_columns = []
        for column in columns:
            if self.is_valid_numeric_column(column):
                valid_group_columns.append(column)
        return valid_group_columns

    def is_valid_numeric_column(self, column_name):
        column_data = self.data[column_name]
        return pd.api.types.is_numeric_dtype(column_data) or pd.api.types.is_datetime64_any_dtype(column_data)

    def get_string_columns(self, columns):
        string_columns = []
        for column in columns:
            if pd.api.types.is_string_dtype(self.data[column]):
                string_columns.append(column)
        return string_columns
