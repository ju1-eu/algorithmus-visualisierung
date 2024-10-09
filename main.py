"""
main.py
Hauptanwendung mit Option zum Ausführen von Tests.

Dieses Modul startet die Algorithmus-Visualisierungs-Framework-Anwendung
oder führt alle Tests aus, abhängig von den übergebenen Befehlszeilenargumenten.
"""

import sys
import os

# Fügen Sie das Projektverzeichnis zum Python-Pfad hinzu
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from framework import AlgorithmVisualizationFramework
from algorithms.ggt_algorithm import GGTAlgorithm
from algorithms.prime_number_algorithm import PrimeNumberAlgorithm
from algorithms.interest_calculation_algorithm import InterestCalculationAlgorithm
from run_tests import run_all_tests


def main():
    """
    Startet die Hauptanwendung oder führt Tests aus.

    Überprüft die Befehlszeilenargumente und führt entweder alle Tests aus
    oder startet das Visualisierungsframework zur Ausführung des Servers.
    """
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_all_tests()
    else:
        framework = AlgorithmVisualizationFramework()

        # Algorithmen registrieren
        framework.register_algorithm(GGTAlgorithm())
        framework.register_algorithm(PrimeNumberAlgorithm())
        framework.register_algorithm(InterestCalculationAlgorithm())

        # Layout aktualisieren nach der Registrierung der Algorithmen
        framework.update_layout()

        framework.run_server(debug=True)


if __name__ == "__main__":
    main()
