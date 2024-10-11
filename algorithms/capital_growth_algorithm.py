# algorithms/capital_growth_algorithm.py

from algorithms.base_algorithm import BaseAlgorithm
import math


class CapitalGrowthAlgorithm(BaseAlgorithm):
    """
    Algorithmus zur Berechnung der Jahre, die benötigt werden,
    bis ein Kapital bei gegebenem Zinssatz eine Zielsumme überschreitet.
    """

    MAX_YEARS = 1000  # Maximale Anzahl der Jahre für die Berechnung

    def get_name(self) -> str:
        """Gibt den Namen des Algorithmus zurück."""
        return "Kapitalwachstum-Berechnung"

    def get_inputs(self) -> list:
        """
        Definiert die benötigten Eingabefelder und deren Eigenschaften.

        Returns:
            list: Eine Liste von Dictionaries mit den Eingabefeld-Definitionen.
        """
        return [
            {
                "id": "initial_capital",
                "label": "Anfangskapital",
                "type": "number",
                "placeholder": "Geben Sie das Anfangskapital ein",
                "min": 0,
                "step": 0.01,
            },
            {
                "id": "interest_rate",
                "label": "Zinssatz (in %)",
                "type": "number",
                "placeholder": "Geben Sie den jährlichen Zinssatz ein",
                "min": 0,
                "max": 100,
                "step": 0.01,
            },
            {
                "id": "target_sum",
                "label": "Zielsumme",
                "type": "number",
                "placeholder": "Geben Sie die zu erreichende Zielsumme ein",
                "min": 0,
                "step": 0.01,
            },
        ]

    def run(self, inputs: dict):
        """
        Führt den Kapitalwachstum-Algorithmus mit den gegebenen Eingaben aus.

        Args:
            inputs (dict): Ein Dictionary mit den Eingabewerten 'initial_capital', 'interest_rate' und 'target_sum'.

        Raises:
            ValueError: Wenn die Eingaben ungültig sind oder die Zielsumme nicht in realistischem Zeitrahmen erreicht wird.
        """
        try:
            initial_capital = float(inputs.get("initial_capital"))
            interest_rate = (
                float(inputs.get("interest_rate")) / 100
            )  # Umwandlung in Dezimalzahl
            target_sum = float(inputs.get("target_sum"))
        except (TypeError, ValueError):
            raise ValueError(
                "Bitte geben Sie gültige Zahlen für Anfangskapital, Zinssatz und Zielsumme ein."
            )

        if initial_capital < 0 or interest_rate < 0 or target_sum <= initial_capital:
            raise ValueError("Ungültige Eingaben. Bitte überprüfen Sie Ihre Werte.")

        self.steps = []
        self.result = None

        # Berechnung der Jahre mit der direkten Formel
        years_direct = self.calculate_years_direct(
            initial_capital, interest_rate, target_sum
        )

        # Iterative Berechnung für die Schritte
        years = 0
        current_capital = initial_capital

        while current_capital < target_sum and years < self.MAX_YEARS:
            self.steps.append({"year": years, "capital": current_capital})
            current_capital = round(
                current_capital * (1 + interest_rate), 2
            )  # Rundung auf 2 Dezimalstellen
            years += 1

        if years == self.MAX_YEARS:
            raise ValueError(
                "Zielsumme wird in realistischem Zeitrahmen nicht erreicht."
            )

        self.steps.append({"year": years, "capital": current_capital})
        self.result = years

        # Vergleich der Ergebnisse
        if abs(years - years_direct) > 1:
            print(
                f"Hinweis: Abweichung zwischen iterativer ({years} Jahre) und direkter Berechnung ({years_direct:.2f} Jahre)."
            )

    def calculate_years_direct(
        self, initial_capital: float, interest_rate: float, target_sum: float
    ) -> float:
        """
        Berechnet die Anzahl der Jahre direkt mit der Zinseszinsformel.

        Args:
            initial_capital (float): Das Anfangskapital.
            interest_rate (float): Der Zinssatz als Dezimalzahl.
            target_sum (float): Die zu erreichende Zielsumme.

        Returns:
            float: Die berechnete Anzahl der Jahre.
        """
        return math.log(target_sum / initial_capital) / math.log(1 + interest_rate)

    def get_visualization_data(self, step: int) -> list:
        """
        Bereitet die Daten für die Visualisierung des aktuellen Schritts auf.

        Args:
            step (int): Der Index des aktuellen Schritts.

        Returns:
            list: Eine Liste von Plotly-Datenobjekten.
        """
        if step < 0 or step >= len(self.steps):
            raise ValueError("Ungültiger Schrittindex.")

        data = [
            {
                "x": [s["year"] for s in self.steps[: step + 1]],
                "y": [s["capital"] for s in self.steps[: step + 1]],
                "type": "scatter",
                "mode": "lines+markers",
                "name": "Kapitalentwicklung",
            }
        ]
        return data

    def get_step_details(self, step: int) -> str:
        """
        Gibt eine Beschreibung oder Details zum aktuellen Schritt zurück.

        Args:
            step (int): Der Index des aktuellen Schritts.

        Returns:
            str: Eine textuelle Beschreibung des Schritts.
        """
        if step < 0 or step >= len(self.steps):
            return "Ungültiger Schritt."

        current_step = self.steps[step]
        return f"Jahr {current_step['year']}: Kapital = {current_step['capital']:.2f}"

    def get_result(self) -> str:
        """
        Gibt das Endergebnis des Algorithmus als String zurück.

        Returns:
            str: Das Ergebnis des Algorithmus.
        """
        return f"Es werden {self.result} Jahre benötigt, um die Zielsumme zu überschreiten."
