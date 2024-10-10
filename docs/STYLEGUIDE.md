---
title: "STYLEGUIDE"
author: "Jan Unger"
date: "2024-10-10"
---

# STYLEGUIDE.md

## Inhaltsverzeichnis

- [STYLEGUIDE.md](#styleguidemd)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Einleitung](#einleitung)
  - [Allgemeine Prinzipien](#allgemeine-prinzipien)
  - [Codeformatierung](#codeformatierung)
  - [Benennungskonventionen](#benennungskonventionen)
  - [Kommentare und Docstrings](#kommentare-und-docstrings)
  - [Code-Struktur](#code-struktur)
  - [Fehler- und Ausnahmebehandlung](#fehler--und-ausnahmebehandlung)
  - [Testen](#testen)
  - [Verwendung von Tools](#verwendung-von-tools)
  - [Git-Konventionen](#git-konventionen)
  - [Weiterführende Ressourcen](#weiterführende-ressourcen)

## Einleitung

Dieser Style-Guide legt die Coding-Standards für das **Algorithmus-Visualisierungsprojekt** fest. Alle Mitwirkenden sollten diese Richtlinien befolgen, um einen konsistenten und hochwertigen Code zu gewährleisten.

## Allgemeine Prinzipien

- **Lesbarkeit vor Cleverness:** Der Code sollte leicht verständlich sein.
- **Konsistenz:** Halten Sie sich an die festgelegten Konventionen.
- **Explizit ist besser als implizit:** Schreiben Sie klaren und eindeutigen Code.
- **Einfache Fehlerbehandlung:** Behandeln Sie Fehlerfälle angemessen und vermeiden Sie unnötige Komplexität.

## Codeformatierung

- **Einrückung:** Verwenden Sie 4 Leerzeichen pro Einrückungsebene.
- **Zeilenlänge:** Maximal 79 Zeichen pro Zeile.
- **Leerzeilen:** Verwenden Sie Leerzeilen, um logische Abschnitte zu trennen.
- **Imports:** Platzieren Sie alle Imports am Anfang der Datei und gruppieren Sie sie.

## Benennungskonventionen

- **Variablen und Funktionen:** Verwenden Sie `lowercase_with_underscores`.
- **Klassen:** Verwenden Sie `CapWords`.
- **Konstanten:** Verwenden Sie `UPPERCASE_WITH_UNDERSCORES`.

## Kommentare und Docstrings

- **Kommentare:** Verwenden Sie aussagekräftige Kommentare, die den Zweck des Codes erklären.
- **Docstrings:** Verwenden Sie Docstrings für alle Module, Klassen und öffentlichen Funktionen oder Methoden.

## Code-Struktur

- **Modul- und Paketstruktur:** Organisieren Sie den Code in logisch getrennten Modulen und Paketen.
- **Klassen und Funktionen:** Platzieren Sie verwandte Klassen und Funktionen im selben Modul.

## Fehler- und Ausnahmebehandlung

- **Spezifische Ausnahmen:** Verwenden Sie spezifische Ausnahmearten.
- **Dokumentation:** Dokumentieren Sie mögliche Ausnahmen in den Docstrings.
- **Keine nackten `except:`-Blöcke:** Geben Sie immer die Ausnahmeart an.

## Testen

- **Unit-Tests:** Schreiben Sie Tests für alle neuen Funktionen und Klassen.
- **Testkonventionen:** Testmethoden sollten mit `test_` beginnen.

## Verwendung von Tools

- **Codeformatierung:** Verwenden Sie `Black` zur automatischen Formatierung.
- **Code-Analyse:** Verwenden Sie `Flake8` oder `Pylint`, um den Code zu überprüfen.

## Git-Konventionen

- **Commit-Nachrichten:** Verwenden Sie klare und prägnante Nachrichten.
- **Branch-Namen:** Verwenden Sie beschreibende Namen in Kleinbuchstaben mit Bindestrichen.

## Weiterführende Ressourcen

- [PEP 8 – Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [PEP 257 – Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
- [Black – The uncompromising code formatter](https://black.readthedocs.io/en/stable/)
- [Pylint – Code Analysis for Python](https://www.pylint.org/)
