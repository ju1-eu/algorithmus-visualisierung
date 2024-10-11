# python main.py
#

"""
Hauptskript zum Starten des Algorithmus-Visualisierungs-Frameworks.

Dieses Skript lädt alle verfügbaren Algorithmen, erstellt das Layout der Dash-Anwendung,
registriert die Callback-Funktionen und startet den Dash-Server.

Neue Algorithmen wie der Kapitalwachstum-Algorithmus werden automatisch durch das
Plugin-System erkannt und geladen, ohne dass Änderungen an dieser Datei erforderlich sind.
"""

from framework import app, create_layout, register_callbacks, load_algorithms
import config


def main():
    """
    Hauptfunktion zum Starten der Anwendung.
    """
    # Algorithmen laden über das Plugin-System
    # Dies wird automatisch alle Algorithmen einschließlich des neuen Kapitalwachstum-Algorithmus laden
    algorithms = load_algorithms()

    # Layout der Dash-Anwendung erstellen
    # Der neue Algorithmus wird automatisch in das Layout integriert
    app.layout = create_layout(algorithms)

    # Callback-Funktionen registrieren
    # Die Callbacks werden für alle geladenen Algorithmen, einschließlich des neuen, registriert
    register_callbacks(app, algorithms)

    # Dash-Server starten
    app.run_server(debug=True)  # Setzen Sie debug=False für die Produktion


if __name__ == "__main__":
    main()
