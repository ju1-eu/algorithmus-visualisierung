# algorithms/base_algorithm.py

from abc import ABC, abstractmethod

class BaseAlgorithm(ABC):
    @property
    @abstractmethod
    def name(self):
        """Gibt den Namen des Algorithmus zurück."""
        pass

    @abstractmethod
    def run(self, *args, **kwargs):
        """Führt den Algorithmus aus."""
        pass

    @abstractmethod
    def get_visualization_data(self, step=None):
        """Bereitet die Daten für die Visualisierung vor."""
        pass

    @abstractmethod
    def get_result(self):
        """Gibt das Ergebnis des Algorithmus zurück."""
        pass

    @abstractmethod
    def get_step_details(self, step=None):
        """Gibt Details zum aktuellen Schritt zurück."""
        pass
