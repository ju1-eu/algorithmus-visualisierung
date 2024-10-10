# algorithms/base_algorithm.py

from abc import ABC, abstractmethod

class BaseAlgorithm(ABC):
    """
    Basisklasse für alle Algorithmen im Visualisierungs-Framework.

    Diese Klasse definiert die Schnittstelle, die alle Algorithmen implementieren müssen.
    Sie stellt abstrakte Methoden bereit, die in den Unterklassen implementiert werden müssen.
    """

    def __init__(self):
        """Initialisiert die gemeinsamen Attribute für alle Algorithmen."""
        self.steps = []
        self.result = None

    @abstractmethod
    def get_name(self) -> str:
        """Gibt den Namen des Algorithmus zurück."""
        pass

    @abstractmethod
    def get_inputs(self) -> list:
        """
        Definiert die benötigten Eingabefelder und deren Eigenschaften.

        Returns:
            list: Eine Liste von Dictionaries mit den Eingabefeld-Definitionen.
        """
        pass

    @abstractmethod
    def run(self, inputs: dict):
        """
        Führt den Algorithmus mit den gegebenen Eingaben aus.

        Args:
            inputs (dict): Ein Dictionary mit den Eingabewerten.

        Raises:
            ValueError: Wenn die Eingaben ungültig sind.
        """
        pass

    @abstractmethod
    def get_visualization_data(self, step: int) -> list:
        """
        Bereitet die Daten für die Visualisierung des aktuellen Schritts auf.

        Args:
            step (int): Der Index des aktuellen Schritts.

        Returns:
            list: Eine Liste von Plotly-Datenobjekten.
        """
        pass

    @abstractmethod
    def get_step_details(self, step: int) -> str:
        """
        Gibt eine Beschreibung oder Details zum aktuellen Schritt zurück.

        Args:
            step (int): Der Index des aktuellen Schritts.

        Returns:
            str: Eine textuelle Beschreibung des Schritts.
        """
        pass

    @abstractmethod
    def get_result(self) -> str:
        """
        Gibt das Endergebnis des Algorithmus als String zurück.

        Returns:
            str: Das Ergebnis des Algorithmus.
        """
        pass
