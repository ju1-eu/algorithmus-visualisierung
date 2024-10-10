# python main.py
# 

"""
Hauptskript zum Starten des Algorithmus-Visualisierungs-Frameworks.

Dieses Skript lädt alle verfügbaren Algorithmen, erstellt das Layout der Dash-Anwendung,
registriert die Callback-Funktionen und startet den Dash-Server.
"""

from framework import app, create_layout, register_callbacks, load_algorithms
import config

def main():
    """
    Hauptfunktion zum Starten der Anwendung.
    """
    # Algorithmen laden über das Plugin-System
    algorithms = load_algorithms()
    
    # Layout der Dash-Anwendung erstellen
    app.layout = create_layout(algorithms)
    
    # Callback-Funktionen registrieren
    register_callbacks(app, algorithms)
    
    # Dash-Server starten
    app.run_server(debug=True)  # Setzen Sie debug=False für die Produktion

if __name__ == "__main__":
    main()
