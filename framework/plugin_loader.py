# framework/plugin_loader.py

"""
Lädt alle Algorithmusklassen dynamisch aus dem 'algorithms'-Verzeichnis.
"""

import pkgutil
import importlib
import algorithms
from algorithms.base_algorithm import BaseAlgorithm

def load_algorithms():
    """
    Durchsucht das 'algorithms'-Verzeichnis und lädt alle Algorithmusklassen, die von BaseAlgorithm erben.

    Returns:
        list: Eine Liste von Instanzen der geladenen Algorithmusklassen.
    """
    algorithms_list = []
    for loader, module_name, is_pkg in pkgutil.iter_modules(algorithms.__path__):
        if module_name == "base_algorithm":
            continue  # Basisklasse überspringen
        module = importlib.import_module(f"algorithms.{module_name}")
        for attr in dir(module):
            obj = getattr(module, attr)
            if isinstance(obj, type) and issubclass(obj, BaseAlgorithm) and obj is not BaseAlgorithm:
                algorithms_list.append(obj())
    return algorithms_list
