# algorithms/ggt_algorithm.py

from algorithms.base_algorithm import BaseAlgorithm

class GGTAlgorithm(BaseAlgorithm):
    """
    Algorithmus zur Berechnung des größten gemeinsamen Teilers (GGT)
    zweier Zahlen mittels des euklidischen Algorithmus.
    """

    def get_name(self) -> str:
        """Gibt den Namen des Algorithmus zurück."""
        return "Größter Gemeinsamer Teiler (GGT)"

    def get_inputs(self) -> list:
        """
        Definiert die benötigten Eingabefelder und deren Eigenschaften.

        Returns:
            list: Eine Liste von Dictionaries mit den Eingabefeld-Definitionen.
        """
        return [
            {
                "id": "number_a",
                "label": "Zahl A",
                "type": "number",
                "placeholder": "Geben Sie die erste Zahl ein",
                "min": 1
            },
            {
                "id": "number_b",
                "label": "Zahl B",
                "type": "number",
                "placeholder": "Geben Sie die zweite Zahl ein",
                "min": 1
            }
        ]

    def run(self, inputs: dict):
        """
        Führt den GGT-Algorithmus mit den gegebenen Eingaben aus.

        Args:
            inputs (dict): Ein Dictionary mit den Eingabewerten 'number_a' und 'number_b'.

        Raises:
            ValueError: Wenn die Eingaben ungültig sind.
        """
        try:
            a = int(inputs.get("number_a"))
            b = int(inputs.get("number_b"))
        except (TypeError, ValueError):
            raise ValueError("Bitte geben Sie gültige ganze Zahlen für Zahl A und Zahl B ein.")

        if a <= 0 or b <= 0:
            raise ValueError("Die Zahlen müssen positiv und größer als 0 sein.")

        self.steps = []
        self.result = None

        # Euklidischer Algorithmus zur Berechnung des GGT
        step_count = 0
        while b != 0:
            self.steps.append({
                'step': step_count,
                'a': a,
                'b': b
            })
            a, b = b, a % b
            step_count += 1

        self.result = a
        # Letzten Schritt hinzufügen
        self.steps.append({
            'step': step_count,
            'a': a,
            'b': b
        })

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

        current_step = self.steps[step]
        data = [
            {
                'x': ['a', 'b'],
                'y': [current_step['a'], current_step['b']],
                'type': 'bar',
                'marker': {'color': ['#1f77b4', '#ff7f0e']}
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
        a = current_step['a']
        b = current_step['b']
        if b != 0:
            return f"Schritt {step}: a = {a}, b = {b}, a % b = {a % b}"
        else:
            return f"Schritt {step}: GGT gefunden mit a = {a}"

    def get_result(self) -> str:
        """
        Gibt das Endergebnis des Algorithmus als String zurück.

        Returns:
            str: Das Ergebnis des Algorithmus.
        """
        return f"Der größte gemeinsame Teiler ist {self.result}."
