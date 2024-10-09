"""
test_prime_number_algorithm.py

Testmodul für den Primzahlen-Algorithmus.

Dieses Modul enthält Unit-Tests für die `PrimeNumberAlgorithm`-Klasse, um sicherzustellen,
dass der Sieb des Eratosthenes korrekt ausgeführt wird und dass
die entsprechenden Fehler bei ungültigen Eingaben ausgelöst werden.
"""

import unittest
from algorithms.prime_number_algorithm import PrimeNumberAlgorithm


class TestPrimeNumberAlgorithm(unittest.TestCase):
    """
    Testklasse für den PrimeNumberAlgorithmus.

    Diese Klasse enthält verschiedene Testfälle, um die Funktionalität des
    `PrimeNumberAlgorithm` zu überprüfen, einschließlich der korrekten Berechnung
    der Primzahlen bis zu einer gegebenen Obergrenze und der richtigen Fehlerbehandlung
    bei ungültigen Eingaben.
    """

    def setUp(self):
        """
        Initialisierung für die Testfälle.

        Diese Methode wird vor jedem Testfall aufgerufen und erstellt eine neue
        Instanz des `PrimeNumberAlgorithm`.
        """
        self.prime = PrimeNumberAlgorithm()

    def test_primes_up_to_10(self):
        """
        Testet die Berechnung der Primzahlen bis zur Obergrenze 10.

        Überprüft, ob die Primzahlen bis 10 korrekt als [2, 3, 5, 7] berechnet werden.
        """
        result = self.prime.run(10)
        self.assertEqual(result, [2, 3, 5, 7])

    def test_primes_up_to_20(self):
        """
        Testet die Berechnung der Primzahlen bis zur Obergrenze 20.

        Überprüft, ob die Primzahlen bis 20 korrekt als [2, 3, 5, 7, 11, 13, 17, 19] berechnet werden.
        """
        result = self.prime.run(20)
        self.assertEqual(result, [2, 3, 5, 7, 11, 13, 17, 19])

    def test_primes_up_to_2(self):
        """
        Testet die Berechnung der Primzahlen bis zur Obergrenze 2.

        Überprüft, ob die Primzahl bis 2 korrekt als [2] berechnet wird.
        """
        result = self.prime.run(2)
        self.assertEqual(result, [2])

    def test_invalid_input(self):
        """
        Testet die Fehlerbehandlung bei ungültigen Eingaben.

        Überprüft, ob ein `ValueError` ausgelöst wird, wenn die Obergrenze kleiner als 2 ist.
        """
        with self.assertRaises(ValueError):
            self.prime.run(1)

    def test_steps_calculation(self):
        """
        Testet die korrekte Berechnung und Speicherung der einzelnen Schritte.

        Überprüft, ob die Anzahl der Schritte des Sieb des Eratosthenes für die Obergrenze 10 korrekt ist.
        Erwartete Anzahl der Schritte ist 4.
        """
        self.prime.run(10)
        self.assertEqual(len(self.prime.steps), 4)

    def test_primes_up_to_large_number(self):
        """
        Testet die Berechnung der Primzahlen bis zu einer großen Obergrenze.

        Überprüft, ob die Primzahlen bis 100 korrekt berechnet werden.
        """
        expected_primes = [
            2,
            3,
            5,
            7,
            11,
            13,
            17,
            19,
            23,
            29,
            31,
            37,
            41,
            43,
            47,
            53,
            59,
            61,
            67,
            71,
            73,
            79,
            83,
            89,
            97,
        ]
        result = self.prime.run(100)
        self.assertEqual(result, expected_primes)

    def test_steps_content(self):
        """
        Testet die Inhalte der einzelnen Schritte.

        Überprüft, ob die Schritte des Sieb des Eratosthenes für die Obergrenze 10 korrekt gespeichert sind.
        """
        self.prime.run(10)
        # Erwartete Anzahl der Schritte ist 4 (2, 3, 5, 7)
        expected_steps = 4
        self.assertEqual(len(self.prime.steps), expected_steps)
        # Überprüfen des letzten Schritts
        final_step = self.prime.steps[-1]
        expected_final_sieve = [
            False,
            False,
            True,
            True,
            False,
            True,
            False,
            True,
            False,
            False,
            False,
        ]
        self.assertTrue((final_step == expected_final_sieve).all())


if __name__ == "__main__":
    unittest.main()
