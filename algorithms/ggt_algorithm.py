"""
algorithms/ggt_algorithm.py

Modul für den Größten Gemeinsamen Teiler (ggT) Algorithmus.

Dieses Modul implementiert den ggT-Algorithmus zur Berechnung des größten gemeinsamen Teilers
zwei positiver ganzer Zahlen. Es bietet Methoden zur Ausführung des Algorithmus, zur
Erstellung von Visualisierungsdaten und zur Darstellung der Ergebnisse.
"""

from typing import List, Tuple, Dict
from dash import html
from algorithms.base_algorithm import BaseAlgorithm

class GGTAlgorithm(BaseAlgorithm):
    """
    Implementiert den Algorithmus zur Berechnung des Größten Gemeinsamen Teilers (ggT).
    """

    def __init__(self):
        """Initialisiert eine neue Instanz des GGTAlgorithmus."""
        self._name = "Größter Gemeinsamer Teiler (GGT)"
        self.steps = []
        self.result = None

    @property
    def name(self):
        """Gibt den Namen des Algorithmus zurück."""
        return self._name

    def run(self, a: int, b: int):
        """Führt den ggT-Algorithmus aus."""
        a, b = int(a), int(b)
        if a <= 0 or b <= 0:
            raise ValueError("Die Zahlen müssen positiv sein.")
        self.steps = []
        while b != 0:
            self.steps.append((a, b))
            a, b = b, a % b
        self.steps.append((a, 0))
        self.result = a

    def get_visualization_data(self, step: int = None) -> List[Dict]:
        """Erstellt Daten für die Visualisierung der ggT-Berechnung."""
        if not self.steps:
            return []
        if step is None or step >= len(self.steps):
            step = len(self.steps) - 1
        current_steps = self.steps[:step + 1]
        a_values = [s[0] for s in current_steps]
        b_values = [s[1] for s in current_steps]
        x_values = list(range(len(current_steps)))
        return [
            {"x": x_values, "y": a_values, "type": "scatter", "name": "a"},
            {"x": x_values, "y": b_values, "type": "scatter", "name": "b"},
        ]

    def get_result(self) -> str:
        """Gibt das Ergebnis der ggT-Berechnung zurück."""
        return f"Der GGT ist {self.result}"

    def get_step_details(self, step: int = None) -> html.P:
        """Erstellt eine detaillierte Beschreibung eines bestimmten Berechnungsschritts."""
        if not self.steps:
            return html.P("Keine Details verfügbar.")
        if step is None or step >= len(self.steps):
            step = len(self.steps) - 1

        a, b = self.steps[step]
        return html.P(
            f"Schritt {step + 1}: a = {a}, b = {b}, a % b = {a % b if b != 0 else 'undefiniert'}"
        )
