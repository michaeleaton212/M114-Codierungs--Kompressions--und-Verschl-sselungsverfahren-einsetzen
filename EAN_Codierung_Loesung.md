# Auftrag 3 – EAN-Codierung: Lösung

## Aufgabe 1: EAN-13 Prüfziffer-Rechner (Excel)

Die Excel-Datei ist hier verfügbar: [EAN13_Pruefziffer.xlsx](./EAN13_Pruefziffer.xlsx)

### Aufbau des Sheets

| Bereich | Inhalt |
|---|---|
| Zeile 3 | Positionsbeschriftungen (Pos 1–12, PZ 13) |
| Zeile 4 (B4:M4) | Eingabefelder für die ersten 12 EAN-Ziffern |
| Zeile 5 N5 | Automatisch berechnete Prüfziffer (fett, goldfarben) |
| Zeilen 8–12 | Schrittweise Berechnung nach EAN-Algorithmus |
| Zeilen 16–18 | Testbeispiele mit Verifikation |

### Formel in Excel (Zelle N5)

```
=MOD(10-MOD((B5+D5+F5+H5+J5+L5)+3*(C5+E5+G5+I5+K5+M5),10),10)
```

---

## Prüfziffer-Algorithmus (EAN-13)

Der Algorithmus berechnet die 13. Stelle aus den ersten 12 Ziffern:

**Schritt 1** – Summe aller Ziffern an ungeraden Positionen (1, 3, 5, 7, 9, 11):

```
S1 = d1 + d3 + d5 + d7 + d9 + d11
```

**Schritt 2** – Summe aller Ziffern an geraden Positionen (2, 4, 6, 8, 10, 12):

```
S2 = d2 + d4 + d6 + d8 + d10 + d12
```

**Schritt 3** – Geraden-Summe mit 3 multiplizieren:

```
S3 = S2 × 3
```

**Schritt 4** – Gesamtsumme:

```
S4 = S1 + S3
```

**Schritt 5** – Prüfziffer:

```
PZ = (10 - (S4 mod 10)) mod 10
```

Der zweite `mod 10` stellt sicher, dass bei einem Rest von 0 die Prüfziffer ebenfalls 0 und nicht 10 lautet.

---

## Rechenbeispiel aus dem Auftrag

EAN-13: `011373559243` → PZ = **3**

| Position | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ziffer | 0 | 1 | 1 | 3 | 7 | 3 | 5 | 5 | 9 | 2 | 4 | 3 |
| Ungerade | 0 | – | 1 | – | 7 | – | 5 | – | 9 | – | 4 | – |
| Gerade | – | 1 | – | 3 | – | 3 | – | 5 | – | 2 | – | 3 |

```
S1 = 0 + 1 + 7 + 5 + 9 + 4 = 26
S2 = 1 + 3 + 3 + 5 + 2 + 3 = 17
S3 = 17 × 3 = 51
S4 = 26 + 51 = 77
PZ = (10 - (77 mod 10)) mod 10 = (10 - 7) mod 10 = 3
```

Vollständiger EAN-13: **0113735592433**

---

## Aufgabe 2: Zusammengesetzte Codierung / Barcodes (A3)

### Aufbau eines EAN-8 Codes

Am Beispiel `42099697` (Vanille Coke):

```
[Hellzone] [101] [AAAA: 4 Nutzzeichen] [01010] [CCCC: 4 Nutzzeichen] [101] [Hellzone]
```

| Abschnitt | Modul-Folge | Bedeutung |
|---|---|---|
| Randzeichen links | `101` | 3 feste Module |
| Nutzzeichen 1. Gruppe | 4 × 7 Bit (Zeichensatz A) | erste 4 Ziffern |
| Trennzeichen | `01010` | 5 feste Module |
| Nutzzeichen 2. Gruppe | 4 × 7 Bit (Zeichensatz C) | letzte 4 Ziffern (inkl. PZ) |
| Randzeichen rechts | `101` | 3 feste Module |

Gesamtbreite EAN-8: **67 Module**

### Zeichensatz-Tabelle (Auszug)

| Ziffer | Satz A | Satz B | Satz C |
|---|---|---|---|
| 0 | 0001101 | 0100111 | 1110010 |
| 1 | 0011001 | 0110011 | 1100110 |
| 2 | 0010011 | 0011011 | 1101100 |
| 4 | 0100011 | 0011101 | 1011100 |
| 9 | 0001011 | 0010111 | 1110100 |

Die erste Ziffer `4` aus Zeichensatz A ergibt: `0100011`

Schwarze Balken = Bit 1, weisse Lücken = Bit 0.

### Codierung der ersten drei Zeichen von EAN-8 `42099697`

**Randzeichen links:** `101`

**Ziffer 4** (Zeichensatz A): `0100011`

**Ziffer 2** (Zeichensatz A): `0010011`

**Ziffer 0** (Zeichensatz A): `0001101`

Vollständige Bitfolge (Anfang): `101 | 0100011 | 0010011 | 0001101 | ...`

### EAN-13 vs. EAN-8 im Vergleich

| Merkmal | EAN-8 | EAN-13 |
|---|---|---|
| Stellen gesamt | 8 (7 codiert + 1 PZ) | 13 (12 codiert + 1 PZ) |
| Spalten gesamt | 67 | 95 |
| Nutzzeichen 1. Gruppe | 4 × Zeichensatz A | 6 × Zeichensatz A oder B |
| Nutzzeichen 2. Gruppe | 4 × Zeichensatz C | 6 × Zeichensatz C |
| Einsatzgebiet | Kleine Verpackungen | Standardartikel |

### Codierungsregel EAN-13

Beim EAN-13 bestimmt die erste Ziffer (Systemziffer, nicht im Barcode codiert), welche Kombination aus Zeichensatz A und B für die 1. Gruppe verwendet wird. So wird die 13. Stelle implizit enkodiert, ohne eine eigene Spaltengruppe zu benötigen.

---

## Weiterführende Code-Typen

**1D numerisch:** ISBN, POSTNET, ITF, Interleaved 2 of 5, Codabar, Code 11

**1D alphanumerisch:** Plessey, Code 39, Code 93, LOGMARS, Code 128

**2D:** QR-Code (Punkte statt Striche), Data Matrix

**1D/2D Mischcode (Composite):** Kombiniert EAN mit 2D-Komponente für Verfallsdaten etc.

**4D Code:** Erweitert 2D um Farbe als zusätzliche Dimension.

---

*Technische Berufsschule Zürich – Modul 114 – Auftrag 3*
