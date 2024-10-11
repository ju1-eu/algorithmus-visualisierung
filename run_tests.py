# run_tests.py
import unittest
from tests.test_ggt_algorithm import TestGGTAlgorithm
from tests.test_prime_number_algorithm import TestPrimeNumberAlgorithm
from tests.test_bubble_sort_algorithm import TestBubbleSortAlgorithm
from tests.test_capital_growth_algorithm import TestCapitalGrowthAlgorithm


def run_test_suite(test_suite, suite_name):
    print(f"\n{suite_name}")
    print("-" * len(suite_name))
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    return result


def run_all_tests():
    loader = unittest.TestLoader()

    test_suites = [
        (TestGGTAlgorithm, "GGT Algorithmus Tests"),
        (TestPrimeNumberAlgorithm, "Primzahlen Algorithmus Tests"),
        (TestBubbleSortAlgorithm, "Bubble Sort Algorithmus Tests"),
        (TestCapitalGrowthAlgorithm, "Kapitalwachstum Algorithmus Tests"),
    ]

    print("Algorithmus-Visualisierungs-Framework Testergebnisse")
    print("====================================================")

    total_tests = 0
    total_errors = 0
    total_failures = 0

    for test_class, suite_name in test_suites:
        suite = loader.loadTestsFromTestCase(test_class)
        result = run_test_suite(suite, suite_name)
        total_tests += result.testsRun
        total_errors += len(result.errors)
        total_failures += len(result.failures)

    print("\nZusammenfassung")
    print("---------------")
    print(f"Gesamtzahl der Tests: {total_tests}")
    print(f"Fehler: {total_errors}")
    print(f"Fehlschläge: {total_failures}")

    if total_errors == 0 and total_failures == 0:
        print("Status: OK (Alle Tests erfolgreich)")
    else:
        print("Status: FEHLER (Einige Tests sind fehlgeschlagen)")


if __name__ == "__main__":
    run_all_tests()
