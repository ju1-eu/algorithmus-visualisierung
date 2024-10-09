# Do-To-Liste

1. **Metadaten hinzufügen:** Algorithmusklassen mit Informationen über Eingaben erweitern.
2. **Layout anpassen:** Funktionen zur dynamischen Generierung von Eingabefeldern basierend auf Metadaten implementieren.
3. **Callback-Logik überarbeiten:** Generische Callbacks erstellen, die mit der Basisklasse interagieren.
4. **Fehlerbehandlung optimieren:** Validierungen und Fehlermeldungen innerhalb der Algorithmen standardisieren.
5. **Dokumentation aktualisieren:** Klarheit über die Erweiterungsmöglichkeiten schaffen und neue Entwickler unterstützen.

## Überprüfung der Dokumentation

Nachdem wir den neuen Algorithmus **"Zinseszinsberechnung"** zu Ihrem Framework hinzugefügt haben, bietet sich die Gelegenheit, die Dokumentation zu überprüfen und sicherzustellen, dass die Anweisungen zum Hinzufügen neuer Algorithmen klar und vollständig sind. Hier sind die wichtigsten Erkenntnisse:

1. **Klarheit der Anweisungen in der Dokumentation**

   - Die Dokumentation in **README.md** und **CONTRIBUTING.md** bietet eine Schritt-für-Schritt-Anleitung zum Hinzufügen neuer Algorithmen.
   - Die Anweisungen sind grundsätzlich klar und verständlich, insbesondere hinsichtlich der Implementierung der erforderlichen Methoden und der Vererbung von der abstrakten Basisklasse `BaseAlgorithm`.

2. **Vollständigkeit der Schritte**

   - Die Dokumentation deckt die meisten notwendigen Schritte ab, einschließlich:
     - **Erstellen einer neuen Algorithmusklasse** im Verzeichnis `algorithms/`.
     - **Implementieren der abstrakten Methoden** aus `BaseAlgorithm`.
     - **Registrieren des Algorithmus** in `main.py`.
     - **Anpassen der Eingabefelder** und **Callback-Funktionen** in `framework.py`.
     - **Schreiben von Tests** für den neuen Algorithmus.

3. **Identifizierte Verbesserungen**

   - **Anpassung von `run_tests.py` nicht erwähnt:**
     - Die Dokumentation vergisst zu erwähnen, dass beim Hinzufügen eines neuen Algorithmus auch die Tests in `run_tests.py` hinzugefügt werden müssen.
     - **Lösung:** In **CONTRIBUTING.md** sollte ein zusätzlicher Schritt eingefügt werden, der darauf hinweist, dass die neuen Tests importiert und der Test-Suite hinzugefügt werden müssen.
   - **Detailliertere Anleitung für die Anpassung von `framework.py`:**
     - Die Schritte zur Anpassung der Achsenbeschriftungen und der Visualisierung könnten genauer beschrieben werden.
     - **Vorschlag:** Beispiele für die dynamische Anpassung der Achsenbeschriftungen basierend auf dem ausgewählten Algorithmus hinzufügen.
   - **Dokumentation der Fehler- und Ausnahmebehandlung:**
     - Es sollte betont werden, dass neue Algorithmen eine konsistente Fehlerbehandlung implementieren und mögliche Ausnahmen in den Docstrings dokumentieren sollten.

4. **Bestätigung der Erweiterbarkeit des Frameworks**

   - Das erfolgreiche Hinzufügen des neuen Algorithmus zeigt, dass das Framework tatsächlich erweiterbar ist.
   - Die Verwendung der abstrakten Basisklasse `BaseAlgorithm` erleichtert die Integration und stellt sicher, dass alle Algorithmen eine einheitliche Schnittstelle bieten.

5. **Praxisbezogene Erkenntnisse**

   - **Eingabefelder anpassen:** Die Dokumentation sollte klarstellen, dass beim Hinzufügen neuer Algorithmen die Eingabefelder im Layout und die zugehörigen Callback-Funktionen angepasst werden müssen.
   - **Visualisierung anpassen:** Hinweise zur Anpassung der Visualisierung, einschließlich der Achsenbeschriftungen und Darstellung der Daten, wären hilfreich.
   - **Tests schreiben und integrieren:** Neben dem Schreiben von Tests sollte auch die Integration dieser Tests in das zentrale Testskript (`run_tests.py`) erwähnt werden.

6. **Empfohlene Aktualisierungen der Dokumentation**

   - **CONTRIBUTING.md:**
     - **Schritt zum Hinzufügen der Tests zu `run_tests.py` ergänzen.**
     - **Hinweise zur Fehler- und Ausnahmebehandlung erweitern.**
   - **README.md:**
     - **Beispiele aktualisieren**, um den neuen Algorithmus einzuschließen.
     - **Anweisungen zum Starten der Anwendung** und Ausführen der Tests überprüfen.
   - **ARCHITECTURE.md:**
     - **Neuen Algorithmus in der Modulübersicht hinzufügen.**
     - **Datenflussdiagramme aktualisieren**, um den neuen Algorithmus zu berücksichtigen.

**Fazit**

Die Dokumentation ist insgesamt gut strukturiert und erleichtert das Hinzufügen neuer Algorithmen. Durch die oben genannten Verbesserungen kann sie noch vollständiger und hilfreicher gestaltet werden. Insbesondere das Hinzufügen detaillierterer Anweisungen und das Berücksichtigen aller notwendigen Schritte tragen dazu bei, zukünftigen Mitwirkenden den Prozess zu erleichtern.

**Nächste Schritte:**

- **Dokumentation aktualisieren:** Nehmen Sie die vorgeschlagenen Ergänzungen und Verbesserungen in Ihre Dokumentation auf.
- **Feedback einholen:** Bitten Sie andere Entwickler oder Mitwirkende, die aktualisierte Dokumentation zu überprüfen und weiteres Feedback zu geben.
- **Kontinuierliche Verbesserung:** Halten Sie die Dokumentation aktuell, insbesondere wenn sich das Framework weiterentwickelt oder neue Funktionen hinzugefügt werden.
