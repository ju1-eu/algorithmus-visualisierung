# framework/__init__.py

"""
Initialisiert das Framework-Modul und stellt wichtige Funktionen bereit.
"""

from .app import app
from .layout import create_layout
from .callbacks import register_callbacks
from .plugin_loader import load_algorithms
