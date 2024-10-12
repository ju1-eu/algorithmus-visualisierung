---
title: "kapitel_5"
author: "Jan Unger"
date: "2024-10-12"
---

# Aufgabenstellungen

## Kapitel 5

### A 5.1
Wir definieren einen neuen logischen Operator `nand` durch folgende Wahrheitstafel:
```
| A   | B   | A nand B |
| --- | --- | -------- |
| 0   | 0   | 1        |
| 0   | 1   | 1        |
| 1   | 0   | 1        |
| 1   | 1   | 0        |
```
Zeigen Sie, dass man beliebige boolesche Funktionen unter alleiniger Verwendung des `nand`-Operators darstellen kann!  
Hinweis: Es reicht, wenn Sie zeigen, dass man `nicht`, `und` und `oder` darstellen kann.

### A 5.2
Erstellen Sie ein Programm, das Wahrheitstafeln für die folgenden booleschen Ausdrücke auf dem Bildschirm ausgibt:
- `A ∧ (B ∨ C)`
- `(A ∧ B) ⇒ (C ∨ D)`
- `(A ∨ B) ∧ (C ∧ D)`
- `(A ⇒ B) ∧ (C ⇒ D)`

Beachten Sie, dass Sie eine Implikation `X ⇒ Y` durch `¬X ∨ Y` ausdrücken können!

### A 5.3
„Aussagenlogische Operatoren“ 

- Assoziativgesetz
- Kommutativgesetz
- Distributivgesetz
- De Morgansches Gesetz

### A 5.4
Die Schaltung aus Aufgabe 5.2 wird dahingehend abgeändert, dass zwei Schalter miteinander gekoppelt werden und eine neue Leitung gelegt wird.  
Finden Sie eine möglichst einfache boolesche Funktion für diese Schaltung, und erstellen Sie ein Programm, das alle Schalterstellungen ausgibt, in denen die Lampe leuchtet!

### A 5.5
Familie Müller ist zu einer Geburtstagsfeier eingeladen. Leider können sich die Familienmitglieder (Anton, Berta, Claus und Doris) nicht einigen, wer hingeht und wer nicht.  
Helfen Sie Familie Müller, indem Sie ein Programm erstellen, das alle Konstellationen ermittelt, in denen Familie Müller zur Feier gehen könnte. Die Regeln sind:

1. Mindestens ein Familienmitglied geht zu der Feier.
2. Anton geht auf keinen Fall zusammen mit Doris.
3. Wenn Berta geht, dann geht Claus mit.
4. Wenn Anton und Claus gehen, dann bleibt Berta zu Hause.
5. Wenn Anton zu Hause bleibt, dann geht entweder Doris oder Claus.

### A 5.6
Bankdirektor Schulze hat den Tresor seiner Bank durch ein elektronisches Schloss sichern lassen. Dieses Schloss kann über neun Kippschalter geöffnet werden, wenn man diese in die richtige Stellung (unten oder oben) bringt.  
Schreiben Sie ein Programm, das den Tresor „knackt“.
