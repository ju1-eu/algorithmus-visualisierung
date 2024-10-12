# Algorithmus-Visualisierung

bearbeitet am 12. Oktober 2024

## Übersicht

Willkommen zur **Algorithmus-Visualisierung** – einem modularen Framework zur interaktiven Visualisierung von Algorithmen wie dem Größten Gemeinsamen Teiler (GGT) und dem Sieb des Eratosthenes für Primzahlen. Dieses Tool wurde entwickelt, um das Verständnis für Algorithmen durch visuelle Darstellung ihrer Schritte zu fördern.

## Inhaltsverzeichnis

- [Algorithmus-Visualisierung](#algorithmus-visualisierung)
  - [Übersicht](#übersicht)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Installation](#installation)
    - [Voraussetzungen](#voraussetzungen)
    - [Schritte](#schritte)
  - [Verwendung](#verwendung)
    - [Anwendung starten](#anwendung-starten)
    - [Funktionen](#funktionen)
  - [Hinzufügen neuer Algorithmen](#hinzufügen-neuer-algorithmen)
  - [Beispiele](#beispiele)
    - [Verwendung der abstrakten Basisklasse](#verwendung-der-abstrakten-basisklasse)
  - [Fehler- und Ausnahmebehandlung](#fehler--und-ausnahmebehandlung)
  - [Tests](#tests)
  - [Beitrag leisten](#beitrag-leisten)
  - [Lizenz](#lizenz)

## Installation

### Voraussetzungen

- **Python 3.6+**
- **pip** Paketmanager

### Schritte

1. **Repository klonen:**

   ```bash
   git clone https://github.com/ju1-eu/algorithmus-visualisierung.git
   cd algorithmus-visualisierung
   ```

2. **Virtuelle Umgebung erstellen und aktivieren:**

   Für Unix/Mac:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   Für Windows:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Abhängigkeiten installieren:**

   ```bash
   pip install -r requirements.txt
   pip install dash plotly

   # Automatische Codeformatierung:
   pip install black
   black .
   git diff
   black . --diff
   
   # Code-Analyse-Tools
   pip install pylint
   pylint main.py

   # Automatisches Aktualisieren von requirements.txt
   pip freeze > requirements.txt
   which python
   python --version
   python -m pip install --upgrade pip
   pip list --outdated
   pip install --upgrade <paketname>
   brew update && brew upgrade
   ```

## Verwendung

### Anwendung starten

Starten Sie die Anwendung mit dem folgenden Befehl:

```bash
################################################
# Projektstruktur
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
├── docs/
├── config.py
├── main.py
├── run_tests.py
└── requirements.txt
└── Makefile
└── template.html
################################################
# Terminal öffnen: jan@imacj $
python3 -m venv .venv
source .venv/bin/activate
# (.venv) jan@imacj $
pip install -r requirements.txt

python main.py
python run_tests.py

black .
pylint algorithms/john_mcclane_algorithm.py

make
make clean

git add .
git commit -m""
git push
```

Öffnen Sie dann Ihren Webbrowser und navigieren Sie zu [http://127.0.0.1:8050/](http://127.0.0.1:8050/), um die Anwendung zu verwenden.

### Funktionen

- **Algorithmusauswahl:** Wählen Sie zwischen verschiedenen Algorithmen zur Visualisierung.
- **Eingabeparameter:** Geben Sie die erforderlichen Parameter für den ausgewählten Algorithmus ein.
- **Visualisierung:** Sehen Sie sich die schrittweise Ausführung des Algorithmus an.
- **Interaktion:** Verwenden Sie den Schieberegler, um zwischen den einzelnen Schritten zu navigieren.

## Hinzufügen neuer Algorithmen

Das Framework ermöglicht es Ihnen, neue Algorithmen einfach hinzuzufügen, indem Sie die abstrakte Basisklasse `BaseAlgorithm` verwenden. Folgen Sie diesen Schritten:

1. **Neue Algorithmusklasse erstellen:**

   Erstellen Sie eine neue Python-Datei im Verzeichnis `algorithms/`, z. B. `example_algorithm.py`.

2. **Von `BaseAlgorithm` erben:**

   Importieren Sie die Basisklasse und erstellen Sie Ihre Klasse, die von `BaseAlgorithm` erbt:

   ```python
   from algorithms.base_algorithm import BaseAlgorithm

   class ExampleAlgorithm(BaseAlgorithm):
       # Implementierung folgt...
   ```

3. **Erforderliche Methoden implementieren:**

   Implementieren Sie die abstrakten Methoden:

   - `name` (Property): Gibt den Namen des Algorithmus zurück.
   - `run(self, *args, **kwargs)`: Führt den Algorithmus aus.
   - `get_visualization_data(self, step=None)`: Bereitet die Daten für die Visualisierung vor.
   - `get_result(self)`: Gibt das Ergebnis des Algorithmus zurück.
   - `get_step_details(self, step=None)`: Gibt Details zum aktuellen Schritt zurück.

4. **Beispielimplementierung:**

   ```python
   from algorithms.base_algorithm import BaseAlgorithm

   class ExampleAlgorithm(BaseAlgorithm):
       def __init__(self):
           self._name = "Beispielalgorithmus"
           self.steps = []
           self.result = None

       @property
       def name(self):
           return self._name

       def run(self, input_value):
           # Implementierung des Algorithmus
           pass

       def get_visualization_data(self, step=None):
           # Daten für die Visualisierung vorbereiten
           pass

       def get_result(self):
           # Ergebnis zurückgeben
           return f"Das Ergebnis ist {self.result}"

       def get_step_details(self, step=None):
           # Details zum aktuellen Schritt
           pass
   ```

5. **Algorithmus registrieren:**

   Fügen Sie Ihren Algorithmus in `main.py` hinzu:

   ```python
   from algorithms.example_algorithm import ExampleAlgorithm

   # ...

   framework.register_algorithm(ExampleAlgorithm())
   ```

6. **Eingabefelder hinzufügen:**

   Wenn Ihr Algorithmus spezielle Eingaben benötigt, passen Sie `framework.py` an:

   - Fügen Sie im Layout die notwendigen Eingabefelder hinzu.
   - Aktualisieren Sie die Callback-Funktionen, um die neuen Eingaben zu verarbeiten.

## Beispiele

### Verwendung der abstrakten Basisklasse

Die Verwendung der abstrakten Basisklasse `BaseAlgorithm` stellt sicher, dass alle Algorithmen eine einheitliche Schnittstelle bieten. Dies erleichtert die Integration neuer Algorithmen in das Framework.

*Beispiel:* Siehe Abschnitt **Hinzufügen neuer Algorithmen**.

## Fehler- und Ausnahmebehandlung

Das Framework implementiert eine konsistente Fehler- und Ausnahmebehandlung:

- **In Algorithmen:**
  - Überprüfen Sie die Eingabedaten und werfen Sie aussagekräftige Ausnahmen (`ValueError`, `TypeError`).
  - Dokumentieren Sie in den Docstrings, welche Ausnahmen geworfen werden können.

*Beispiel in einem Algorithmus:*

```python
def run(self, input_value):
    """
    Führt den Algorithmus aus.

    Args:
        input_value (int): Die Eingabe für den Algorithmus.

    Raises:
        ValueError: Wenn die Eingabe ungültig ist.
    """
    if input_value <= 0:
        raise ValueError("Die Eingabe muss positiv sein.")
    # Algorithmusimplementierung...
```

- **Im Framework:**
  - Fangt spezifische Ausnahmen ab und zeigt dem Benutzer hilfreiche Fehlermeldungen an.
  - Allgemeine Ausnahmen werden protokolliert und eine generische Fehlermeldung wird angezeigt.

## Tests

Zum Ausführen der Unit-Tests verwenden Sie:

```bash
python main.py --test
```

Dies führt die Tests für die Algorithmen aus und stellt sicher, dass alles korrekt funktioniert.

## Beitrag leisten

Wir freuen uns über Beiträge von der Community! Bitte lesen Sie unsere [Beitragsrichtlinien](CONTRIBUTING.md), um zu erfahren, wie Sie zum Projekt beitragen können.

## Lizenz

Dieses Projekt steht unter der [MIT-Lizenz](LICENSE).
