# tests/bubble_sort_algorithm.py

import unittest
from algorithms.bubble_sort_algorithm import BubbleSortAlgorithm

class TestBubbleSortAlgorithm(unittest.TestCase):
    def setUp(self):
        self.algorithm = BubbleSortAlgorithm()

    def test_get_name(self):
        self.assertEqual(self.algorithm.get_name(), "Bubble Sort")

    def test_get_inputs(self):
        inputs = self.algorithm.get_inputs()
        self.assertEqual(len(inputs), 1)
        self.assertEqual(inputs[0]['id'], "input_array")
        self.assertEqual(inputs[0]['type'], "text")

    def test_run_valid_input(self):
        inputs = {"input_array": "5, 2, 8, 12, 1, 6"}
        self.algorithm.run(inputs)
        self.assertEqual(self.algorithm.result, [1.0, 2.0, 5.0, 6.0, 8.0, 12.0])

    def test_run_invalid_input(self):
        inputs = {"input_array": "5, 2, a, 12, 1, 6"}
        with self.assertRaises(ValueError):
            self.algorithm.run(inputs)

    def test_run_empty_input(self):
        inputs = {"input_array": ""}
        with self.assertRaises(ValueError):
            self.algorithm.run(inputs)

    def test_get_visualization_data(self):
        inputs = {"input_array": "5, 2, 8, 12, 1, 6"}
        self.algorithm.run(inputs)
        data = self.algorithm.get_visualization_data(0)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['type'], 'bar')
        self.assertEqual(len(data[0]['x']), 6)
        self.assertEqual(len(data[0]['y']), 6)

    def test_get_step_details(self):
        inputs = {"input_array": "5, 2, 8, 12, 1, 6"}
        self.algorithm.run(inputs)
        details = self.algorithm.get_step_details(0)
        self.assertTrue(details.startswith("Schritt 0: Vergleiche Position"))

    def test_get_result(self):
        inputs = {"input_array": "5, 2, 8, 12, 1, 6"}
        self.algorithm.run(inputs)
        result = self.algorithm.get_result()
        self.assertEqual(result, "Sortiertes Array: 1.0, 2.0, 5.0, 6.0, 8.0, 12.0")

if __name__ == '__main__':
    unittest.main()

