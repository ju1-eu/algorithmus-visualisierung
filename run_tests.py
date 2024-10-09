"""
run_tests.py
Zentrales Skript zum Ausführen aller Tests.

Dieses Modul sammelt und führt alle Unit-Tests für die verschiedenen
Algorithmen im Projekt aus.
"""

import unittest

# Importieren der Testmodule
from tests.test_ggt_algorithm import TestGGTAlgorithm
from tests.test_prime_number_algorithm import TestPrimeNumberAlgorithm
from tests.test_interest_calculation_algorithm import TestInterestCalculationAlgorithm  # Neuer Import


def run_all_tests():
    """
    Führt alle verfügbaren Unit-Tests aus.

    Erstellt eine Test-Suite, fügt alle definierten Testklassen hinzu und
    führt die Tests mit einem Text-Test-Runner aus, der detaillierte
    Informationen über die Testergebnisse anzeigt.

    Parameters:
        Keine direkten Parameter.

    Returns:
        None

    Raises:
        Keine spezifischen Ausnahmen werden hier explizit behandelt.
    """
    # Erstellen einer Test-Suite
    test_suite = unittest.TestSuite()

    # Hinzufügen der Tests zur Suite
    test_suite.addTest(unittest.makeSuite(TestGGTAlgorithm))
    test_suite.addTest(unittest.makeSuite(TestPrimeNumberAlgorithm))
    test_suite.addTest(unittest.makeSuite(TestInterestCalculationAlgorithm))  # Neuer Test hinzugefügt

    # Ausführen der Tests
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)


if __name__ == "__main__":
    run_all_tests()
