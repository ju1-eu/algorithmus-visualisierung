"""
test_ggt_algorithm.py

Testmodul für den GGT-Algorithmus.

Dieses Modul enthält Unit-Tests für die `GGTAlgorithm`-Klasse, um sicherzustellen,
dass der Größte Gemeinsame Teiler (GGT) korrekt berechnet wird und dass
die entsprechenden Fehler bei ungültigen Eingaben ausgelöst werden.
"""

import unittest
from algorithms.ggt_algorithm import GGTAlgorithm


class TestGGTAlgorithm(unittest.TestCase):
    """
    Testklasse für den GGTAlgorithmus.

    Diese Klasse enthält verschiedene Testfälle, um die Funktionalität des
    `GGTAlgorithm` zu überprüfen, einschließlich der korrekten Berechnung des GGT
    und der richtigen Fehlerbehandlung bei ungültigen Eingaben.
    """

    def setUp(self):
        """
        Initialisierung für die Testfälle.

        Diese Methode wird vor jedem Testfall aufgerufen und erstellt eine neue
        Instanz des `GGTAlgorithm`.
        """
        self.ggt = GGTAlgorithm()

    def test_ggt_positive_numbers(self):
        """
        Testet die Berechnung des GGT für zwei positive Zahlen.

        Überprüft, ob der GGT von 48 und 18 korrekt als 6 berechnet wird.
        """
        self.ggt.run(48, 18)
        self.assertEqual(self.ggt.result, 6)

    def test_ggt_negative_numbers(self):
        """
        Testet die Fehlerbehandlung bei negativen Zahlen.

        Überprüft, ob ein `ValueError` ausgelöst wird, wenn eine der Eingaben
        negativ ist.
        """
        with self.assertRaises(ValueError):
            self.ggt.run(-48, 18)

    def test_ggt_zero(self):
        """
        Testet die Fehlerbehandlung bei einer Null als Eingabe.

        Überprüft, ob ein `ValueError` ausgelöst wird, wenn eine der Eingaben
        null ist.
        """
        with self.assertRaises(ValueError):
            self.ggt.run(0, 18)

    def test_ggt_same_number(self):
        """
        Testet die Berechnung des GGT, wenn beide Zahlen gleich sind.

        Überprüft, ob der GGT von 5 und 5 korrekt als 5 berechnet wird.
        """
        self.ggt.run(5, 5)
        self.assertEqual(self.ggt.result, 5)

    def test_steps_calculation(self):
        """
        Testet die korrekte Berechnung und Speicherung der einzelnen Schritte.

        Überprüft, ob die Schritte des GGT-Algorithmus für die Eingaben 48 und 18
        korrekt gespeichert werden.
        """
        self.ggt.run(48, 18)
        expected_steps = [(48, 18), (18, 12), (12, 6), (6, 0)]
        self.assertEqual(self.ggt.steps, expected_steps)


if __name__ == "__main__":
    unittest.main()
