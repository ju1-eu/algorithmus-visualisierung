# framework/app.py

"""
Initialisiert die Dash-Anwendung für das Algorithmus-Visualisierungs-Framework.
"""

import dash
import config

# Initialisierung der Dash-Anwendung
app = dash.Dash(
    __name__,
    external_stylesheets=config.EXTERNAL_STYLESHEETS,
)
app.title = "Algorithmus-Visualisierung"
