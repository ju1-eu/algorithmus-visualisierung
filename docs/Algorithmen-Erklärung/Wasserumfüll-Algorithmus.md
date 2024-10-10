---
title: "Wasserumfüll-Algorithmus"
author: "Jan Unger"
date: "2024-10-10"
---

# Wasserumfüll-Algorithmus: Analyse und Implementierung

## Einleitung

Der Wasserumfüll-Algorithmus modelliert einen iterativen Prozess des Wassertransfers zwischen zwei Eimern. Dieses scheinbar einfache System birgt überraschende Komplexität und findet Anwendungen in verschiedenen wissenschaftlichen und praktischen Bereichen. In dieser Analyse untersuchen wir die mathematischen Grundlagen, die Implementierung und die vielfältigen Anwendungsmöglichkeiten dieses Algorithmus.

## Mathematische Grundlagen

Der Prozess lässt sich mathematisch wie folgt beschreiben:

Sei $x_n$ die Wassermenge im ersten Eimer und $y_n$ die Wassermenge im zweiten Eimer nach dem $n$-ten Umfüllvorgang.

1. Umfüllen von Eimer 1 zu Eimer 2:
   $$ x_{n+1/2} = x_n - ax_n = (1-a)x_n $$
   $$ y_{n+1/2} = y_n + ax_n $$

2. Umfüllen von Eimer 2 zu Eimer 1:
   $$ x_{n+1} = x_{n+1/2} + by_{n+1/2} = (1-a)x_n + b(y_n + ax_n) $$
   $$ y_{n+1} = y_{n+1/2} - by_{n+1/2} = (1-b)(y_n + ax_n) $$

Dies lässt sich als Matrixgleichung darstellen:

$$ \begin{pmatrix} x_{n+1} \\ y_{n+1} \end{pmatrix} = \begin{pmatrix} 1-a+ab & b \\ a(1-b) & 1-b \end{pmatrix} \begin{pmatrix} x_n \\ y_n \end{pmatrix} $$

Für das Langzeitverhalten ist der Eigenwert $\lambda = 1$ der Übergangsmatrix entscheidend, da er die stationäre Verteilung bestimmt. Dies bedeutet, dass es einen Zustand gibt, der sich durch weiteres Umfüllen nicht mehr ändert, was einem Gleichgewicht entspricht.

## Erklärung des Codes und Algorithmus

Der Algorithmus implementiert den oben beschriebenen mathematischen Prozess:

1. **Initialisierung**: Setzt die Startwerte für beide Eimer.
2. **Hauptschleife**: Führt $n$ Umfüllvorgänge durch.
   a. Berechnet den Transfer von Eimer 1 zu Eimer 2.
   b. Aktualisiert die Wasserstände.
   c. Berechnet den Transfer von Eimer 2 zu Eimer 1.
   d. Aktualisiert die Wasserstände erneut.
   e. Speichert den aktuellen Zustand.
3. **Ergebnisanalyse**: Berechnet die finale Wasserverteilung und analysiert das Langzeitverhalten.

Hier ein Pseudocode zur Veranschaulichung:

```python
def water_transfer_algorithm(x, y, a, b, n):
    for i in range(n):
        # Transfer von Eimer 1 zu Eimer 2
        transfer = a * x
        x -= transfer
        y += transfer
        
        # Transfer von Eimer 2 zu Eimer 1
        transfer = b * y
        y -= transfer
        x += transfer
        
        # Speichere aktuellen Zustand
        save_state(x, y)
    
    analyze_long_term_behavior(x, y)
    return x, y
```

Wichtige Aspekte der Implementierung:

- Verwendung von Fließkommazahlen für präzise Berechnungen.
- Rundung der Ausgabewerte auf zwei Dezimalstellen für bessere Lesbarkeit.
- Implementierung einer Methode zur Analyse des Langzeitverhaltens.

## Struktogramm des Algorithmus

```
┌─────────────────────────────────────────────────┐
│           Initialisiere Variablen               │
│      (x, y, a, b, n, steps, result)             │
└───────────────────────┬─────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────┐
│               Für i von 0 bis n-1               │
│   ┌─────────────────────────────────────────┐   │
│   │    Berechne Transfer von Eimer 1 zu 2   │   │
│   └─────────────────────┬───────────────────┘   │
│                         │                       │
│   ┌─────────────────────▼───────────────────┐   │
│   │       Aktualisiere Wasserstände         │   │
│   └─────────────────────┬───────────────────┘   │
│                         │                       │
│   ┌─────────────────────▼───────────────────┐   │
│   │    Berechne Transfer von Eimer 2 zu 1   │   │
│   └─────────────────────┬───────────────────┘   │
│                         │                       │
│   ┌─────────────────────▼───────────────────┐   │
│   │       Aktualisiere Wasserstände         │   │
│   └─────────────────────┬───────────────────┘   │
│                         │                       │
│   ┌─────────────────────▼───────────────────┐   │
│   │      Speichere aktuellen Zustand        │   │
│   └─────────────────────────────────────────┘   │
└───────────────────────┬─────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────┐
│         Analysiere Langzeitverhalten            │
└─────────────────────────────────────────────────┘
```

Legende:

- Rechtecke: Prozessschritte
- Rauten: Entscheidungen (hier nicht verwendet)
- Pfeile: Flussrichtung des Algorithmus

## Anwendungen

Der Wasserumfüll-Algorithmus findet in verschiedenen Bereichen Anwendung:

1. **Flüssigkeitsmanagement**: 
   - Modellierung von Mischprozessen in der chemischen Industrie.
   - Beispiel: Optimierung von Batch-Reaktoren in der Pharmaproduktion.

2. **Ökonomie**: 
   - Simulation von Geldflüssen zwischen zwei Wirtschaftssektoren.
   - Anwendung: Analyse von Investitionsströmen zwischen Industrie und Dienstleistungssektor.

3. **Ökologie**: 
   - Modellierung von Populationsdynamiken zwischen zwei Habitaten.
   - Beispiel: Untersuchung der Migration von Arten zwischen zwei benachbarten Ökosystemen.

4. **Physik**: 
   - Simulation von Wärmeaustauschprozessen zwischen zwei Systemen.
   - Anwendung: Modellierung der Temperaturänderung in verbundenen Wärmereservoiren.

Herausforderungen bei der Anwendung:

- Berücksichtigung von Verlusten oder externen Zuflüssen im realen System.
- Anpassung des Modells an nicht-lineare Transferraten in komplexeren Systemen.

## Beispielberechnungen und Visualisierung

Betrachten wir folgendes Beispiel:

- $x = 100$ Liter (Startwert Eimer 1)
- $y = 50$ Liter (Startwert Eimer 2)
- $a = 30\%$ (Transfer von Eimer 1 zu 2)
- $b = 20\%$ (Transfer von Eimer 2 zu 1)
- $n = 5$ Zyklen

| Zyklus | Eimer 1 | Eimer 2 |
| ------ | ------- | ------- |
| Start  | 100.00  | 50.00   |
| 1      | 80.00   | 70.00   |
| 2      | 70.00   | 80.00   |
| 3      | 65.00   | 85.00   |
| 4      | 62.50   | 87.50   |
| 5      | 61.25   | 88.75   |

Grafische Darstellung der Entwicklung:

```
Wasserstand (L)
    ^
100 |x
    |  x
 80 |    x
    |      x  x  x
 60 |          y  y  y
    |      y
 40 |  y
    |y
 20 |
    |
  0 +--+--+--+--+--+--+
    0  1  2  3  4  5  Zyklus
    
x: Eimer 1, y: Eimer 2
```

Langzeitanalyse: Bei Fortführung des Prozesses würde sich das System einem Gleichgewichtszustand annähern. In diesem Beispiel konvergiert das System gegen eine Verteilung von etwa 60% in Eimer 2 und 40% in Eimer 1.

## MindMap zum Code

```
                  ┌───────────────┐
                  │WaterTransfer  │
                  │  Algorithm    │
                  └───────┬───────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
 ┌──────▼──────┐   ┌──────▼──────┐   ┌──────▼──────┐
 │ get_inputs  │   │    run      │   │ get_result  │
 └─────────────┘   └──────┬──────┘   └─────────────┘
                          │
              ┌───────────┴───────────┐
              │                       │
      ┌───────▼───────┐       ┌───────▼───────┐
      │ Initialisierung│       │ Hauptschleife │
      └───────────────┘       └───────┬───────┘
                                      │
                          ┌───────────┴───────────┐
                          │                       │
                  ┌───────▼───────┐       ┌───────▼───────┐
                  │Transfer 1 → 2 │       │Transfer 2 → 1 │
                  └───────────────┘       └───────────────┘
```

Erklärung der Beziehungen:

- `get_inputs`: Erfasst die Startparameter (x, y, a, b, n)
- `run`: Hauptfunktion, die den Algorithmus ausführt
- `get_result`: Gibt das Endergebnis und die Analyse zurück
- Die Hauptschleife führt abwechselnd die Transfers zwischen den Eimern durch

## Effizienz und Optimierung

Der Algorithmus hat eine Zeitkomplexität von O(n), wobei n die Anzahl der Zyklen ist. Für die meisten praktischen Anwendungen ist dies ausreichend effizient. Mögliche Optimierungen:

1. Frühzeitiger Abbruch bei Erreichen des Gleichgewichtszustands.
2. Verwendung analytischer Methoden zur direkten Berechnung des Gleichgewichtszustands für große n.

## Skalierbarkeit

Der Algorithmus lässt sich auf Systeme mit mehr als zwei Eimern erweitern:

- Die Komplexität steigt von O(n) auf O(m²n), wobei m die Anzahl der Eimer ist.
- Die Matrixdarstellung wird zu einer m×m-Matrix erweitert.
- Die Analyse des Langzeitverhaltens wird komplexer und kann multiple Gleichgewichtszustände aufweisen.

## Fazit

Der Wasserumfüll-Algorithmus demonstriert, wie ein einfaches Modell komplexe Systeme abbilden kann. Seine Anwendbarkeit in verschiedenen Disziplinen unterstreicht die Bedeutung mathematischer Modellierung in der Wissenschaft und Technik. 