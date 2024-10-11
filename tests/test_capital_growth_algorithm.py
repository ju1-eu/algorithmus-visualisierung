# tests/test_capital_growth_algorithm.py

import unittest
from algorithms.capital_growth_algorithm import CapitalGrowthAlgorithm


class TestCapitalGrowthAlgorithm(unittest.TestCase):
    def setUp(self):
        self.algorithm = CapitalGrowthAlgorithm()

    def test_get_name(self):
        self.assertEqual(self.algorithm.get_name(), "Kapitalwachstum-Berechnung")

    def test_get_inputs(self):
        inputs = self.algorithm.get_inputs()
        self.assertEqual(len(inputs), 3)
        self.assertEqual(inputs[0]["id"], "initial_capital")
        self.assertEqual(inputs[1]["id"], "interest_rate")
        self.assertEqual(inputs[2]["id"], "target_sum")
        self.assertEqual(inputs[0]["type"], "number")
        self.assertEqual(inputs[1]["type"], "number")
        self.assertEqual(inputs[2]["type"], "number")

    def test_run_valid_input(self):
        inputs = {"initial_capital": "1000", "interest_rate": "5", "target_sum": "1500"}
        self.algorithm.run(inputs)
        self.assertEqual(self.algorithm.result, 9)

    def test_run_invalid_input_type(self):
        inputs = {
            "initial_capital": "1000",
            "interest_rate": "invalid",
            "target_sum": "1500",
        }
        with self.assertRaises(ValueError):
            self.algorithm.run(inputs)

    def test_run_negative_input(self):
        inputs = {
            "initial_capital": "-1000",
            "interest_rate": "5",
            "target_sum": "1500",
        }
        with self.assertRaises(ValueError):
            self.algorithm.run(inputs)

    def test_run_target_less_than_initial(self):
        inputs = {"initial_capital": "1000", "interest_rate": "5", "target_sum": "500"}
        with self.assertRaises(ValueError):
            self.algorithm.run(inputs)

    def test_get_visualization_data(self):
        inputs = {"initial_capital": "1000", "interest_rate": "5", "target_sum": "1500"}
        self.algorithm.run(inputs)
        data = self.algorithm.get_visualization_data(0)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["type"], "scatter")
        self.assertEqual(data[0]["mode"], "lines+markers")
        self.assertEqual(len(data[0]["x"]), 1)
        self.assertEqual(len(data[0]["y"]), 1)

    def test_get_step_details(self):
        inputs = {"initial_capital": "1000", "interest_rate": "5", "target_sum": "1500"}
        self.algorithm.run(inputs)
        details = self.algorithm.get_step_details(0)
        self.assertTrue(details.startswith("Jahr 0:"))

    def test_get_result(self):
        inputs = {"initial_capital": "1000", "interest_rate": "5", "target_sum": "1500"}
        self.algorithm.run(inputs)
        result = self.algorithm.get_result()
        self.assertEqual(
            result, "Es werden 9 Jahre benötigt, um die Zielsumme zu überschreiten."
        )

    def test_invalid_step_index(self):
        inputs = {"initial_capital": "1000", "interest_rate": "5", "target_sum": "1500"}
        self.algorithm.run(inputs)
        with self.assertRaises(ValueError):
            self.algorithm.get_visualization_data(-1)
        with self.assertRaises(ValueError):
            self.algorithm.get_visualization_data(1000)


if __name__ == "__main__":
    unittest.main()
