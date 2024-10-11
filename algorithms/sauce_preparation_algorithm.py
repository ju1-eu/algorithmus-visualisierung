from algorithms.base_algorithm import BaseAlgorithm
from typing import List, Dict


class SaucePreparationAlgorithm(BaseAlgorithm):
    """
    Algorithmus zur Simulation des Wasserumfüllprozesses für die Soßenzubereitung
    mit zwei Gläsern unterschiedlicher Kapazität.
    """

    def get_name(self) -> str:
        """Gibt den Namen des Algorithmus zurück."""
        return "Soßen-Zubereitungs-Algorithmus"

    def get_inputs(self) -> list:
        """
        Definiert die benötigten Eingabefelder und deren Eigenschaften.
        In diesem Fall sind keine Eingaben erforderlich, da die Glasgrößen festgelegt sind.

        Returns:
            list: Eine leere Liste, da keine Eingaben benötigt werden.
        """
        return []

    def run(self, inputs: dict):
        """
        Führt die Simulation des Wasserumfüllprozesses für die Soßenzubereitung durch.

        Args:
            inputs (dict): Ein leeres Dictionary, da keine Eingaben benötigt werden.
        """
        self.steps = []
        self.result = None

        small_glass = 0  # 0.3-Liter-Glas
        large_glass = 0  # 0.5-Liter-Glas
        small_capacity = 0.3
        large_capacity = 0.5
        target_amount = 0.1

        # Schritt 1: 0.3-Liter-Glas füllen
        small_glass = small_capacity
        self.steps.append(
            {
                "step": 1,
                "small_glass": small_glass,
                "large_glass": large_glass,
                "action": f"0.3-Liter-Glas mit {small_glass} Liter gefüllt",
            }
        )

        # Schritt 2: Inhalt in das 0.5-Liter-Glas kippen
        large_glass = small_glass
        small_glass = 0
        self.steps.append(
            {
                "step": 2,
                "small_glass": small_glass,
                "large_glass": large_glass,
                "action": f"Inhalt in das 0.5-Liter-Glas gekippt",
            }
        )

        # Schritt 3: 0.3-Liter-Glas erneut füllen
        small_glass = small_capacity
        self.steps.append(
            {
                "step": 3,
                "small_glass": small_glass,
                "large_glass": large_glass,
                "action": f"0.3-Liter-Glas erneut mit {small_glass} Liter gefüllt",
            }
        )

        # Schritt 4: Aus dem 0.3-Liter-Glas in das 0.5-Liter-Glas schütten, bis es voll ist
        transfer = min(small_glass, large_capacity - large_glass)
        small_glass -= transfer
        large_glass += transfer
        self.steps.append(
            {
                "step": 4,
                "small_glass": small_glass,
                "large_glass": large_glass,
                "action": f"{transfer} Liter in das 0.5-Liter-Glas geschüttet",
            }
        )

        self.result = {
            "success": abs(small_glass - target_amount) < 0.001,
            "final_small_glass": small_glass,
            "final_large_glass": large_glass,
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
                "x": ["0.3-Liter-Glas", "0.5-Liter-Glas"],
                "y": [current_step["small_glass"], current_step["large_glass"]],
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
        return (
            f"Schritt {current_step['step']}: {current_step['action']}. "
            f"0.3-Liter-Glas: {current_step['small_glass']:.2f} Liter, "
            f"0.5-Liter-Glas: {current_step['large_glass']:.2f} Liter"
        )

    def get_result(self) -> str:
        """
        Gibt das Endergebnis des Algorithmus als String zurück.

        Returns:
            str: Das Ergebnis des Algorithmus.
        """
        if self.result["success"]:
            return (
                f"Die Soße kann gelingen! Im 0.3-Liter-Glas befinden sich genau "
                f"{self.result['final_small_glass']:.2f} Liter Wasser."
            )
        else:
            return (
                f"Die gewünschte Menge konnte nicht exakt erreicht werden. "
                f"Im 0.3-Liter-Glas befinden sich {self.result['final_small_glass']:.2f} Liter Wasser."
            )

    def john_mcclane_solution(self) -> str:
        """
        Gibt die Lösung für die Zusatzfrage zu John McClane zurück.

        Returns:
            str: Die Erklärung, wie John McClane sich gerettet hat.
        """
        return (
            "John McClane hat sich in 'Stirb Langsam 3' mit einem ähnlichen Rätsel gerettet. "
            "Er musste eine Wasserbombe entschärfen, indem er exakt 4 Gallonen Wasser auf eine Waage stellen musste. "
            "Zur Verfügung standen nur ein 3- und ein 5-Gallonen-Kanister. Die Lösung war ähnlich wie bei unserem "
            "Soßen-Problem: Er füllte den 5-Gallonen-Kanister, goss davon 3 Gallonen in den kleineren Kanister "
            "und behielt so 2 Gallonen. Dann leerte er den 3-Gallonen-Kanister und füllte die verbleibenden 2 Gallonen hinein. "
            "Anschließend füllte er den 5-Gallonen-Kanister erneut und goss davon genug in den 3-Gallonen-Kanister, "
            "um ihn zu füllen (1 Gallone). So blieben genau 4 Gallonen im großen Kanister übrig."
        )
