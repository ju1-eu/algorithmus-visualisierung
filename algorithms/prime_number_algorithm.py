"""
algorithms/prime_number_algorithm.py

Modul für den Primzahlen-Algorithmus (Sieb des Eratosthenes).

Dieses Modul implementiert den Sieb des Eratosthenes zur Berechnung von Primzahlen
bis zu einer angegebenen Obergrenze. Es bietet Methoden zur Ausführung des
Algorithmus, zur Erstellung von Visualisierungsdaten und zur Darstellung der
Ergebnisse sowie der einzelnen Schritte des Algorithmus.
"""

from typing import List, Dict
from dash import html
import numpy as np
from algorithms.base_algorithm import BaseAlgorithm

class PrimeNumberAlgorithm(BaseAlgorithm):
    """
    Implementiert den Sieb des Eratosthenes zur Berechnung von Primzahlen.
    """

    def __init__(self):
        """Initialisiert eine neue Instanz des PrimeNumberAlgorithmus."""
        self._name = "Primzahlen (Sieb des Eratosthenes)"
        self.steps = []
        self.result = []
        self.limit = 0

    @property
    def name(self):
        """Gibt den Namen des Algorithmus zurück."""
        return self._name

    def run(self, limit: int):
        """Führt den Sieb des Eratosthenes aus."""
        self.limit = int(limit)
        if self.limit < 2:
            raise ValueError("Die Grenze muss mindestens 2 sein.")

        self.steps = []
        sieve = np.ones(self.limit + 1, dtype=bool)
        sieve[0:2] = False

        for current in range(2, self.limit + 1):
            if sieve[current]:
                self.steps.append(sieve.copy())
                sieve[current * 2::current] = False

        self.result = np.nonzero(sieve)[0].tolist()
        return self.result 

    def get_visualization_data(self, step: int = None) -> List[Dict]:
        """Erstellt Daten für die Visualisierung der Primzahlberechnung."""
        if not self.steps:
            return []
        if step is None or step >= len(self.steps):
            step = len(self.steps) - 1
        sieve_state = self.steps[step]
        x_values = list(range(2, self.limit + 1))
        colors = [
            "green" if sieve_state[i] else "red" for i in range(2, self.limit + 1)
        ]
        return [
            {
                "x": x_values,
                "y": [1] * len(x_values),
                "type": "bar",
                "marker": {"color": colors},
                "hoverinfo": "x",
                "showlegend": False,
            }
        ]

    def get_result(self) -> str:
        """Gibt das Ergebnis der Primzahlberechnung zurück."""
        return f"Primzahlen bis {self.limit}: {', '.join(map(str, self.result))}"

    def get_step_details(self, step: int = None) -> html.Div:
        """Erstellt eine detaillierte Beschreibung eines bestimmten Berechnungsschritts."""
        if not self.steps:
            return html.P("Keine Details verfügbar.")
        if step is None or step >= len(self.steps):
            step = len(self.steps) - 1

        sieve_state = self.steps[step]
        primes_so_far = np.nonzero(sieve_state)[0]
        current_prime = primes_so_far[step]
        eliminated = np.nonzero(
            ~sieve_state
            & (self.steps[step - 1] if step > 0 else np.ones_like(sieve_state))
        )[0]

        eliminated = eliminated[eliminated > current_prime]
        eliminated = eliminated.tolist()

        return html.Div(
            [
                html.P(f"Schritt {step + 1}: Prüfe Zahl {current_prime}"),
                html.P(
                    f"Eliminierte Vielfache von {current_prime}: {', '.join(map(str, eliminated))}"
                    if eliminated
                    else "Keine Zahlen eliminiert"
                ),
            ]
        )
