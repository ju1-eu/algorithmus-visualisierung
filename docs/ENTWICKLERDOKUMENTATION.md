---
title: "ENTWICKLERDOKUMENTATION"
author: "Jan Unger"
date: "2024-10-10"
---

# Entwicklerdokumentation zum Algorithmus-Visualisierungs-Framework

bearbeitet am 12. Oktober 2024

- [Entwicklerdokumentation zum Algorithmus-Visualisierungs-Framework](#entwicklerdokumentation-zum-algorithmus-visualisierungs-framework)
  - [Überblick](#überblick)
  - [Architektur und Struktur](#architektur-und-struktur)
    - [Verzeichnisstruktur](#verzeichnisstruktur)
  - [Hauptkomponenten](#hauptkomponenten)
    - [1. `BaseAlgorithm` (Basisklasse für Algorithmen)](#1-basealgorithm-basisklasse-für-algorithmen)
      - [Beschreibung](#beschreibung)
      - [Methoden](#methoden)
      - [Beispiel](#beispiel)
    - [2. Dynamische Eingabefelder](#2-dynamische-eingabefelder)
    - [3. Polymorphe Methoden](#3-polymorphe-methoden)
    - [4. Modularisierung des Codes](#4-modularisierung-des-codes)
    - [5. Verbesserte Fehlerbehandlung](#5-verbesserte-fehlerbehandlung)
  - [Verwendung des Frameworks](#verwendung-des-frameworks)
    - [Anwendung starten](#anwendung-starten)
    - [Hinzufügen neuer Algorithmen](#hinzufügen-neuer-algorithmen)
      - [Schritt 1: Algorithmusklasse erstellen](#schritt-1-algorithmusklasse-erstellen)
      - [Schritt 2: Keine manuelle Registrierung erforderlich](#schritt-2-keine-manuelle-registrierung-erforderlich)
    - [Plugin-System](#plugin-system)
  - [Interna des Frameworks](#interna-des-frameworks)
    - [Dynamische Eingabefelder](#dynamische-eingabefelder)
    - [Polymorphe Callback-Funktionen](#polymorphe-callback-funktionen)
  - [Best Practices und Empfehlungen](#best-practices-und-empfehlungen)
    - [Nutzung von Polymorphie](#nutzung-von-polymorphie)
    - [Dynamische Eingabefelder](#dynamische-eingabefelder-1)
    - [Modularisierung](#modularisierung)
    - [Verbesserte Fehlerbehandlung](#verbesserte-fehlerbehandlung)
    - [Dokumentation und Kommentare](#dokumentation-und-kommentare)
  - [Beispiel: Hinzufügen des "Bubble Sort"-Algorithmus](#beispiel-hinzufügen-des-bubble-sort-algorithmus)
    - [Algorithmusklasse erstellen](#algorithmusklasse-erstellen)
    - [Keine weitere Anpassung erforderlich](#keine-weitere-anpassung-erforderlich)
  - [Fehlerbehandlung und Benutzerrückmeldung](#fehlerbehandlung-und-benutzerrückmeldung)
  - [Erweiterte Funktionen](#erweiterte-funktionen)
    - [Automatisches Laden von Algorithmen](#automatisches-laden-von-algorithmen)
    - [Externe Konfigurationsdateien (optional)](#externe-konfigurationsdateien-optional)
  - [Häufig gestellte Fragen (FAQ)](#häufig-gestellte-fragen-faq)
    - [Wie füge ich einen neuen Algorithmus hinzu?](#wie-füge-ich-einen-neuen-algorithmus-hinzu)
    - [Muss ich das Layout oder die Callback-Funktionen anpassen?](#muss-ich-das-layout-oder-die-callback-funktionen-anpassen)
    - [Wie werden Eingabefehler behandelt?](#wie-werden-eingabefehler-behandelt)
  - [Zusammenfassung](#zusammenfassung)
  - [Nächste Schritte für Entwickler](#nächste-schritte-für-entwickler)
  - [Aktualisierte Projektstruktur und Komponenten](#aktualisierte-projektstruktur-und-komponenten)
    - [Verzeichnisstruktur](#verzeichnisstruktur-1)
    - [Hauptkomponenten](#hauptkomponenten-1)
    - [Verwendung des Makefiles](#verwendung-des-makefiles)
    - [Ausführen von Tests](#ausführen-von-tests)
    - [Dokumentationsgenerierung](#dokumentationsgenerierung)
    - [Integration von template.html](#integration-von-templatehtml)
    - [Zusätzliche Ressourcen](#zusätzliche-ressourcen)
    - [Entwicklungsumgebung](#entwicklungsumgebung)
    - [Versionskontrolle](#versionskontrolle)

## Überblick

Das Algorithmus-Visualisierungs-Framework ist eine modulare und erweiterbare Plattform zur interaktiven Darstellung von Algorithmen mithilfe von Dash und Plotly. Es wurde entwickelt, um Entwicklern das Hinzufügen neuer Algorithmen mit minimalem Aufwand zu ermöglichen und gleichzeitig eine robuste und wartbare Codebasis bereitzustellen.

---

## Architektur und Struktur

### Verzeichnisstruktur

```
.
├── algorithms/
│   ├── base_algorithm.py
│   ├── ggt_algorithm.py
│   ├── prime_number_algorithm.py
│   ├── bubble_sort_algorithm.py
│   └── ...
├── framework/
│   ├── __init__.py
│   ├── app.py
│   ├── layout.py
│   ├── callbacks.py
│   └── plugin_loader.py
├── config.py
├── main.py
└── requirements.txt
```

- **`algorithms/`**: Enthält alle Algorithmusimplementierungen. Jeder Algorithmus ist in einer eigenen Datei definiert und erbt von `BaseAlgorithm`.
- **`framework/`**: Beinhaltet die Hauptkomponenten des Frameworks, aufgeteilt in Initialisierung, Layout, Callback-Funktionen und Plugin-Lader.
- **`config.py`**: Enthält Konfigurationsparameter und globale Einstellungen.
- **`main.py`**: Startet die Anwendung und registriert die Algorithmen über das Plugin-System.
- **`requirements.txt`**: Listet die Abhängigkeiten des Projekts auf.

---

## Hauptkomponenten

### 1. `BaseAlgorithm` (Basisklasse für Algorithmen)

**Datei**: `algorithms/base_algorithm.py`

#### Beschreibung

Die `BaseAlgorithm`-Klasse definiert die Schnittstelle für alle Algorithmen und stellt gemeinsame Funktionalitäten bereit. Sie nutzt abstrakte Methoden, um sicherzustellen, dass alle Unterklassen die erforderlichen Methoden implementieren.

#### Methoden

- **`get_name(self) -> str`**: Gibt den Namen des Algorithmus zurück, der im Dropdown-Menü angezeigt wird.
- **`get_inputs(self) -> List[Dict]`**: Definiert die benötigten Eingabefelder und deren Eigenschaften (z. B. `id`, `label`, `type`, `placeholder`).
- **`run(self, inputs: Dict)`**: Führt den Algorithmus mit den übergebenen Eingaben aus. Validiert die Eingaben und füllt `self.steps` und `self.result`.
- **`get_visualization_data(self, step: int) -> List[Dict]`**: Bereitet die Daten für die Visualisierung des aktuellen Schritts auf.
- **`get_step_details(self, step: int) -> str`**: Gibt eine Beschreibung oder Details zum aktuellen Schritt zurück.
- **`get_result(self) -> str`**: Gibt das Endergebnis des Algorithmus als lesbaren String zurück.

#### Beispiel

```python
from abc import ABC, abstractmethod

class BaseAlgorithm(ABC):
    def __init__(self):
        self.steps = []
        self.result = None

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_inputs(self):
        pass

    @abstractmethod
    def run(self, inputs):
        pass

    @abstractmethod
    def get_visualization_data(self, step):
        pass

    @abstractmethod
    def get_step_details(self, step):
        pass

    @abstractmethod
    def get_result(self):
        pass
```

### 2. Dynamische Eingabefelder

**Beschreibung**

Die Eingabefelder werden dynamisch generiert, basierend auf den Anforderungen des ausgewählten Algorithmus. Jeder Algorithmus definiert über `get_inputs()` die benötigten Eingaben.

**Implementierung**

- **In `layout.py`**: Funktion `generate_input_fields(algorithm)` erstellt die Eingabefelder zur Laufzeit.
- **In `callbacks.py`**: Die Callback-Funktion verarbeitet die dynamisch generierten Eingabewerte.

### 3. Polymorphe Methoden

**Beschreibung**

Anstatt `isinstance`-Abfragen zu verwenden, werden polymorphe Methoden genutzt. Dadurch werden algorithmusspezifische Logiken in den jeweiligen Klassen gekapselt, und der Code wird flexibler und wartbarer.

### 4. Modularisierung des Codes

**Beschreibung**

Der Code ist in klare Module aufgeteilt:

- **`app.py`**: Initialisiert die Dash-Anwendung.
- **`layout.py`**: Definiert das Layout der Anwendung.
- **`callbacks.py`**: Enthält alle Callback-Funktionen.
- **`plugin_loader.py`**: Lädt die Algorithmen dynamisch aus dem `algorithms/`-Verzeichnis.

### 5. Verbesserte Fehlerbehandlung

**Beschreibung**

- **Eingabevalidierung**: Innerhalb der `run()`-Methode jedes Algorithmus werden die Eingaben validiert.
- **Klare Fehlermeldungen**: Bei ungültigen Eingaben werden aussagekräftige Fehlermeldungen an den Benutzer zurückgegeben.
- **Spezifische Exceptions**: Anstelle generischer Exceptions werden spezifische Fehler geworfen.

---

## Verwendung des Frameworks

### Anwendung starten

**In `main.py`**

```python
from framework.app import app
from framework.plugin_loader import load_algorithms
from framework import layout, callbacks

# Algorithmen laden und registrieren
algorithms = load_algorithms()
app.layout = layout.create_layout(algorithms)

if __name__ == '__main__':
    app.run_server(debug=True)
```

### Hinzufügen neuer Algorithmen

#### Schritt 1: Algorithmusklasse erstellen

**Datei anlegen**: `algorithms/mein_algorithmus.py`

```python
from algorithms.base_algorithm import BaseAlgorithm

class MeinAlgorithmus(BaseAlgorithm):
    def get_name(self):
        return "Mein Algorithmus"

    def get_inputs(self):
        return [
            {
                "id": "parameter1",
                "label": "Parameter 1",
                "type": "number",
                "placeholder": "Geben Sie Parameter 1 ein"
            },
            # Weitere Eingabefelder nach Bedarf
        ]

    def run(self, inputs):
        parameter1 = inputs.get("parameter1")
        if parameter1 is None:
            raise ValueError("Parameter 1 darf nicht leer sein.")
        # Implementierung des Algorithmus
        self.steps = []
        self.result = None
        # Algorithmuslogik hier einfügen

    def get_visualization_data(self, step):
        # Daten für die Visualisierung des Schritts 'step' aufbereiten
        return [...]

    def get_step_details(self, step):
        return f"Schritt {step}: Beschreibung"

    def get_result(self):
        return f"Ergebnis: {self.result}"
```

#### Schritt 2: Keine manuelle Registrierung erforderlich

Dank des Plugin-Systems wird der neue Algorithmus automatisch erkannt und geladen. Es ist keine Anpassung von `main.py` oder anderen Dateien erforderlich.

### Plugin-System

**Datei**: `framework/plugin_loader.py`

**Beschreibung**

Das Plugin-System lädt automatisch alle Algorithmusklassen aus dem `algorithms/`-Verzeichnis, die von `BaseAlgorithm` erben.

**Implementierung**

```python
import pkgutil
import importlib
import algorithms
from algorithms.base_algorithm import BaseAlgorithm

def load_algorithms():
    algorithms_list = []
    for loader, module_name, is_pkg in pkgutil.iter_modules(algorithms.__path__):
        module = importlib.import_module(f"algorithms.{module_name}")
        for attr in dir(module):
            obj = getattr(module, attr)
            if isinstance(obj, type) and issubclass(obj, BaseAlgorithm) and obj is not BaseAlgorithm:
                algorithms_list.append(obj())
    return algorithms_list
```

---

## Interna des Frameworks

### Dynamische Eingabefelder

**In `layout.py`**

```python
from dash import html, dcc

def generate_input_fields(algorithm):
    inputs = algorithm.get_inputs()
    fields = []
    for input_def in inputs:
        field = dcc.Input(
            id={"type": "algorithm-input", "index": input_def["id"]},
            type=input_def.get("type", "text"),
            placeholder=input_def.get("placeholder", ""),
        )
        fields.append(html.Div([html.Label(input_def["label"]), field]))
    return html.Div(fields, id="algorithm-input-fields")
```

### Polymorphe Callback-Funktionen

**In `callbacks.py`**

```python
from dash.dependencies import Input, Output, State, ALL
from dash import callback, no_update

@callback(
    Output("output-result", "children"),
    Output("algorithm-graph", "figure"),
    Output("step-details", "children"),
    Output("error-message", "children"),
    Output("step-slider", "max"),
    Output("step-slider", "marks"),
    Output("step-slider", "value"),
    Input("submit-button", "n_clicks"),
    Input("step-slider", "value"),
    State("algorithm-selector", "value"),
    State({"type": "algorithm-input", "index": ALL}, "value"),
    prevent_initial_call=True,
)
def update_output(n_clicks, step, selected_algorithm, input_values):
    algorithm = get_algorithm_by_name(selected_algorithm)
    inputs = {input_def["id"]: value for input_def, value in zip(algorithm.get_inputs(), input_values)}
    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if trigger_id == "submit-button":
        try:
            algorithm.run(inputs)
            max_steps = len(algorithm.steps) - 1
            marks = {i: str(i) for i in range(max_steps + 1)}
            figure = {
                "data": algorithm.get_visualization_data(max_steps),
                "layout": go.Layout(
                    title=f"Schritte des {algorithm.get_name()}",
                    xaxis={"title": "X-Achse"},
                    yaxis={"title": "Y-Achse"},
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
            return "", {}, "", f"Fehler: {str(e)}", 0, {}, 0
    elif trigger_id == "step-slider":
        data = algorithm.get_visualization_data(step)
        figure = {
            "data": data,
            "layout": go.Layout(
                title=f"Schritte des {algorithm.get_name()}",
                xaxis={"title": "X-Achse"},
                yaxis={"title": "Y-Achse"},
                template="plotly_white",
            ),
        }
        details = algorithm.get_step_details(step)
        return no_update, figure, details, "", no_update, no_update, no_update
    else:
        return no_update, no_update, no_update, "", no_update, no_update, no_update
```

---

## Best Practices und Empfehlungen

### Nutzung von Polymorphie

- **Vorteile**: Reduziert die Notwendigkeit von Typabfragen und erhöht die Flexibilität.
- **Umsetzung**: Alle algorithmusspezifischen Methoden werden in den jeweiligen Klassen implementiert.

### Dynamische Eingabefelder

- **Vorteile**: Erleichtert das Hinzufügen neuer Algorithmen ohne Anpassung des Layouts.
- **Umsetzung**: Algorithmen definieren ihre Eingaben über die Methode `get_inputs()`.

### Modularisierung

- **Vorteile**: Erhöht die Übersichtlichkeit und Wartbarkeit des Codes.
- **Umsetzung**: Aufteilung des Codes in Module für Layout, Callbacks und Plugin-Loading.

### Verbesserte Fehlerbehandlung

- **Vorteile**: Bessere Benutzererfahrung durch klare Fehlermeldungen.
- **Umsetzung**: Validierung der Eingaben in der `run()`-Methode und spezifische Exceptions.

### Dokumentation und Kommentare

- **Vorteile**: Erleichtert neuen Entwicklern den Einstieg und fördert die Zusammenarbeit.
- **Umsetzung**: Ausführliche Docstrings und Kommentare in allen Klassen und Methoden.

---

## Beispiel: Hinzufügen des "Bubble Sort"-Algorithmus

### Algorithmusklasse erstellen

**Datei**: `algorithms/bubble_sort_algorithm.py`

```python
from algorithms.base_algorithm import BaseAlgorithm

class BubbleSortAlgorithm(BaseAlgorithm):
    def get_name(self):
        return "Bubble Sort"

    def get_inputs(self):
        return [
            {
                "id": "input_array",
                "label": "Eingabe-Array",
                "type": "text",
                "placeholder": "Liste von Zahlen, kommagetrennt",
            }
        ]

    def run(self, inputs):
        data_input = inputs.get("input_array")
        if not data_input:
            raise ValueError("Bitte geben Sie eine Liste von Zahlen ein.")
        try:
            data = [int(x.strip()) for x in data_input.split(',')]
        except ValueError:
            raise ValueError("Die Eingabe muss eine Liste von Zahlen sein.")
        self.steps = []
        arr = data.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                self.steps.append(arr.copy())
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        self.result = arr
        self.steps.append(arr.copy())

    def get_visualization_data(self, step):
        return [{
            'x': list(range(len(self.steps[step]))),
            'y': self.steps[step],
            'type': 'bar'
        }]

    def get_step_details(self, step):
        return f"Schritt {step}: {self.steps[step]}"

    def get_result(self):
        return f"Sortiertes Array: {self.result}"
```

### Keine weitere Anpassung erforderlich

Der neue Algorithmus wird automatisch vom Plugin-System erkannt und in die Anwendung integriert.

---

## Fehlerbehandlung und Benutzerrückmeldung

- **Eingabevalidierung**: Jeder Algorithmus ist verantwortlich für die Validierung seiner Eingaben.
- **Fehlermeldungen**: Klare und spezifische Fehlermeldungen werden an die Benutzeroberfläche weitergeleitet.
- **Exception-Handling**: Verwendung von spezifischen Exceptions wie `ValueError`.

---

## Erweiterte Funktionen

### Automatisches Laden von Algorithmen

- **Beschreibung**: Das Plugin-System durchsucht das `algorithms/`-Verzeichnis und lädt alle Klassen, die von `BaseAlgorithm` erben.
- **Vorteile**: Neue Algorithmen können hinzugefügt werden, ohne den bestehenden Code zu ändern.

### Externe Konfigurationsdateien (optional)

- **Beschreibung**: Metadaten und Eingabedefinitionen könnten in Zukunft aus externen Dateien wie JSON oder YAML geladen werden.
- **Vorteile**: Erhöht die Flexibilität und ermöglicht Nicht-Programmierern, Algorithmen zu konfigurieren.

---

## Häufig gestellte Fragen (FAQ)

### Wie füge ich einen neuen Algorithmus hinzu?

1. Erstellen Sie eine neue Datei im `algorithms/`-Verzeichnis.
2. Definieren Sie eine Klasse, die von `BaseAlgorithm` erbt.
3. Implementieren Sie alle abstrakten Methoden.
4. Der Algorithmus wird automatisch vom Plugin-System geladen.

### Muss ich das Layout oder die Callback-Funktionen anpassen?

Nein, dank der dynamischen Eingabefelder und der Nutzung von Polymorphie ist keine Anpassung erforderlich.

### Wie werden Eingabefehler behandelt?

Eingabefehler sollten innerhalb der `run()`-Methode des Algorithmus erkannt und durch Werfen einer `ValueError` mit einer aussagekräftigen Fehlermeldung behandelt werden.

---

## Zusammenfassung

Das Algorithmus-Visualisierungs-Framework wurde entwickelt, um Entwicklern eine einfache und effiziente Möglichkeit zu bieten, neue Algorithmen hinzuzufügen und zu visualisieren. Durch die Implementierung von Best Practices wie dynamische Eingabefelder, Nutzung von Polymorphie, Modularisierung und verbesserte Fehlerbehandlung ist das Framework sowohl wartungsfreundlich als auch erweiterbar.

---

## Nächste Schritte für Entwickler

1. **Einarbeitung**: Lesen Sie diese Dokumentation gründlich, um das Framework zu verstehen.
2. **Erste Implementierung**: Versuchen Sie, einen einfachen Algorithmus hinzuzufügen, um den Prozess zu verinnerlichen.
3. **Feedback geben**: Teilen Sie Verbesserungsvorschläge oder melden Sie Probleme, um das Framework weiter zu optimieren.
4. **Weiterentwicklung**: Beteiligen Sie sich aktiv an der Weiterentwicklung des Frameworks, indem Sie neue Funktionen oder Algorithmen beitragen.

---

**Hinweis**: Diese Dokumentation wurde aktualisiert, um alle Änderungen und neuen Funktionen zu reflektieren, die die Wartungsfreundlichkeit und Erweiterbarkeit des Algorithmus-Visualisierungs-Frameworks verbessern. Sie dient als Leitfaden für Entwickler, die mit dem Framework arbeiten oder es erweitern möchten.

## Aktualisierte Projektstruktur und Komponenten

Das Projekt hat sich seit der ursprünglichen Dokumentation weiterentwickelt. Hier ist eine umfassende Übersicht über die aktuelle Struktur und die Funktionen der Komponenten:

### Verzeichnisstruktur

```
.
├── .venv/                 # Virtuelle Python-Umgebung
├── algorithms/            # Algorithmus-Implementierungen
├── docs/                  # Dokumentation und zusätzliche Ressourcen
│   ├── Algorithmen-Erklärung/
│   ├── Aufgaben/
│   ├── KI/
│   ├── LaTeX/
│   ├── MindMaps/
│   └── images/
├── framework/             # Kernkomponenten des Frameworks
├── scripts/               # Hilfsskripte
├── tests/                 # Unittest-Dateien
├── .git/                  # Git-Repository-Informationen
├── .gitignore             # Git-Ignorier-Datei
├── config.py              # Konfigurationsdatei
├── main.py                # Haupteinstiegspunkt der Anwendung
├── run_tests.py           # Skript zum Ausführen von Tests
├── requirements.txt       # Python-Abhängigkeiten
├── Makefile               # Build-Automatisierung
├── README.md              # Projekt-Readme
└── template.html          # HTML-Template für die Dokumentation
```

### Hauptkomponenten

1. **algorithms/**:
   - Enthält alle Algorithmus-Implementierungen
   - Jeder Algorithmus ist in einer separaten Datei definiert
   - Beispiele: `base_algorithm.py`, `ggt_algorithm.py`, `bubble_sort_algorithm.py`, etc.

2. **docs/**:
   - Umfangreiche Dokumentation und zusätzliche Ressourcen
   - Unterverzeichnisse für spezifische Themen wie Algorithmen-Erklärungen, KI, LaTeX-Vorlagen
   - Enthält auch Bilder und MindMaps

3. **framework/**:
   - Kernkomponenten des Visualisierungs-Frameworks
   - Enthält `app.py`, `callbacks.py`, `layout.py`, und `plugin_loader.py`

4. **scripts/**:
   - Hilfsskripte für verschiedene Aufgaben:
     - `add_front_matter.sh`: Fügt Front Matter zu Markdown-Dateien hinzu
     - `backup_cloud_start.sh` und `backup_usbstick_start.sh`: Backup-Skripte
     - `git_setup.sh`: Git-Konfigurationsskript
     - `setup_environment.sh`: Skript zur Einrichtung der Entwicklungsumgebung

5. **tests/**:
   - Enthält Unittest-Dateien für verschiedene Algorithmen
   - Beispiele: `test_bubble_sort_algorithm.py`, `test_ggt_algorithm.py`, etc.

6. **main.py**:
   - Haupteinstiegspunkt der Anwendung
   - Initialisiert und startet die Dash-Anwendung
   - Lädt Algorithmen über das Plugin-System

7. **run_tests.py**:
   - Skript zum Ausführen aller Unittests

8. **Makefile**:
   - Automatisiert den Build-Prozess und andere Entwicklungsaufgaben
   - Hauptfunktionen:
     - Konvertierung von Markdown zu HTML
     - Generierung eines Inhaltsverzeichnisses
     - Hinzufügen von Front Matter zu Markdown-Dateien

9. **template.html**:
   - HTML-Template für die generierten Dokumentationsseiten
   - Enthält Verweise auf CSS-Dateien und JavaScript-Bibliotheken

### Verwendung des Makefiles

Das Makefile bietet verschiedene Targets zur Automatisierung von Aufgaben:

- `make all`: Konvertiert alle Markdown-Dateien zu HTML und erstellt das Inhaltsverzeichnis
- `make html`: Konvertiert nur die Markdown-Dateien zu HTML
- `make index`: Generiert das Inhaltsverzeichnis (start.md/start.html)
- `make clean`: Löscht generierte HTML-Dateien

### Ausführen von Tests

Tests können mit dem folgenden Befehl ausgeführt werden:

```bash
python run_tests.py
```

### Dokumentationsgenerierung

Die Dokumentation wird aus Markdown-Dateien im `docs/`-Verzeichnis generiert. Der Prozess umfasst:

1. Hinzufügen von Front Matter zu Markdown-Dateien
2. Konvertierung von Markdown zu HTML mit Pandoc
3. Anwendung des benutzerdefinierten CSS und HTML-Templates
4. Generierung eines Inhaltsverzeichnisses (start.html)

Um die Dokumentation zu aktualisieren, führen Sie `make all` aus.

### Integration von template.html

Die `template.html`-Datei dient als Basis für alle generierten HTML-Seiten. Sie enthält:

- Verweise auf externe CSS-Dateien für Styling
- JavaScript-Bibliotheken für Syntax-Highlighting (Prism) und LaTeX-Rendering (MathJax)
- Eine grundlegende HTML-Struktur, in die der generierte Inhalt eingefügt wird

### Zusätzliche Ressourcen

- **LaTeX/**: Enthält LaTeX-Vorlagen und zugehörige Dateien für die Erstellung von PDF-Dokumenten
- **MindMaps/**: Beinhaltet MindMap-Dateien zur Visualisierung von Konzepten
- **Algorithmen-Erklärung/**: Detaillierte Erklärungen spezifischer Algorithmen
- **KI/**: Dokumentation zu KI-bezogenen Themen und Prompts

### Entwicklungsumgebung

Das Projekt verwendet eine virtuelle Python-Umgebung (.venv/). Stellen Sie sicher, diese zu aktivieren, bevor Sie am Projekt arbeiten.

### Versionskontrolle

Das Projekt verwendet Git für die Versionskontrolle. Die `.gitignore`-Datei ist so konfiguriert, dass temporäre und umgebungsspezifische Dateien nicht im Repository gespeichert werden.
