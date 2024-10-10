from algorithms.base_algorithm import BaseAlgorithm
from typing import List, Dict

class WaterTransferAlgorithm(BaseAlgorithm):
    """
    Algorithmus zur Simulation eines prozentualen Wasserumfüllprozesses zwischen zwei Eimern
    über eine bestimmte Anzahl von Zyklen.
    """

    def get_name(self) -> str:
        """Gibt den Namen des Algorithmus zurück."""
        return "Prozentualer Wasserumfüll-Algorithmus"

    def get_inputs(self) -> list:
        """
        Definiert die benötigten Eingabefelder und deren Eigenschaften.

        Returns:
            list: Eine Liste von Dictionaries mit den Eingabefeld-Definitionen.
        """
        return [
            {
                "id": "x",
                "label": "Startwert Eimer 1 (x)",
                "type": "number",
                "placeholder": "Anfänglicher Wasserstand in Eimer 1",
                "min": 0,
            },
            {
                "id": "y",
                "label": "Startwert Eimer 2 (y)",
                "type": "number",
                "placeholder": "Anfänglicher Wasserstand in Eimer 2",
                "min": 0,
            },
            {
                "id": "a",
                "label": "Prozentsatz a",
                "type": "number",
                "placeholder": "Prozentsatz des Wassers von Eimer 1 zu Eimer 2",
                "min": 0,
                "max": 100,
            },
            {
                "id": "b",
                "label": "Prozentsatz b",
                "type": "number",
                "placeholder": "Prozentsatz des Wassers von Eimer 2 zu Eimer 1",
                "min": 0,
                "max": 100,
            },
            {
                "id": "n",
                "label": "Anzahl der Umfüllvorgänge (n)",
                "type": "number",
                "placeholder": "Anzahl der Umfüllzyklen",
                "min": 1,
            },
        ]

    def run(self, inputs: dict):
        """
        Führt die Wasserumfüll-Simulation mit den gegebenen Eingaben aus.

        Args:
            inputs (dict): Ein Dictionary mit den Eingabewerten x, y, a, b und n.

        Raises:
            ValueError: Wenn die Eingaben ungültig sind.
        """
        try:
            x = float(inputs.get("x"))
            y = float(inputs.get("y"))
            a = float(inputs.get("a")) / 100  # Umwandlung in Dezimalzahl
            b = float(inputs.get("b")) / 100  # Umwandlung in Dezimalzahl
            n = int(inputs.get("n"))
        except (TypeError, ValueError):
            raise ValueError("Bitte geben Sie gültige Zahlen für alle Eingaben ein.")

        if x < 0 or y < 0:
            raise ValueError("Die Wasserstände dürfen nicht negativ sein.")
        
        if a < 0 or a > 1 or b < 0 or b > 1:
            raise ValueError("Die Prozentsätze müssen zwischen 0 und 100 liegen.")

        if n <= 0:
            raise ValueError("Die Anzahl der Umfüllvorgänge muss positiv sein.")

        self.steps = []
        self.result = None

        bucket1 = x
        bucket2 = y

        for cycle in range(n):
            self.steps.append({
                "cycle": cycle,
                "bucket1": round(bucket1, 2),
                "bucket2": round(bucket2, 2)
            })

            # Umfüllen von Eimer 1 zu Eimer 2
            transfer = bucket1 * a
            bucket1 -= transfer
            bucket2 += transfer

            self.steps.append({
                "cycle": cycle,
                "bucket1": round(bucket1, 2),
                "bucket2": round(bucket2, 2),
                "action": f"Umfüllen von Eimer 1 zu Eimer 2: {round(transfer, 2)} Einheiten"
            })

            # Umfüllen von Eimer 2 zu Eimer 1
            transfer = bucket2 * b
            bucket2 -= transfer
            bucket1 += transfer

            self.steps.append({
                "cycle": cycle,
                "bucket1": round(bucket1, 2),
                "bucket2": round(bucket2, 2),
                "action": f"Umfüllen von Eimer 2 zu Eimer 1: {round(transfer, 2)} Einheiten"
            })

        self.result = {
            "final_bucket1": round(bucket1, 2),
            "final_bucket2": round(bucket2, 2)
        }

    def get_visualization_data(self, step: int) -> List[Dict]:
        """
        Bereitet die Daten für die Visualisierung des aktuellen Schritts auf.

        Args:
            step (int): Der Index des aktuellen Schritts.

        Returns:
            List[Dict]: Eine Liste von Plotly-Datenobjekten.
        """
        if step < 0 or step >= len(self.steps):
            raise ValueError("Ungültiger Schrittindex.")

        current_step = self.steps[step]
        data = [
            {
                "x": ["Eimer 1", "Eimer 2"],
                "y": [current_step["bucket1"], current_step["bucket2"]],
                "type": "bar",
                "marker": {"color": ["#1f77b4", "#ff7f0e"]},
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
        cycle = current_step["cycle"]
        bucket1 = current_step["bucket1"]
        bucket2 = current_step["bucket2"]
        
        if "action" in current_step:
            return f"Zyklus {cycle}: {current_step['action']}. Neuer Stand: Eimer 1 = {bucket1}, Eimer 2 = {bucket2}"
        else:
            return f"Zyklus {cycle}: Aktueller Stand: Eimer 1 = {bucket1}, Eimer 2 = {bucket2}"

    def get_result(self) -> str:
        """
        Gibt das Endergebnis des Algorithmus als String zurück.

        Returns:
            str: Das Ergebnis des Algorithmus.
        """
        return f"Endstand: Eimer 1 enthält {self.result['final_bucket1']} Einheiten Wasser, " \
               f"Eimer 2 enthält {self.result['final_bucket2']} Einheiten Wasser."

    def analyze_long_term_behavior(self) -> str:
        """
        Analysiert das langfristige Verhalten des Wasserumfüllprozesses.

        Returns:
            str: Eine Beschreibung des langfristigen Verhaltens.
        """
        initial_total = self.steps[0]["bucket1"] + self.steps[0]["bucket2"]
        final_total = self.result["final_bucket1"] + self.result["final_bucket2"]
        
        if abs(initial_total - final_total) < 0.01:
            ratio1 = self.result["final_bucket1"] / initial_total
            ratio2 = self.result["final_bucket2"] / initial_total
            return f"Auf lange Sicht stabilisiert sich die Wasserverteilung bei etwa " \
                   f"{ratio1:.2%} in Eimer 1 und {ratio2:.2%} in Eimer 2."
        else:
            return "Die Gesamtwassermenge hat sich verändert. Überprüfen Sie die Berechnungen."