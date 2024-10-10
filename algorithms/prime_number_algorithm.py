# algorithms/prime_number_algorithm.py

from algorithms.base_algorithm import BaseAlgorithm


class PrimeNumberAlgorithm(BaseAlgorithm):
    """
    Algorithmus zur Berechnung von Primzahlen bis zu einer gegebenen Obergrenze
    mittels des Siebs des Eratosthenes.
    """

    def get_name(self) -> str:
        """Gibt den Namen des Algorithmus zurück."""
        return "Primzahlen (Sieb des Eratosthenes)"

    def get_inputs(self) -> list:
        """
        Definiert die benötigten Eingabefelder und deren Eigenschaften.

        Returns:
            list: Eine Liste von Dictionaries mit den Eingabefeld-Definitionen.
        """
        return [
            {
                "id": "upper_limit",
                "label": "Obergrenze",
                "type": "number",
                "placeholder": "Geben Sie die Obergrenze ein",
                "min": 2,
            }
        ]

    def run(self, inputs: dict):
        """
        Führt den Primzahl-Algorithmus mit den gegebenen Eingaben aus.

        Args:
            inputs (dict): Ein Dictionary mit dem Eingabewert 'upper_limit'.

        Raises:
            ValueError: Wenn die Eingabe ungültig ist.
        """
        try:
            limit = int(inputs.get("upper_limit"))
        except (TypeError, ValueError):
            raise ValueError(
                "Bitte geben Sie eine gültige ganze Zahl für die Obergrenze ein."
            )

        if limit < 2:
            raise ValueError("Die Obergrenze muss mindestens 2 sein.")

        self.steps = []
        self.result = None

        # Sieb des Eratosthenes zur Berechnung von Primzahlen
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        step_count = 0

        for current in range(2, limit + 1):
            if is_prime[current]:
                # Aktuellen Zustand speichern
                self.steps.append(
                    {
                        "step": step_count,
                        "current": current,
                        "is_prime": is_prime.copy(),
                    }
                )
                step_count += 1
                for multiple in range(current * 2, limit + 1, current):
                    is_prime[multiple] = False

        # Letzten Schritt hinzufügen
        self.steps.append(
            {"step": step_count, "current": None, "is_prime": is_prime.copy()}
        )

        # Primzahlen extrahieren
        self.result = [num for num, prime in enumerate(is_prime) if prime]

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
        is_prime = current_step["is_prime"]

        data = [
            {
                "x": list(range(len(is_prime))),
                "y": [1 if prime else 0 for prime in is_prime],
                "type": "bar",
                "marker": {
                    "color": ["#1f77b4" if prime else "#d62728" for prime in is_prime]
                },
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
        current = current_step["current"]

        if current is not None:
            return f"Schritt {step}: Markiere Vielfache von {current} als nicht prim."
        else:
            return f"Schritt {step}: Algorithmus abgeschlossen."

    def get_result(self) -> str:
        """
        Gibt das Endergebnis des Algorithmus als String zurück.

        Returns:
            str: Das Ergebnis des Algorithmus.
        """
        primes = ", ".join(map(str, self.result))
        return f"Primzahlen bis {self.result[-1]}: {primes}"
