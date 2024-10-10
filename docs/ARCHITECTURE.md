---
title: "ARCHITECTURE"
author: "Jan Unger"
date: "2024-10-10"
---

# ARCHITECTURE.md

## Inhaltsverzeichnis

- [ARCHITECTURE.md](#architecturemd)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Übersicht über die Module](#übersicht-über-die-module)
    - [1. `main.py`](#1-mainpy)
    - [2. `framework.py`](#2-frameworkpy)
    - [3. `algorithms/`](#3-algorithms)
    - [4. `tests/`](#4-tests)
    - [5. `run_tests.py`](#5-run_testspy)
  - [Interaktion zwischen Modulen](#interaktion-zwischen-modulen)
  - [Datenfluss](#datenfluss)
  - [Verwendung der abstrakten Basisklasse](#verwendung-der-abstrakten-basisklasse)
  - [Fehler- und Ausnahmebehandlung](#fehler--und-ausnahmebehandlung)

## Übersicht über die Module

### 1. `main.py`

- **Funktion:** Startpunkt der Anwendung. Registriert die Algorithmen und startet das Framework.
- **Abhängigkeiten:** Importiert das Framework und die Algorithmen.

### 2. `framework.py`

- **Funktion:** Kern des Dash-Frameworks. Definiert das Layout, die Callbacks und die Hauptlogik.
- **Abhängigkeiten:** Importiert Dash-Komponenten und die Algorithmen.

### 3. `algorithms/`

- **Funktion:** Enthält alle Algorithmus-Klassen.
- **Struktur:**
  - `base_algorithm.py`: Definiert die abstrakte Basisklasse `BaseAlgorithm`.
  - `ggt_algorithm.py`: Implementiert den GGT-Algorithmus.
  - `prime_number_algorithm.py`: Implementiert den Primzahlen-Algorithmus.
  - Weitere Algorithmen können hier hinzugefügt werden.

### 4. `tests/`

- **Funktion:** Enthält alle Unit-Tests für die Algorithmen.
- **Struktur:**
  - `test_ggt_algorithm.py`: Tests für den GGT-Algorithmus.
  - `test_prime_number_algorithm.py`: Tests für den Primzahlen-Algorithmus.

### 5. `run_tests.py`

- **Funktion:** Skript zum Ausführen aller Tests.

## Interaktion zwischen Modulen

- **`main.py`:** Initialisiert das Framework und registriert die Algorithmen.
- **`framework.py`:** Verwendet die Algorithmen zur Berechnung und Visualisierung.
- **`algorithms/`:** Stellt die Algorithmen bereit, die von `framework.py` genutzt werden.
- **`tests/`:** Testet die Algorithmen unabhängig vom Framework.
- **Kommunikation:** Erfolgt über Objektinstanzen und Methodenaufrufe.

## Datenfluss

1. **Benutzerinteraktion:**

   - Der Benutzer wählt einen Algorithmus und gibt Eingaben über die Benutzeroberfläche ein.

2. **Framework-Verarbeitung:**

   - `framework.py` empfängt die Eingaben und leitet sie an den entsprechenden Algorithmus weiter.

3. **Algorithmusausführung:**

   - Der ausgewählte Algorithmus führt die Berechnungen durch und speichert die Schritte.

4. **Visualisierung:**

   - Die Ergebnisse und Schritte werden vom Framework abgefragt und in der Benutzeroberfläche dargestellt.

## Verwendung der abstrakten Basisklasse

- **`BaseAlgorithm`:** Definiert die Schnittstelle für alle Algorithmen.
- **Erweiterbarkeit:**
  - Neue Algorithmen erben von `BaseAlgorithm` und implementieren die erforderlichen Methoden.
  - Das Framework interagiert über die Schnittstelle mit den Algorithmen, ohne deren interne Implementierung zu kennen.

## Fehler- und Ausnahmebehandlung

- **In Algorithmen:**
  - Eingabedaten werden validiert.
  - Es werden aussagekräftige Ausnahmen geworfen (`ValueError`, `TypeError`).
  - Ausnahmen sind in den Docstrings dokumentiert.

- **Im Framework:**
  - Fängt spezifische Ausnahmen ab und zeigt dem Benutzer hilfreiche Fehlermeldungen.
  - Allgemeine Ausnahmen werden protokolliert.
  - Die Anwendung bleibt stabil und informiert den Benutzer über Fehler.

