import unittest
from algorithms.interest_calculation_algorithm import InterestCalculationAlgorithm

class TestInterestCalculationAlgorithm(unittest.TestCase):
    def setUp(self):
        self.algorithm = InterestCalculationAlgorithm()

    def test_calculation(self):
        """Testet die Berechnung der Anzahl der Jahre."""
        self.algorithm.run(initial_capital=1000, interest_rate=5, target_amount=2000)
        self.assertEqual(self.algorithm.result, 15)

    def test_invalid_initial_capital(self):
        """Testet die Fehlerbehandlung bei ungültigem Anfangskapital."""
        with self.assertRaises(ValueError):
            self.algorithm.run(initial_capital=-1000, interest_rate=5, target_amount=2000)

    def test_invalid_interest_rate(self):
        """Testet die Fehlerbehandlung bei ungültigem Zinssatz."""
        with self.assertRaises(ValueError):
            self.algorithm.run(initial_capital=1000, interest_rate=-5, target_amount=2000)

    def test_invalid_target_amount(self):
        """Testet die Fehlerbehandlung bei ungültiger Zielsumme."""
        with self.assertRaises(ValueError):
            self.algorithm.run(initial_capital=1000, interest_rate=5, target_amount=500)

    def test_get_visualization_data(self):
        """Testet die Erstellung der Visualisierungsdaten."""
        self.algorithm.run(initial_capital=1000, interest_rate=5, target_amount=2000)
        data = self.algorithm.get_visualization_data()
        self.assertTrue(len(data) > 0)

    def test_get_step_details(self):
        """Testet die Rückgabe der Schrittdetails."""
        self.algorithm.run(initial_capital=1000, interest_rate=5, target_amount=2000)
        details = self.algorithm.get_step_details(0)
        self.assertIsNotNone(details)

if __name__ == '__main__':
    unittest.main()
