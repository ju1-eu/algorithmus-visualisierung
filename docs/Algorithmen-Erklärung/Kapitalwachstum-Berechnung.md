---
title: "Kapitalwachstum-Berechnung"
author: "Jan Unger"
date: "2024-10-10"
---

# Kapitalwachstum-Berechnung: Von der Theorie zur Praxis

## Einleitung

In der Finanzwelt spielt die Berechnung des Kapitalwachstums eine zentrale Rolle. Sie hilft bei der langfristigen Finanzplanung, sei es für Investitionen, Altersvorsorge oder zur Einschätzung von Kreditkosten. Dieser Text erklärt die mathematischen Grundlagen, den Algorithmus und die praktische Anwendung der Kapitalwachstums-Berechnung.

## Mathematische Grundlagen

Die Berechnung basiert auf dem Prinzip des Zinseszinses. Dabei werden nicht nur auf das ursprüngliche Kapital Zinsen berechnet, sondern in den Folgejahren auch auf die bereits gutgeschriebenen Zinsen. Dies führt zu einem exponentiellen Wachstum, das durch die Zinseszinsformel beschrieben wird:

$$A = P \cdot (1 + r)^t$$

Wobei:

- $A$: Endkapital
- $P$: Anfangskapital
- $r$: Zinssatz (als Dezimalzahl, z.B. 5% = 0.05)
- $t$: Zeit in Jahren

## Erklärung des Codes und Algorithmus

Der Algorithmus setzt die mathematische Formel in einen iterativen Prozess um:

1. Initialisierung: $\text{current_capital} = P$
2. Für jedes Jahr $t$:
   $$\text{current_capital} = \text{current_capital} \cdot (1 + r)$$
3. Wiederholung von Schritt 2, bis $\text{current_capital} \geq \text{target\_sum}$

## Struktogramm des Algorithmus

```
+----------------------------------+
|             Start                |
+----------------------------------+
                |
                v
+----------------------------------+
|        Initialisierung           |
| years = 0                        |
| current_capital = initial_capital|
+----------------------------------+
                |
                v
+----------------------------------+
|   current_capital < target_sum?  |
+----------------------------------+
        |               |
       Ja              Nein
        |               |
        v               v
+----------------------------------+
| Berechne neues Kapital           |
| current_capital *= (1 + r)       |
| Runde current_capital auf 2      |
| Dezimalstellen                   |
+----------------------------------+
        |
        v
+----------------------------------+
| Jahre erhöhen                    |
| years += 1                       |
+----------------------------------+
        |
        |<-----------------------+
        |                        |
        v                        |
+----------------------------------+
| Speichere Schritt               |
| steps.append({"year": years,    |
|    "capital": current_capital}) |
+----------------------------------+
        |
        |------------------------->|
                                   v
             +----------------------------------+
             |             Ende                 |
             | Rückgabe: years                  |
             +----------------------------------+
```

1. Der Algorithmus beginnt mit der Initialisierung der Variablen.
2. Die Hauptschleife prüft, ob das aktuelle Kapital kleiner als die Zielsumme ist.
3. Wenn ja, wird das neue Kapital berechnet, gerundet und die Jahre werden erhöht.
4. Jeder Schritt wird gespeichert.
5. Die Schleife wiederholt sich, bis das aktuelle Kapital die Zielsumme erreicht oder überschreitet.
6. Am Ende wird die Anzahl der Jahre zurückgegeben.

Der Kern des Algorithmus wird im Code wie folgt umgesetzt:

```python
years = 0
current_capital = initial_capital

while current_capital < target_sum:
    self.steps.append({"year": years, "capital": current_capital})
    current_capital *= (1 + interest_rate)
    years += 1
```

Die Berechnung stoppt, sobald die Zielsumme überschritten wird, um das erste Jahr zu ermitteln, in dem das Ziel erreicht wird. Dies ist in der Praxis oft relevanter als das exakte Erreichen der Summe.

## Anwendung

Der Algorithmus findet Anwendung in verschiedenen Bereichen:

- Finanzplanung: Berechnung von Anlagehorizonten für Sparziele
- Investitionsanalysen: Bewertung verschiedener Anlageoptionen
- Kreditwesen: Einschätzung der Gesamtkosten eines Kredits
- Bildung: Veranschaulichung des Zinseszinseffekts im Finanzunterricht

## Beispielberechnung

Angenommen:

- Anfangskapital: $P = 10000$ EUR
- Zinssatz: $r = 5\% = 0.05$
- Zielsumme: $20000$ EUR

Berechnung:

1. Jahr 0: $10000$ EUR
2. Jahr 1: $10000 \cdot 1.05 = 10500$ EUR
3. Jahr 2: $10500 \cdot 1.05 = 11025$ EUR
...
15. Jahr 15: $20789.28$ EUR

Der Algorithmus ergibt 15 Jahre, da die Zielsumme dann erstmals überschritten wird.

```tsx
import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const data = Array.from({ length: 16 }, (_, i) => ({
  year: i,
  capital: Math.round(10000 * Math.pow(1.05, i) * 100) / 100
}));

const CapitalGrowthChart = () => (
  <ResponsiveContainer width="100%" height={400}>
    <LineChart
      data={data}
      margin={{
        top: 5,
        right: 30,
        left: 20,
        bottom: 5,
      }}
    >
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="year" />
      <YAxis />
      <Tooltip />
      <Legend />
      <Line type="monotone" dataKey="capital" stroke="#8884d8" activeDot={{ r: 8 }} />
    </LineChart>
  </ResponsiveContainer>
);

export default CapitalGrowthChart;

```

Diese Grafik veranschaulicht das exponentielle Wachstum des Kapitals über die Zeit.

## Grenzen und Annahmen

Der Algorithmus basiert auf einigen vereinfachenden Annahmen:

1. Konstanter Zinssatz: In der Realität können Zinssätze schwanken.
2. Keine Gebühren oder Steuern: Diese könnten das tatsächliche Wachstum reduzieren.
3. Keine Inflation: Die Kaufkraft des Endkapitals wird nicht berücksichtigt.

## Ethische Überlegungen

Während der Zinseszinseffekt bei Investitionen positiv wirkt, kann er bei Schulden zu einer erheblichen finanziellen Belastung führen.
