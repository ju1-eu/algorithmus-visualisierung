# CONTRIBUTING.md

Beitrag zum Algorithmus-Visualisierungsprojekt

Durch Ihre Unterstützung können wir das Tool verbessern und es für mehr Benutzer zugänglich machen.

## Inhaltsverzeichnis

- [CONTRIBUTING.md](#contributingmd)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Über das Projekt](#über-das-projekt)
  - [Wie Sie beitragen können](#wie-sie-beitragen-können)
  - [Code-Richtlinien](#code-richtlinien)
  - [Entwicklungsumgebung einrichten](#entwicklungsumgebung-einrichten)
  - [Hinzufügen neuer Algorithmen](#hinzufügen-neuer-algorithmen)
  - [Tests schreiben](#tests-schreiben)
  - [Pull-Request erstellen](#pull-request-erstellen)

## Über das Projekt

Das Algorithmus-Visualisierungsprojekt ist ein Framework zur interaktiven Darstellung verschiedener Algorithmen. Es ermöglicht Benutzern, die Schritte eines Algorithmus visuell zu verfolgen und zu verstehen.

## Wie Sie beitragen können

- **Fehler melden:** Öffnen Sie ein Issue und beschreiben Sie das Problem detailliert.
- **Funktionen vorschlagen:** Wenn Sie eine Idee für eine neue Funktion haben, teilen Sie sie uns mit.
- **Code beitragen:** Sie können neue Algorithmen hinzufügen oder bestehende verbessern.

## Code-Richtlinien

Bitte halten Sie sich an die folgenden Richtlinien:

- **PEP 8:** Folgen Sie dem offiziellen Style Guide für Python-Code.
- **Docstrings:** Dokumentieren Sie Ihre Funktionen und Klassen mit aussagekräftigen Docstrings.
- **Kommentare:** Verwenden Sie Kommentare, um komplexen Code zu erklären.
- **Codeformatierung:** Nutzen Sie Tools wie **Black** und **isort** zur automatischen Formatierung.
- **Fehlerbehandlung:** Implementieren Sie eine konsistente Fehlerbehandlung und dokumentieren Sie mögliche Ausnahmen in den Docstrings.

## Entwicklungsumgebung einrichten

1. **Repository forken und klonen:**

   ```bash
   git clone https://github.com/IhrBenutzername/algorithmus-visualisierung.git
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
   ```

4. **Entwicklungswerkzeuge installieren (optional):**

   ```bash
   pip install black isort pylint
   ```

## Hinzufügen neuer Algorithmen

Um einen neuen Algorithmus zum Framework hinzuzufügen, folgen Sie diesen Schritten:

1. **Neue Algorithmusklasse erstellen:**

   - Legen Sie eine neue Datei im Verzeichnis `algorithms/` an, z. B. `example_algorithm.py`.
   - Importieren Sie `BaseAlgorithm`:

     ```python
     from algorithms.base_algorithm import BaseAlgorithm
     ```

2. **Von BaseAlgorithm erben:**

   ```python
   class ExampleAlgorithm(BaseAlgorithm):
       # Implementierung folgt...
   ```

3. **Erforderliche Methoden implementieren:**

   - `name` (Property): Gibt den Namen des Algorithmus zurück.
   - `run(self, *args, **kwargs)`: Führt den Algorithmus aus.
   - `get_visualization_data(self, step=None)`: Bereitet die Daten für die Visualisierung vor.
   - `get_result(self)`: Gibt das Ergebnis des Algorithmus zurück.
   - `get_step_details(self, step=None)`: Gibt Details zum aktuellen Schritt zurück.

4. **Beispiel:**

   ```python
   from algorithms.base_algorithm import BaseAlgorithm

   class ExampleAlgorithm(BaseAlgorithm):
       def __init__(self):
           self._name = Beispielalgorithmus
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
           return fDas Ergebnis ist {self.result}

       def get_step_details(self, step=None):
           # Details zum aktuellen Schritt
           pass
   ```

5. **Tests schreiben:**

   - Erstellen Sie ein neues Testmodul im Verzeichnis `tests/`, z. B. `test_example_algorithm.py`.
   - Verwenden Sie das `unittest`-Modul, um Ihre Tests zu schreiben.

   ```python
   import unittest
   from algorithms.example_algorithm import ExampleAlgorithm

   class TestExampleAlgorithm(unittest.TestCase):
       def setUp(self):
           self.algorithm = ExampleAlgorithm()

       def test_run(self):
           # Testen Sie die Run-Methode
           pass

       def test_get_result(self):
           # Testen Sie die Ergebnisrückgabe
           pass

   if __name__ == '__main__':
       unittest.main()
   ```

6. **Algorithmus registrieren:**

   - Fügen Sie Ihren Algorithmus in `main.py` hinzu:

     ```python
     from algorithms.example_algorithm import ExampleAlgorithm

     # ...

     framework.register_algorithm(ExampleAlgorithm())
     ```

7. **Eingabefelder hinzufügen:**

   - Wenn Ihr Algorithmus spezielle Eingabefelder benötigt, passen Sie `framework.py` an.
   - Fügen Sie die notwendigen Eingabefelder im Layout hinzu.
   - Aktualisieren Sie die Callback-Funktionen, um die neuen Eingaben zu verarbeiten.

8. **Dokumentation aktualisieren:**

   - Stellen Sie sicher, dass Sie Ihre Klasse und Methoden mit Docstrings versehen.
   - Dokumentieren Sie mögliche Ausnahmen und Fehlerbehandlungen.

## Tests schreiben

- **Abdeckung sicherstellen:** Stellen Sie sicher, dass alle Funktionen Ihres Algorithmus durch Tests abgedeckt sind.
- **Fehlerfälle testen:** Schreiben Sie Tests für gültige und ungültige Eingaben.
- **Testkonventionen beachten:** Testmethoden sollten mit `test_` beginnen.

## Pull-Request erstellen

1. **Branch erstellen:**

   ```bash
   git checkout -b feature/neuer-algorithmus
   ```

2. **Änderungen vornehmen und committen:**

   ```bash
   git add .
   git commit -m Neuen Algorithmus hinzugefügt
   ```

3. **Branch pushen:**

   ```bash
   git push origin feature/neuer-algorithmus
   ```

4. **Pull-Request erstellen:**

   - Navigieren Sie zu Ihrem Fork auf GitHub.
   - Klicken Sie auf **Compare & pull request**.
   - Beschreiben Sie Ihre Änderungen ausführlich.