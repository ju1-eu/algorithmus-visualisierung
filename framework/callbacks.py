# framework/callbacks.py

"""
Definiert die Callback-Funktionen für die Interaktivität der Dash-Anwendung.
"""

from dash import html, dcc, callback, no_update
from dash.dependencies import Input, Output, State, ALL
import plotly.graph_objs as go
import dash

def register_callbacks(app, algorithms):
    """
    Registriert alle notwendigen Callback-Funktionen für die Anwendung.

    Args:
        app: Die Dash-Anwendung.
        algorithms: Liste der verfügbaren Algorithmusinstanzen.
    """

    # Hilfsfunktion, um einen Algorithmus anhand seines Namens zu erhalten
    def get_algorithm_by_name(name):
        for algo in algorithms:
            if algo.get_name() == name:
                return algo
        return None

    @app.callback(
        Output("dynamic-input-fields", "children"),
        Input("algorithm-selector", "value"),
    )
    def update_input_fields(selected_algorithm_name):
        """
        Aktualisiert die angezeigten Eingabefelder basierend auf dem ausgewählten Algorithmus.

        Args:
            selected_algorithm_name (str): Der Name des ausgewählten Algorithmus.

        Returns:
            html.Div: Ein Div-Element mit den dynamisch generierten Eingabefeldern.
        """
        algorithm = get_algorithm_by_name(selected_algorithm_name)
        if algorithm:
            return generate_input_fields(algorithm)
        else:
            return html.Div()

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
                html.Div(
                    [
                        html.Label(input_def["label"]),
                        field,
                    ],
                    className="my-2",
                )
            )
        return html.Div(fields, id="algorithm-input-fields")

    @app.callback(
        [
            Output("output-result", "children"),
            Output("algorithm-graph", "figure"),
            Output("step-details", "children"),
            Output("error-message", "children"),
            Output("step-slider", "max"),
            Output("step-slider", "marks"),
            Output("step-slider", "value"),
        ],
        [
            Input("submit-button", "n_clicks"),
            Input("step-slider", "value"),
        ],
        [
            State("algorithm-selector", "value"),
            State({"type": "algorithm-input", "index": ALL}, "value"),
            State({"type": "algorithm-input", "index": ALL}, "id"),
        ],
        prevent_initial_call=True,
    )
    def update_output(n_clicks, step_value, selected_algorithm_name, input_values, input_ids):
        """
        Aktualisiert die Ausgabe basierend auf Benutzereingaben und steuert die Algorithmusausführung.

        Args:
            n_clicks (int): Anzahl der Klicks auf den "Berechnen"-Button.
            step_value (int): Der aktuelle Wert des Schiebereglers.
            selected_algorithm_name (str): Der Name des ausgewählten Algorithmus.
            input_values (list): Liste der Werte der Eingabefelder.
            input_ids (list): Liste der IDs der Eingabefelder.

        Returns:
            Tuple: Aktualisierte Outputs für die Dash-Komponenten.
        """
        ctx = dash.callback_context
        trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]

        algorithm = get_algorithm_by_name(selected_algorithm_name)
        if not algorithm:
            return no_update, no_update, no_update, "Algorithmus nicht gefunden.", no_update, no_update, no_update

        # Eingaben als Dictionary zusammenfassen
        inputs = {id_dict["index"]: value for id_dict, value in zip(input_ids, input_values)}

        if trigger_id == "submit-button":
            # Algorithmus ausführen
            try:
                algorithm.run(inputs)
                max_steps = len(algorithm.steps) - 1
                marks = {i: str(i) for i in range(max_steps + 1)}

                figure = {
                    "data": algorithm.get_visualization_data(max_steps),
                    "layout": go.Layout(
                        title=f"Schritte des {algorithm.get_name()}",
                        xaxis={"title": "Index"},
                        yaxis={"title": "Wert"},
                        template="plotly_white",
                    ),
                }
                step_details = algorithm.get_step_details(max_steps)
                result = algorithm.get_result()
                return (
                    result,
                    figure,
                    step_details,
                    "",
                    max_steps,
                    marks,
                    max_steps,
                )
            except ValueError as e:
                return "", {}, "", f"Fehler: {str(e)}", 0, {}, 0
            except Exception as e:
                print(f"Fehler in update_output: {str(e)}")
                return "", {}, "", "Ein unerwarteter Fehler ist aufgetreten.", 0, {}, 0

        elif trigger_id == "step-slider":
            # Visualisierung für den ausgewählten Schritt aktualisieren
            try:
                if algorithm.steps:
                    data = algorithm.get_visualization_data(step_value)
                    figure = {
                        "data": data,
                        "layout": go.Layout(
                            title=f"Schritte des {algorithm.get_name()}",
                            xaxis={"title": "Index"},
                            yaxis={"title": "Wert"},
                            template="plotly_white",
                        ),
                    }
                    step_details = algorithm.get_step_details(step_value)
                    return no_update, figure, step_details, "", no_update, no_update, no_update
                else:
                    return "", {}, "", "Bitte führen Sie zuerst eine Berechnung durch.", 0, {}, 0
            except Exception as e:
                print(f"Fehler in update_output: {str(e)}")
                return "", {}, "", "Ein Fehler ist aufgetreten.", 0, {}, 0
        else:
            return no_update, no_update, no_update, "", no_update, no_update, no_update
