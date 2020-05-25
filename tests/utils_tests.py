import unittest
import pandas as pd

from utils.utils import calculate_ratio


class CalculateRatioTests(unittest.TestCase):
    def setUp(self) -> None:
        d = {'col1': ['a', 'b', 'c'], 'col2': [1, 2, 4]}
        self.df = pd.DataFrame(data=d)
        self.expected_result = 0.25

    def test_generate_options_with_success(self):
        actual_result = calculate_ratio(self.df, 'col1', 'col2', 'a', 'c')
        self.assertEqual(self.expected_result, actual_result)

    def test_generate_options_with_key_error(self):
        """When key passed isn't in dataframe"""
        with self.assertRaises(KeyError) as error:
            calculate_ratio(self.df, 'random', 'col2', 'a', 'c')
        self.assertEqual('random', error.exception.args[0])

    def test_generate_options_with_result_key_error(self):
        """When result_key passed isn't in dataframe"""
        with self.assertRaises(KeyError) as error:
            calculate_ratio(self.df, 'col1', 'random', 'a', 'c')
        self.assertEqual('random', error.exception.args[0])

    def test_generate_options_with_value1_error(self):
        """When value1 passed isn't in dataframe"""
        with self.assertRaises(TypeError) as error:
            calculate_ratio(self.df, 'col1', 'col2', 'random', 'c')
        self.assertTrue("cannot convert" in error.exception.args[0])

    def test_generate_options_with_value2_error(self):
        """When value2 passed isn't in dataframe"""
        with self.assertRaises(TypeError) as error:
            calculate_ratio(self.df, 'col1', 'col2', 'a', 'random')
        self.assertTrue("cannot convert" in error.exception.args[0])

    def test_generate_options_with_convertion_error(self):
        df = pd.DataFrame(data={'col1': ['a', 'b', 'c'], 'col2': ['asas', 'sdsd', 'dfdf']})
        with self.assertRaises(ValueError) as error:
            actual_result = calculate_ratio(df, 'col1', 'col2', 'a', 'c')
        self.assertTrue("could not convert string to float" in error.exception.args[0])

    def test_generate_options_with_zero_division_error(self):
        df = pd.DataFrame(data={'col1': ['a', 'b', 'c'], 'col2': [1, 2, 0]})
        with self.assertRaises(ZeroDivisionError) as error:
            actual_result = calculate_ratio(df, 'col1', 'col2', 'a', 'c')
        self.assertTrue("float division by zero" in error.exception.args[0])
