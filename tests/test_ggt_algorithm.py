# tests/test_ggt_algorithm.py

import unittest
from algorithms.ggt_algorithm import GGTAlgorithm

class TestGGTAlgorithm(unittest.TestCase):
    def setUp(self):
        self.algorithm = GGTAlgorithm()

    def test_get_name(self):
        self.assertEqual(self.algorithm.get_name(), "Größter Gemeinsamer Teiler (GGT)")

    def test_get_inputs(self):
        inputs = self.algorithm.get_inputs()
        self.assertEqual(len(inputs), 2)
        self.assertEqual(inputs[0]['id'], "number_a")
        self.assertEqual(inputs[1]['id'], "number_b")
        self.assertEqual(inputs[0]['type'], "number")
        self.assertEqual(inputs[1]['type'], "number")

    def test_run_valid_input(self):
        inputs = {"number_a": "48", "number_b": "18"}
        self.algorithm.run(inputs)
        self.assertEqual(self.algorithm.result, 6)

    def test_run_invalid_input(self):
        inputs = {"number_a": "a", "number_b": "18"}
        with self.assertRaises(ValueError):
            self.algorithm.run(inputs)

    def test_run_zero_input(self):
        inputs = {"number_a": "0", "number_b": "18"}
        with self.assertRaises(ValueError):
            self.algorithm.run(inputs)

    def test_run_negative_input(self):
        inputs = {"number_a": "-48", "number_b": "18"}
        with self.assertRaises(ValueError):
            self.algorithm.run(inputs)

    def test_get_visualization_data(self):
        inputs = {"number_a": "48", "number_b": "18"}
        self.algorithm.run(inputs)
        data = self.algorithm.get_visualization_data(0)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['type'], 'bar')
        self.assertEqual(len(data[0]['x']), 2)
        self.assertEqual(len(data[0]['y']), 2)

    def test_get_step_details(self):
        inputs = {"number_a": "48", "number_b": "18"}
        self.algorithm.run(inputs)
        details = self.algorithm.get_step_details(0)
        self.assertTrue(details.startswith("Schritt 0:"))

    def test_get_result(self):
        inputs = {"number_a": "48", "number_b": "18"}
        self.algorithm.run(inputs)
        result = self.algorithm.get_result()
        self.assertEqual(result, "Der größte gemeinsame Teiler ist 6.")

    def test_invalid_step_index(self):
        inputs = {"number_a": "48", "number_b": "18"}
        self.algorithm.run(inputs)
        with self.assertRaises(ValueError):
            self.algorithm.get_visualization_data(-1)
        with self.assertRaises(ValueError):
            self.algorithm.get_visualization_data(1000)

if __name__ == '__main__':
    unittest.main()