"""
framework.py

Hauptframework für die modulare Algorithmus-Visualisierung.

Dieses Modul stellt das zentrale Framework zur Verfügung, das die
Dash-Anwendung initialisiert, Algorithmen registriert, das Layout
einrichtet und die erforderlichen Callback-Funktionen für die
Interaktivität der Anwendung definiert.
"""

import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go

from algorithms.base_algorithm import BaseAlgorithm
from algorithms.ggt_algorithm import GGTAlgorithm
from algorithms.prime_number_algorithm import PrimeNumberAlgorithm
from algorithms.interest_calculation_algorithm import InterestCalculationAlgorithm  # Neuer Import

import config


class AlgorithmVisualizationFramework:
    """
    Framework zur Visualisierung von Algorithmen mit Dash.

    Dieses Framework ermöglicht die Registrierung verschiedener Algorithmen,
    die von der Basisklasse BaseAlgorithm abgeleitet sind, und stellt eine
    Benutzeroberfläche zur Verfügung, um diese Algorithmen interaktiv auszuführen
    und zu visualisieren.
    """

    def __init__(self):
        """Initialisiert das Dash-Framework und richtet die Grundkonfiguration ein."""
        self.app = dash.Dash(
            __name__,
            external_stylesheets=config.EXTERNAL_STYLESHEETS,
        )
        self.algorithms = {}
        self.setup_layout()
        self.setup_callbacks()

    def register_algorithm(self, algorithm: BaseAlgorithm):
        """
        Registriert einen neuen Algorithmus im Framework.

        Args:
            algorithm (BaseAlgorithm): Eine Instanz eines Algorithmus, der von BaseAlgorithm abgeleitet ist.
        """
        self.algorithms[algorithm.name] = algorithm

    def setup_layout(self):
        """Erstellt das initiale Layout der Dash-Anwendung."""
        self.app.layout = html.Div(
            [
                html.H1("Algorithmus-Visualisierung", className="header"),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Label(
                                    "Wähle einen Algorithmus:", className="label"
                                ),
                                dcc.Dropdown(
                                    id="algorithm-selector",
                                    options=[],
                                    value=None,
                                    className="dropdown",
                                ),
                                # Eingabefelder für GGTAlgorithm
                                html.Div(
                                    id="inputs-ggt",
                                    children=[
                                        dcc.Input(
                                            id="ggt-input-a",
                                            type="number",
                                            placeholder="Zahl A eingeben",
                                        ),
                                        dcc.Input(
                                            id="ggt-input-b",
                                            type="number",
                                            placeholder="Zahl B eingeben",
                                        ),
                                    ],
                                    style={"display": "none"},
                                ),
                                # Eingabefelder für PrimeNumberAlgorithm
                                html.Div(
                                    id="inputs-prime",
                                    children=[
                                        dcc.Input(
                                            id="prime-input-limit",
                                            type="number",
                                            placeholder="Obergrenze eingeben",
                                            min=2,
                                        )
                                    ],
                                    style={"display": "none"},
                                ),
                                # Eingabefelder für InterestCalculationAlgorithm
                                html.Div(
                                    id="inputs-interest",
                                    children=[
                                        dcc.Input(
                                            id="interest-input-initial-capital",
                                            type="number",
                                            placeholder="Anfangskapital eingeben",
                                            min=0,
                                        ),
                                        dcc.Input(
                                            id="interest-input-interest-rate",
                                            type="number",
                                            placeholder="Zinssatz in % eingeben",
                                            min=0,
                                        ),
                                        dcc.Input(
                                            id="interest-input-target-amount",
                                            type="number",
                                            placeholder="Zielsumme eingeben",
                                            min=0,
                                        ),
                                    ],
                                    style={"display": "none"},
                                ),
                                html.Button(
                                    "Berechnen",
                                    id="submit-button",
                                    n_clicks=0,
                                    className="button",
                                ),
                                html.Div(
                                    id="error-message", className="error-message"
                                ),
                                html.Div(id="output-result", className="result"),
                            ],
                            className="control-panel",
                        ),
                        html.Div(
                            [
                                dcc.Graph(id="algorithm-graph", className="graph"),
                                html.Div(
                                    [
                                        html.Label("Schritt:", className="label"),
                                        dcc.Slider(
                                            id="step-slider",
                                            min=0,
                                            max=0,
                                            step=1,
                                            value=0,
                                            marks={},
                                            className="slider",
                                        ),
                                    ],
                                    className="slider-container",
                                ),
                                html.Div(
                                    id="step-details", className="step-details"
                                ),
                            ],
                            className="visualization-panel",
                        ),
                    ],
                    className="main-content",
                ),
            ],
            className="container",
        )

    def update_layout(self):
        """Aktualisiert das Layout nach der Registrierung von Algorithmen."""
        algorithm_options = [
            {"label": name, "value": name} for name in self.algorithms.keys()
        ]
        self.app.layout.children[1].children[0].children[1].options = algorithm_options
        if self.algorithms:
            self.app.layout.children[1].children[0].children[1].value = list(
                self.algorithms.keys()
            )[0]

    def setup_callbacks(self):
        """Definiert die Callback-Funktionen für die Interaktivität der Anwendung."""

        @self.app.callback(
            [
                Output("inputs-ggt", "style"),
                Output("inputs-prime", "style"),
                Output("inputs-interest", "style"),
            ],
            Input("algorithm-selector", "value"),
        )
        def toggle_input_fields(selected_algorithm):
            """Zeigt die entsprechenden Eingabefelder basierend auf dem ausgewählten Algorithmus an."""
            if selected_algorithm == "Größter Gemeinsamer Teiler (GGT)":
                return {"display": "block"}, {"display": "none"}, {"display": "none"}
            elif selected_algorithm == "Primzahlen (Sieb des Eratosthenes)":
                return {"display": "none"}, {"display": "block"}, {"display": "none"}
            elif selected_algorithm == "Zinseszinsberechnung":
                return {"display": "none"}, {"display": "none"}, {"display": "block"}
            else:
                return {"display": "none"}, {"display": "none"}, {"display": "none"}

        @self.app.callback(
            [
                Output("output-result", "children"),
                Output("algorithm-graph", "figure"),
                Output("step-details", "children"),
                Output("error-message", "children"),
                Output("step-slider", "max"),
                Output("step-slider", "marks"),
                Output("step-slider", "value"),
            ],
            [Input("submit-button", "n_clicks"), Input("step-slider", "value")],
            [
                State("algorithm-selector", "value"),
                State("ggt-input-a", "value"),
                State("ggt-input-b", "value"),
                State("prime-input-limit", "value"),
                State("interest-input-initial-capital", "value"),
                State("interest-input-interest-rate", "value"),
                State("interest-input-target-amount", "value"),
            ],
            prevent_initial_call=True,
        )
        def update_output(
            n_clicks,
            step,
            selected_algorithm,
            ggt_a,
            ggt_b,
            prime_limit,
            initial_capital,
            interest_rate,
            target_amount,
        ):
            """
            Aktualisiert die Ausgabe basierend auf Benutzereingaben.

            Handhabt die Logik für die Ausführung des ausgewählten Algorithmus
            und die Aktualisierung der Visualisierung sowie der Schrittdetails.
            """
            ctx = dash.callback_context

            if not ctx.triggered:
                trigger_id = "No clicks yet"
            else:
                trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]

            if selected_algorithm in self.algorithms:
                algorithm = self.algorithms[selected_algorithm]

                if trigger_id == "submit-button":
                    # Verarbeitung bei Klick auf den Berechnungsbutton
                    try:
                        if isinstance(algorithm, GGTAlgorithm):
                            if ggt_a is None or ggt_b is None:
                                raise ValueError(
                                    "Bitte geben Sie beide Zahlen für den GGT-Algorithmus ein."
                                )
                            a = int(ggt_a)
                            b = int(ggt_b)
                            algorithm.run(a, b)
                        elif isinstance(algorithm, PrimeNumberAlgorithm):
                            if prime_limit is None:
                                raise ValueError(
                                    "Bitte geben Sie die Obergrenze für den Primzahlenalgorithmus ein."
                                )
                            limit = int(prime_limit)
                            algorithm.run(limit)
                        elif isinstance(algorithm, InterestCalculationAlgorithm):
                            if (
                                initial_capital is None
                                or interest_rate is None
                                or target_amount is None
                            ):
                                raise ValueError(
                                    "Bitte geben Sie alle Werte für die Zinseszinsberechnung ein."
                                )
                            initial_capital = float(initial_capital)
                            interest_rate = float(interest_rate)
                            target_amount = float(target_amount)
                            algorithm.run(
                                initial_capital, interest_rate, target_amount
                            )
                        max_steps = len(algorithm.steps) - 1
                        marks = {i: str(i) for i in range(max_steps + 1)}

                        # Anpassung der Achsenbeschriftungen
                        if isinstance(algorithm, GGTAlgorithm):
                            x_axis_title = "Schritt"
                            y_axis_title = "Wert"
                        elif isinstance(algorithm, PrimeNumberAlgorithm):
                            x_axis_title = "Zahl"
                            y_axis_title = "Schritt"
                        elif isinstance(algorithm, InterestCalculationAlgorithm):
                            x_axis_title = "Jahr"
                            y_axis_title = "Kapital (€)"
                        else:
                            x_axis_title = "X"
                            y_axis_title = "Y"

                        figure = {
                            "data": algorithm.get_visualization_data(max_steps),
                            "layout": go.Layout(
                                title=f"Schritte des {algorithm.name} Algorithmus",
                                xaxis={"title": x_axis_title},
                                yaxis={"title": y_axis_title},
                                template="plotly_white",
                            ),
                        }
                        return (
                            algorithm.get_result(),
                            figure,
                            algorithm.get_step_details(max_steps),
                            "",
                            max_steps,
                            marks,
                            max_steps,
                        )
                    except ValueError as e:
                        return (
                            "",
                            {},
                            [],
                            f"Fehler: {str(e)}",
                            0,
                            {},
                            0,
                        )
                    except Exception as e:
                        print(f"Fehler in update_output: {str(e)}")
                        return (
                            "",
                            {},
                            [],
                            f"Ein unerwarteter Fehler ist aufgetreten: {str(e)}",
                            0,
                            {},
                            0,
                        )

                elif trigger_id == "step-slider":
                    # Verarbeitung bei Änderung des Schiebereglers
                    try:
                        if algorithm.steps:
                            data = algorithm.get_visualization_data(step)

                            # Anpassung der Achsenbeschriftungen
                            if isinstance(algorithm, GGTAlgorithm):
                                x_axis_title = "Schritt"
                                y_axis_title = "Wert"
                            elif isinstance(algorithm, PrimeNumberAlgorithm):
                                x_axis_title = "Zahl"
                                y_axis_title = "Schritt"
                            elif isinstance(algorithm, InterestCalculationAlgorithm):
                                x_axis_title = "Jahr"
                                y_axis_title = "Kapital (€)"
                            else:
                                x_axis_title = "X"
                                y_axis_title = "Y"

                            layout = go.Layout(
                                title=f"Schritte des {algorithm.name} Algorithmus",
                                xaxis={"title": x_axis_title},
                                yaxis={"title": y_axis_title},
                                template="plotly_white",
                            )
                            figure = {"data": data, "layout": layout}
                            details = algorithm.get_step_details(step)
                            # Beibehalten der aktuellen Werte für andere Outputs
                            return (
                                dash.no_update,
                                figure,
                                details,
                                "",
                                dash.no_update,
                                dash.no_update,
                                dash.no_update,
                            )
                        else:
                            return (
                                "",
                                {},
                                [],
                                "Keine Daten zum Anzeigen. "
                                "Bitte führen Sie zuerst eine Berechnung durch.",
                                0,
                                {},
                                0,
                            )
                    except Exception as e:
                        print(f"Fehler in update_output: {str(e)}")
                        return (
                            "",
                            {},
                            [],
                            f"Ein Fehler ist aufgetreten: {str(e)}",
                            0,
                            {},
                            0,
                        )
                else:
                    # Wenn der Trigger unbekannt ist
                    return (
                        dash.no_update,
                        dash.no_update,
                        dash.no_update,
                        "",
                        dash.no_update,
                        dash.no_update,
                        dash.no_update,
                    )
            else:
                return "", {}, [], "Bitte wählen Sie einen Algorithmus aus.", 0, {}, 0

    def run_server(self, debug=True):
        """Startet den Dash-Server."""
        self.app.run_server(debug=debug)
