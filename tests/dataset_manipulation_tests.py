import unittest
import pandas as pd

from utils.dataset_manipulation import generate_options, merge_on_headers, reduce_on_items


class GenerateOptionsTest(unittest.TestCase):

    def setUp(self) -> None:
        d = {'col1': [1, 2, 2, 3], 'col2': ['a', 'b', 'b', 'c']}
        self.df = pd.DataFrame(data=d)
        self.expected_result = {'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']}

    def test_generate_options_with_success(self):
        actual_result = generate_options(self.df, ['col1', 'col2'])
        self.assertEqual(self.expected_result, actual_result)

    def test_generate_options_with_key_error(self):
        """When headers passed aren't in dataframe"""
        with self.assertRaises(KeyError) as error:
            generate_options(self.df, ['col1', 'col2', 'col3'])
        self.assertEqual('col3', error.exception.args[0])


class MergeOnHeadersTest(unittest.TestCase):
    def setUp(self) -> None:
        self.df1 = pd.DataFrame(data={
            'col1': [1, 2, 3, 3],
            'col2': ['a', 'b', 'b', 'c'],
            'col3': [True, False, True, False]
        })
        self.d2 = {
            'col1': [1, 2, 3, 3],
            'col2': ['a', 'b', 'b', 'c'],
            'col4': ['True', 'False', 'True', 'False']
        }
        self.expected_result_dict = {
            'col1': {0: 1, 1: 2, 2: 3, 3: 3},
            'col2': {0: 'a', 1: 'b', 2: 'b', 3: 'c'},
            'col3': {0: True, 1: False, 2: True, 3: False},
            'col4': {0: 'True', 1: 'False', 2: 'True', 3: 'False'}
        }

    def test_merge_on_headers_with_success(self):
        df2 = pd.DataFrame(data=self.d2)
        actual_result = merge_on_headers(self.df1, df2, ['col1', 'col2'])
        self.assertEqual(self.expected_result_dict, actual_result.to_dict())

    def test_merge_on_headers_with_different_lengths(self):
        """When dfs to merge aren't same size, extra is ignored"""
        df2 = pd.DataFrame(data={
            'col1': [1, 2, 3, 3, 4],
            'col2': ['a', 'b', 'b', 'c', 'd'],
            'col4': ['True', 'False', 'True', 'False', 'True']
        })
        actual_result = merge_on_headers(self.df1, df2, ['col1', 'col2'])
        self.assertEqual(self.expected_result_dict, actual_result.to_dict())

    def test_merge_on_headers_with_key_error_on_d1(self):
        """When headers to merge aren't in df1"""
        df2 = pd.DataFrame(data=self.d2)
        with self.assertRaises(KeyError) as error:
            merge_on_headers(self.df1, df2, ['col1', 'col2', 'col4'])
        self.assertEqual('col4', error.exception.args[0])

    def test_merge_on_headers_with_key_error_on_d2(self):
        """When headers to merge aren't in df2"""
        df2 = pd.DataFrame(data=self.d2)
        with self.assertRaises(KeyError) as error:
            merge_on_headers(self.df1, df2, ['col1', 'col2', 'col3'])
        self.assertEqual('col3', error.exception.args[0])


class ReduceOnItemsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.df = pd.DataFrame(data={
            'col1': [1, 2, 3, 3],
            'col2': ['a', 'b', 'b', 'c'],
            'col3': [True, False, True, False]
        })

    def test_reduce_on_items_with_success(self):
        expected_result_dict = {
            'col1': {1: 2, 2: 3},
            'col3': {1: False, 2: True}
        }
        actual_result = reduce_on_items(self.df, {'col2': 'b'})
        self.assertEqual(expected_result_dict, actual_result.to_dict())

    def test_reduce_on_items_with_key_error(self):
        """When filters passed aren't in dataframe"""
        with self.assertRaises(KeyError) as error:
            reduce_on_items(self.df, {'col4': 'AinXabituka'})
        self.assertEqual('col4', error.exception.args[0])
