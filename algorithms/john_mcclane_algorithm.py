# john_mcclane_algorithm.py

"""
Dieses Modul enthält den Algorithmus zur Simulation des Wasserumfüllprozesses
aus dem Film 'Stirb Langsam 3', bei dem John McClane eine Wasserbombe entschärfen muss.
"""

from typing import List, Dict
from algorithms.base_algorithm import BaseAlgorithm

# Konstanten definieren
SMALL_JUG_CAPACITY = 3
LARGE_JUG_CAPACITY = 5
TARGET_AMOUNT = 4


class JohnMcClaneAlgorithm(BaseAlgorithm):
    """
    Algorithmus zur Simulation des Wasserumfüllprozesses aus 'Stirb Langsam 3',
    bei dem John McClane eine Wasserbombe mit zwei Kanistern unterschiedlicher Kapazität entschärfen muss.
    """

    def __init__(self):
        super().__init__()
        self.steps = []
        self.result = None

    def get_name(self) -> str:
        """Gibt den Namen des Algorithmus zurück."""
        return "John McClane Wasserbomben-Entschärfungs-Algorithmus"

    def get_inputs(self) -> list:
        """
        Definiert die benötigten Eingabefelder und deren Eigenschaften.

        Returns:
            list: Eine leere Liste, da keine Eingaben benötigt werden.
        """
        return []

    def get_description(self) -> str:
        """
        Gibt eine Beschreibung des John McClane Algorithmus zurück.
        """
        return """
        John McClane's Wasserbomben-Entschärfung

        Ziel: Exakt 4 Gallonen Wasser, 1 US-Gallone=3,78541 Liter

        Verfügbare Behälter:
        1. Ein 3-Gallonen-Kanister
        2. Ein 5-Gallonen-Kanister

        Aufgabe: Finde eine Lösung, wie mit nur diesen zwei Kanistern 
        genau 4 Gallonen Wasser abmessen kann, um die Bombe zu entschärfen.
        """

    def run(self, inputs: dict):
        """
        Führt die Simulation des Wasserumfüllprozesses für die Wasserbomben-Entschärfung durch.

        Args:
            inputs (dict): Ein leeres Dictionary, da keine Eingaben benötigt werden.

        Raises:
            ValueError: Wenn unerwartete Eingaben vorhanden sind.
        """
        if inputs:
            raise ValueError("Unerwartete Eingaben erhalten.")

        self.steps = []
        self.result = None

        small_jug = 0
        large_jug = 0

        # Schritt 1: 5-Gallonen-Kanister füllen
        large_jug = LARGE_JUG_CAPACITY
        self.steps.append(
            {
                "step": 1,
                "small_jug": small_jug,
                "large_jug": large_jug,
                "action": f"5-Gallonen-Kanister mit {large_jug} Gallonen gefüllt",
            }
        )

        # Schritt 2: Aus dem 5-Gallonen-Kanister in den 3-Gallonen-Kanister schütten
        transfer = min(large_jug, SMALL_JUG_CAPACITY)
        large_jug -= transfer
        small_jug = transfer
        self.steps.append(
            {
                "step": 2,
                "small_jug": small_jug,
                "large_jug": large_jug,
                "action": f"{transfer} Gallonen in den 3-Gallonen-Kanister geschüttet",
            }
        )

        # Schritt 3: 3-Gallonen-Kanister leeren
        small_jug = 0
        self.steps.append(
            {
                "step": 3,
                "small_jug": small_jug,
                "large_jug": large_jug,
                "action": "3-Gallonen-Kanister geleert",
            }
        )

        # Schritt 4: Restliche 2 Gallonen in den 3-Gallonen-Kanister umfüllen
        transfer = min(large_jug, SMALL_JUG_CAPACITY)
        large_jug -= transfer
        small_jug = transfer
        self.steps.append(
            {
                "step": 4,
                "small_jug": small_jug,
                "large_jug": large_jug,
                "action": f"{transfer} Gallonen in den 3-Gallonen-Kanister umgefüllt",
            }
        )

        # Schritt 5: 5-Gallonen-Kanister erneut füllen
        large_jug = LARGE_JUG_CAPACITY
        self.steps.append(
            {
                "step": 5,
                "small_jug": small_jug,
                "large_jug": large_jug,
                "action": f"5-Gallonen-Kanister erneut mit {LARGE_JUG_CAPACITY} Gallonen gefüllt",
            }
        )

        # Schritt 6: Aus dem 5-Gallonen-Kanister in den 3-Gallonen-Kanister schütten, bis er voll ist
        transfer = min(large_jug, SMALL_JUG_CAPACITY - small_jug)
        large_jug -= transfer
        small_jug += transfer
        self.steps.append(
            {
                "step": 6,
                "small_jug": small_jug,
                "large_jug": large_jug,
                "action": f"{transfer} Gallone in den 3-Gallonen-Kanister geschüttet",
            }
        )

        self.result = {
            "success": large_jug == TARGET_AMOUNT,
            "final_small_jug": small_jug,
            "final_large_jug": large_jug,
        }

    def get_visualization_data(self, step: int) -> List[Dict]:
        """
        Bereitet die Daten für die Visualisierung des aktuellen Schritts auf.

        Args:
            step (int): Der Index des aktuellen Schritts.

        Returns:
            List[Dict]: Eine Liste von Plotly-Datenobjekten.

        Raises:
            ValueError: Wenn der Schrittindex ungültig ist.
        """
        if step < 0 or step >= len(self.steps):
            raise ValueError("Ungültiger Schrittindex.")

        current_step = self.steps[step]
        data = [
            {
                "x": ["3-Gallonen-Kanister", "5-Gallonen-Kanister"],
                "y": [current_step["small_jug"], current_step["large_jug"]],
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
            f"3-Gallonen-Kanister: {current_step['small_jug']:.2f} Gallonen, "
            f"5-Gallonen-Kanister: {current_step['large_jug']:.2f} Gallonen"
        )

    def get_result(self) -> str:
        """
        Gibt das Endergebnis des Algorithmus als String zurück.

        Returns:
            str: Das Ergebnis des Algorithmus.
        """
        if self.result["success"]:
            return (
                f"John McClane hat es geschafft! Im 5-Gallonen-Kanister befinden sich genau "
                f"{self.result['final_large_jug']:.2f} Gallonen Wasser. Die Bombe ist entschärft!"
            )
        return (
            f"Oh nein! Die benötigte Menge konnte nicht exakt erreicht werden. "
            f"Im 5-Gallonen-Kanister befinden sich "
            f"{self.result['final_large_jug']:.2f} Gallonen Wasser. Die Bombe konnte nicht entschärft werden!"
        )
