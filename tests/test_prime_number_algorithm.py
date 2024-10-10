# tests/test_prime_number_algorithm.py

import unittest
from algorithms.prime_number_algorithm import PrimeNumberAlgorithm


class TestPrimeNumberAlgorithm(unittest.TestCase):
    def setUp(self):
        self.algorithm = PrimeNumberAlgorithm()

    def test_get_name(self):
        self.assertEqual(
            self.algorithm.get_name(), "Primzahlen (Sieb des Eratosthenes)"
        )

    def test_get_inputs(self):
        inputs = self.algorithm.get_inputs()
        self.assertEqual(len(inputs), 1)
        self.assertEqual(inputs[0]["id"], "upper_limit")
        self.assertEqual(inputs[0]["type"], "number")
        self.assertEqual(inputs[0]["min"], 2)

    def test_run_valid_input(self):
        inputs = {"upper_limit": "30"}
        self.algorithm.run(inputs)
        self.assertEqual(self.algorithm.result, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_run_invalid_input(self):
        inputs = {"upper_limit": "a"}
        with self.assertRaises(ValueError):
            self.algorithm.run(inputs)

    def test_run_too_small_input(self):
        inputs = {"upper_limit": "1"}
        with self.assertRaises(ValueError):
            self.algorithm.run(inputs)

    def test_get_visualization_data(self):
        inputs = {"upper_limit": "10"}
        self.algorithm.run(inputs)
        data = self.algorithm.get_visualization_data(0)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["type"], "bar")
        self.assertEqual(len(data[0]["x"]), 11)  # 0 to 10
        self.assertEqual(len(data[0]["y"]), 11)  # 0 to 10

    def test_get_step_details(self):
        inputs = {"upper_limit": "10"}
        self.algorithm.run(inputs)
        details = self.algorithm.get_step_details(0)
        self.assertTrue(details.startswith("Schritt 0:"))

    def test_get_result(self):
        inputs = {"upper_limit": "30"}
        self.algorithm.run(inputs)
        result = self.algorithm.get_result()
        self.assertEqual(
            result, "Primzahlen bis 29: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29"
        )

    def test_invalid_step_index(self):
        inputs = {"upper_limit": "10"}
        self.algorithm.run(inputs)
        with self.assertRaises(ValueError):
            self.algorithm.get_visualization_data(-1)
        with self.assertRaises(ValueError):
            self.algorithm.get_visualization_data(1000)


if __name__ == "__main__":
    unittest.main()
