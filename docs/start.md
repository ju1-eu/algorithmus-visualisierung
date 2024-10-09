# interaktiven Visualisierung

1. **Algorithmus-Implementierung:**
   - Implementierung des Algorithmus in Python
   - Robuste Fehlerbehandlung und Eingabevalidierung
   - Separate Funktionen für die Berechnung und die Schritt-für-Schritt-Verfolgung

2. **Interaktives Dashboard:**
   - Verwendung von Dash für die Erstellung eines webbasierten, interaktiven Dashboards
   - Eingabefelder für Zahlen und ein "Berechnen"-Button
   - Sofortige Aktualisierung der Visualisierung bei Eingabeänderungen

3. **Visualisierung:**
   - Plotly-Graph zur Darstellung der Werte in jedem Schritt des Algorithmus
   - Farbcodierte Linien und Marker
   - Hover-Informationen für detaillierte Werte bei jedem Schritt

4. **Detaillierte Erklärung:**
   - Textuelle Schritt-für-Schritt-Erklärung neben dem Graphen
   - Anzeige des aktuellen Rests und der Logik hinter jedem Schritt
   - Hervorhebung des Endergebnisses

5. **Benutzerfreundlichkeit:**
   - Intuitive Benutzeroberfläche mit klar gekennzeichneten Eingabefeldern
   - Sofortige visuelle und textuelle Rückmeldung nach der Berechnung
   - Deutliche Fehlermeldungen bei ungültigen Eingaben

6. **Responsives Design:**
   - Anpassungsfähiges Layout für verschiedene Bildschirmgrößen
   - Ausgewogene Anordnung von Graph und textueller Erklärung

7. **Code-Struktur und Best Practices:**
   - Modularisierung des Codes (separate Dateien für Algorithmus, Tests und Dashboard)
   - Verwendung von Typenhinweisen und Docstrings für bessere Lesbarkeit
   - Implementierung von Unittests zur Sicherstellung der Korrektheit

8. **Erweiterbarkeit:**
   - Flexibler Code, der einfach um zusätzliche Funktionen erweitert werden kann
   - Möglichkeit, weitere Visualisierungen oder Erklärungen hinzuzufügen

## Unit-Tests für Algorithmen

```bash
(.venv) jan@macbookj $ python main.py       
Dash is running on http://127.0.0.1:8050/

 * Serving Flask app 'framework'
 * Debug mode: on
                                                       # files                                                 main.py                                                run_tests.py
framework.py                   prime_number_algorithm.py      
test_gcd_algorithm.py
gcd_algorithm.py               readme.md                      test_prime_number_algorithm.py
```

Um das System mit den integrierten Tests zu verwenden:

1. Speichern Sie alle Dateien im gleichen Verzeichnis.
2. Um das Dashboard zu starten, führen Sie `python main.py` aus.
3. Um alle Tests auszuführen, verwenden Sie `python main.py --test`.

## Fokus: interaktiven Visualisierung von Algorithmen

1. **Modulares Framework:**
   - Ein zentrales `AlgorithmVisualizationFramework` wurde entwickelt, das als Grundlage für die Integration verschiedener Algorithmen dient.
   - Jeder Algorithmus wird als separates Modul implementiert, was die Erweiterbarkeit und Wartbarkeit erhöht.

2. **Flexibilität der Algorithmen:**
   - Algorithmen (wie GCD und Primzahlen) sind als eigenständige Klassen implementiert.
   - Jede Algorithmusklasse definiert ihre eigene Eingabe-Layout, Berechnungslogik, Visualisierungsdaten und Schritt-für-Schritt-Erklärungen.

3. **Interaktive Benutzeroberfläche:**
   - Das Dashboard ermöglicht die Auswahl verschiedener Algorithmen über ein Dropdown-Menü.
   - Dynamische Anpassung der Eingabefelder je nach ausgewähltem Algorithmus.
   - Sofortige Aktualisierung der Visualisierung und Ergebnisse nach Benutzereingaben.

4. **Visualisierung:**
   - Verwendung von Plotly für die Erstellung interaktiver Graphen.
   - Jeder Algorithmus kann seine eigene spezifische Visualisierungsmethode definieren (z.B. Liniendiagramm für GCD, Heatmap für Primzahlen).
   - Die Visualisierung zeigt den schrittweisen Fortschritt des Algorithmus.

5. **Detaillierte Erklärungen:**
   - Neben der grafischen Darstellung werden textuelle Erklärungen für jeden Schritt des Algorithmus angezeigt.
   - Dies fördert das Verständnis der Funktionsweise des Algorithmus.

6. **Erweiterbarkeit:**
   - Neue Algorithmen können einfach hinzugefügt werden, indem man eine neue Klasse erstellt und sie im Framework registriert.
   - Das Framework ist so konzipiert, dass es verschiedene Arten von Algorithmen und Visualisierungen unterstützen kann.

7. **Testintegration:**
   - Jeder Algorithmus hat seine eigenen Unit-Tests zur Überprüfung der Korrektheit.
   - Ein zentrales Testskript ermöglicht die Ausführung aller Tests mit einem Befehl.
   - Die Hauptanwendung bietet eine Option zum Ausführen von Tests oder zum Starten des Dashboards.

8. **Benutzerfreundlichkeit:**
   - Klare und intuitive Benutzeroberfläche mit Eingabefeldern, einem "Berechnen"-Button und Ergebnisanzeige.
   - Fehlerbehandlung und Validierung von Benutzereingaben zur Verbesserung der Robustheit.

9. **Bildungsaspekt:**
   - Die Kombination aus visueller Darstellung und textueller Erklärung macht das Tool besonders nützlich für Bildungszwecke.
   - Benutzer können den Ablauf verschiedener Algorithmen Schritt für Schritt nachvollziehen.

10. **Technologiestack:**
    - Verwendung von Dash und Plotly für die Erstellung des interaktiven Dashboards.
    - Python als Hauptprogrammiersprache, was eine einfache Integration verschiedener Algorithmen ermöglicht.

11. **Codeorganisation:**
    - Klare Trennung von Belangen: Framework, individuelle Algorithmen, Tests und Hauptanwendung sind in separaten Dateien organisiert.
    - Dies verbessert die Übersichtlichkeit und erleichtert die Zusammenarbeit in Teams.
