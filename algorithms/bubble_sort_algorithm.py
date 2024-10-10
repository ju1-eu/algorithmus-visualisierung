# algorithms/bubble_sort_algorithm.py

from algorithms.base_algorithm import BaseAlgorithm

class BubbleSortAlgorithm(BaseAlgorithm):
    """
    Algorithmus zur Sortierung einer Liste von Zahlen mittels Bubble Sort.
    """

    def get_name(self) -> str:
        """Gibt den Namen des Algorithmus zurück."""
        return "Bubble Sort"

    def get_inputs(self) -> list:
        """
        Definiert die benötigten Eingabefelder und deren Eigenschaften.

        Returns:
            list: Eine Liste von Dictionaries mit den Eingabefeld-Definitionen.
        """
        return [
            {
                "id": "input_array",
                "label": "Eingabe-Array",
                "type": "text",
                "placeholder": "Liste von Zahlen, kommagetrennt",
            }
        ]

    def run(self, inputs: dict):
        """
        Führt den Bubble Sort Algorithmus mit den gegebenen Eingaben aus.

        Args:
            inputs (dict): Ein Dictionary mit dem Eingabewert 'input_array'.

        Raises:
            ValueError: Wenn die Eingabe ungültig ist.
        """
        data_input = inputs.get("input_array")
        if not data_input:
            raise ValueError("Bitte geben Sie eine Liste von Zahlen ein.")

        try:
            data = [float(x.strip()) for x in data_input.split(',')]
        except ValueError:
            raise ValueError("Die Eingabe muss eine Liste von Zahlen sein.")

        self.steps = []
        self.result = None

        # Bubble Sort Algorithmus
        arr = data.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                # Aktuellen Zustand speichern
                self.steps.append({
                    'step': len(self.steps),
                    'array': arr.copy(),
                    'current_indices': (j, j + 1)
                })
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        # Letzten Schritt hinzufügen
        self.steps.append({
            'step': len(self.steps),
            'array': arr.copy(),
            'current_indices': None
        })

        self.result = arr

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
        array = current_step['array']
        current_indices = current_step['current_indices']

        colors = ['#1f77b4'] * len(array)
        if current_indices:
            idx_a, idx_b = current_indices
            colors[idx_a] = '#ff7f0e'
            colors[idx_b] = '#ff7f0e'

        data = [{
            'x': list(range(len(array))),
            'y': array,
            'type': 'bar',
            'marker': {'color': colors}
        }]
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
        current_indices = current_step['current_indices']
        array = current_step['array']

        if current_indices:
            idx_a, idx_b = current_indices
            val_a, val_b = array[idx_a], array[idx_b]
            return (f"Schritt {step}: Vergleiche Position {idx_a} ({val_a}) "
                    f"mit Position {idx_b} ({val_b}).")
        else:
            return f"Schritt {step}: Algorithmus abgeschlossen."

    def get_result(self) -> str:
        """
        Gibt das Endergebnis des Algorithmus als String zurück.

        Returns:
            str: Das Ergebnis des Algorithmus.
        """
        sorted_array = ', '.join(map(str, self.result))
        return f"Sortiertes Array: {sorted_array}"
