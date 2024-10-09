from algorithms.base_algorithm import BaseAlgorithm
from dash import html

class InterestCalculationAlgorithm(BaseAlgorithm):
    """
    Berechnet die Anzahl der Jahre, die benötigt werden, damit ein Kapital bei gegebenem Zinssatz eine bestimmte Zielsumme überschreitet.
    """

    def __init__(self):
        self._name = "Zinseszinsberechnung"
        self.steps = []
        self.result = None
        self.initial_capital = 0
        self.interest_rate = 0
        self.target_amount = 0

    @property
    def name(self):
        """Gibt den Namen des Algorithmus zurück."""
        return self._name

    def run(self, initial_capital: float, interest_rate: float, target_amount: float):
        """
        Führt die Zinseszinsberechnung aus.

        Args:
            initial_capital (float): Anfangskapital.
            interest_rate (float): Zinssatz in Prozent.
            target_amount (float): Zielsumme.

        Raises:
            ValueError: Wenn Eingabewerte ungültig sind.
        """
        if initial_capital <= 0:
            raise ValueError("Das Anfangskapital muss größer als 0 sein.")
        if interest_rate <= 0:
            raise ValueError("Der Zinssatz muss größer als 0 sein.")
        if target_amount <= initial_capital:
            raise ValueError("Die Zielsumme muss größer als das Anfangskapital sein.")

        self.initial_capital = initial_capital
        self.interest_rate = interest_rate / 100  # Umrechnung in Dezimalzahl
        self.target_amount = target_amount
        self.steps = []

        year = 0
        capital = initial_capital

        while capital < target_amount:
            self.steps.append((year, capital))
            capital *= (1 + self.interest_rate)
            year += 1

        self.steps.append((year, capital))
        self.result = year

    def get_visualization_data(self, step=None):
        """
        Bereitet die Daten für die Visualisierung vor.

        Args:
            step (int, optional): Der spezifische Schritt für die Visualisierung.

        Returns:
            List[Dict]: Daten für die Visualisierung.
        """
        if not self.steps:
            return []

        if step is None or step >= len(self.steps):
            step = len(self.steps) - 1

        current_steps = self.steps[:step + 1]
        years = [s[0] for s in current_steps]
        capitals = [s[1] for s in current_steps]

        return [
            {"x": years, "y": capitals, "type": "line", "name": "Kapitalentwicklung"}
        ]

    def get_result(self):
        """Gibt das Ergebnis der Berechnung zurück."""
        return f"Es dauert {self.result} Jahr(e), bis das Kapital die Zielsumme überschreitet."

    def get_step_details(self, step=None):
        """
        Gibt Details zum aktuellen Schritt zurück.

        Args:
            step (int, optional): Der spezifische Schritt.

        Returns:
            html.P: HTML-Element mit Schrittdetails.
        """
        if not self.steps:
            return html.P("Keine Details verfügbar.")

        if step is None or step >= len(self.steps):
            step = len(self.steps) - 1

        year, capital = self.steps[step]
        return html.P(
            f"Jahr {year}: Kapital = {capital:.2f}€"
        )
