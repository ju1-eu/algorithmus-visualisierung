---
title: "CONTRIBUTING"
author: "Jan Unger"
date: "2024-10-10"
---

# Beitrag zum Algorithmus-Visualisierungsprojekt

Durch Ihre Unterstützung können wir das Tool verbessern und es für mehr Benutzer zugänglich machen.

## Inhaltsverzeichnis

- [Beitrag zum Algorithmus-Visualisierungsprojekt](#beitrag-zum-algorithmus-visualisierungsprojekt)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Über das Projekt](#über-das-projekt)
  - [Wie Sie beitragen können](#wie-sie-beitragen-können)
  - [Code-Richtlinien](#code-richtlinien)
  - [Entwicklungsumgebung einrichten](#entwicklungsumgebung-einrichten)
  - [Hinzufügen neuer Algorithmen](#hinzufügen-neuer-algorithmen)
  - [Tests schreiben](#tests-schreiben)
  - [Git](#git)
    - [**1. Initialisieren Sie ein neues Git-Repository**](#1-initialisieren-sie-ein-neues-git-repository)
    - [**2. Fügen Sie Ihre Dateien zum Staging-Bereich hinzu**](#2-fügen-sie-ihre-dateien-zum-staging-bereich-hinzu)
    - [**3. Erstellen Sie den ersten Commit**](#3-erstellen-sie-den-ersten-commit)
    - [**4. Benennen Sie den Hauptbranch in 'main' um (falls erforderlich)**](#4-benennen-sie-den-hauptbranch-in-main-um-falls-erforderlich)
    - [**5. Fügen Sie das Remote-Repository hinzu**](#5-fügen-sie-das-remote-repository-hinzu)
    - [**6. Pushen Sie Ihren Code zu GitHub**](#6-pushen-sie-ihren-code-zu-github)
    - [**Erklärung der Befehle**](#erklärung-der-befehle)
    - [**Zusätzliche Empfehlungen**](#zusätzliche-empfehlungen)
      - [**Erstellen einer `.gitignore`-Datei**](#erstellen-einer-gitignore-datei)
      - [**Aktualisieren des `README.md`**](#aktualisieren-des-readmemd)
      - [**Überprüfen Sie den Status Ihres Repositories**](#überprüfen-sie-den-status-ihres-repositories)
      - [**Weitere Änderungen committen**](#weitere-änderungen-committen)
      - [**Erneutes Pushen**](#erneutes-pushen)
      - [Tagging der Version](#tagging-der-version)
    - [**Hinweise**](#hinweise)
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

## Git

### **1. Initialisieren Sie ein neues Git-Repository**

Navigieren Sie in Ihr Projektverzeichnis und initialisieren Sie ein neues Git-Repository:

```bash
git init
```

### **2. Fügen Sie Ihre Dateien zum Staging-Bereich hinzu**

Fügen Sie die Dateien hinzu, die Sie in Ihrem ersten Commit aufnehmen möchten. Wenn Sie alle Dateien hinzufügen möchten, verwenden Sie:

```bash
git add .
```

Alternativ können Sie spezifische Dateien hinzufügen:

```bash
git add README.md
```

### **3. Erstellen Sie den ersten Commit**

Erstellen Sie einen Commit mit einer aussagekräftigen Nachricht:

```bash
git commit -m "Initialer Commit"
```

### **4. Benennen Sie den Hauptbranch in 'main' um (falls erforderlich)**

Standardmäßig verwendet Git den Branch-Namen `master`. Um ihn in `main` umzubenennen (was heutzutage üblich ist), führen Sie Folgendes aus:

```bash
git branch -M main
```

### **5. Fügen Sie das Remote-Repository hinzu**

Verbinden Sie Ihr lokales Repository mit dem Remote-Repository auf GitHub:

```bash
git remote add origin git@github.com:ju1-eu/algorithmus-visualisierung.git
# oder
#git remote add origin https://github.com/ju1-eu/algorithmus-visualisierung.git
```

**Hinweis:** Stellen Sie sicher, dass die URL korrekt ist und dass Sie die notwendigen Berechtigungen haben (SSH-Schlüssel oder HTTPS-Authentifizierung).

### **6. Pushen Sie Ihren Code zu GitHub**

Übertragen Sie Ihren lokalen `main`-Branch zum Remote-Repository:

```bash
git push -u origin main
```

Die Option `-u` setzt `origin/main` als Upstream für Ihren lokalen `main`-Branch, sodass Sie zukünftig einfach `git push` verwenden können.

---

### **Erklärung der Befehle**

- **`git init`**: Initialisiert ein neues lokales Git-Repository im aktuellen Verzeichnis.

- **`git add .`**: Fügt alle neuen und geänderten Dateien zum Staging-Bereich hinzu.

- **`git commit -m "Nachricht"`**: Erstellt einen neuen Commit mit den Dateien im Staging-Bereich und einer Commit-Nachricht.

- **`git branch -M main`**: Benennt den aktuellen Branch in `main` um.

- **`git remote add origin [URL]`**: Fügt ein Remote-Repository mit dem Namen `origin` hinzu.

- **`git push -u origin main`**: Überträgt den `main`-Branch zum Remote-Repository und setzt `origin/main` als Upstream.

---

### **Zusätzliche Empfehlungen**

#### **Erstellen einer `.gitignore`-Datei**

Es ist üblich, bestimmte Dateien oder Verzeichnisse vom Tracking auszuschließen, z. B. virtuelle Umgebungen oder temporäre Dateien.

Erstellen Sie eine `.gitignore`-Datei:

```bash
echo ".venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
```

Fügen Sie die `.gitignore`-Datei hinzu und committen Sie sie:

```bash
git add .gitignore
git commit -m "Füge .gitignore hinzu"
```

#### **Aktualisieren des `README.md`**

Stellen Sie sicher, dass Ihr `README.md` eine vollständige und aktuelle Beschreibung Ihres Projekts enthält.

#### **Überprüfen Sie den Status Ihres Repositories**

Vor dem Pushen können Sie den Status überprüfen:

```bash
git status
```

#### **Weitere Änderungen committen**

Wenn Sie weitere Dateien hinzugefügt oder geändert haben:

```bash
git add .
git commit -m "Beschreibe deine Änderungen"
```

#### **Erneutes Pushen**

Nachdem Sie weitere Commits erstellt haben, können Sie diese mit folgendem Befehl pushen:

```bash
git push
```

#### Tagging der Version

```bash
git tag -a v1.0 -m "Version 1.0: fehlerfreie Version mit drei Algorithmen"
git push origin v1.0
```

### **Hinweise**

- **Authentifizierung**: Stellen Sie sicher, dass Sie die notwendigen Anmeldedaten oder SSH-Schlüssel eingerichtet haben, um auf Ihr GitHub-Konto zuzugreifen.

- **GitHub-Repository erstellen**: Falls Sie das Remote-Repository noch nicht auf GitHub erstellt haben, tun Sie dies zuerst. Navigieren Sie zu GitHub, klicken Sie auf **"New repository"** und folgen Sie den Anweisungen.

## Pull-Request erstellen

1. **Branch erstellen:**

   ```bash
   git checkout -b feature/neuer-algorithmus
   ```

2. **Änderungen vornehmen und committen:**

   ```bash
   git add .
   git commit -m "Neuen Algorithmus hinzugefügt"
   ```

3. **Branch pushen:**

   ```bash
   git push origin feature/neuer-algorithmus
   ```

4. **Pull-Request erstellen:**

   - Navigieren Sie zu Ihrem Fork auf GitHub.
   - Klicken Sie auf **Compare & pull request**.
   - Beschreiben Sie Ihre Änderungen ausführlich.