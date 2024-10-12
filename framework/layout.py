# framework/layout.py

from dash import html, dcc
import dash_bootstrap_components as dbc


def generate_input_fields(algorithm):
    """Generiert dynamisch die Eingabefelder basierend auf den Algorithmus-Anforderungen."""
    inputs = algorithm.get_inputs()
    fields = []
    for input_def in inputs:
        field = dcc.Input(
            id={"type": "algorithm-input", "index": input_def["id"]},
            type=input_def.get("type", "text"),
            placeholder=input_def.get("placeholder", ""),
            min=input_def.get("min"),
        )
        fields.append(
            dbc.Row(
                [
                    dbc.Col(dbc.Label(input_def["label"]), width="auto"),
                    dbc.Col(field),
                ],
                className="mb-3",
            )
        )
    return html.Div(fields, id="algorithm-input-fields")


def create_layout(algorithms):
    """Erstellt das Hauptlayout der Anwendung."""
    algorithm_options = [
        {"label": algo.get_name(), "value": algo.get_name()} for algo in algorithms
    ]
    layout = dbc.Container(
        [
            html.H1("Algorithmus-Visualisierung", className="text-center my-4"),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(
                                        dbc.Label("Wähle einen Algorithmus:"),
                                        width="auto",
                                    ),
                                    dbc.Col(
                                        dcc.Dropdown(
                                            id="algorithm-selector",
                                            options=algorithm_options,
                                            value=(
                                                algorithm_options[0]["value"]
                                                if algorithm_options
                                                else None
                                            ),
                                        )
                                    ),
                                ],
                                className="mb-3",
                            ),
                            html.Div(
                                id="algorithm-description", className="my-3"
                            ),  # Neue Zeile
                            html.Div(id="dynamic-input-fields"),
                            dbc.Button(
                                "Berechnen",
                                id="submit-button",
                                color="primary",
                                className="w-100 my-2",
                            ),
                            html.Div(id="error-message", className="text-danger"),
                            html.Div(id="output-result", className="my-2"),
                        ],
                        md=4,
                    ),
                    dbc.Col(
                        [
                            dcc.Graph(id="algorithm-graph"),
                            dbc.Row(
                                [
                                    dbc.Col(dbc.Label("Schritt:"), width="auto"),
                                    dbc.Col(
                                        dcc.Slider(
                                            id="step-slider",
                                            min=0,
                                            max=0,
                                            step=1,
                                            value=0,
                                            marks={},
                                        )
                                    ),
                                ],
                                className="mb-3",
                            ),
                            html.Div(id="step-details"),
                        ],
                        md=8,
                    ),
                ]
            ),
        ],
        fluid=True,
    )
    return layout
