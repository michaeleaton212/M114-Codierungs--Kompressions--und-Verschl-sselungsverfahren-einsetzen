# Aufgabe 2 - Loesungen: Codierung

**Technische Berufsschule Zuerich | Modul 114**

---

## Aufgabe 1: Binaer-Zaehlen (0 bis 15)

| Dezimal | 4-Bit   | 8-Bit (Nibbles) |
|---------|---------|-----------------|
| 0       | 0000    | 0000 0000       |
| 1       | 0001    | 0000 0001       |
| 2       | 0010    | 0000 0010       |
| 3       | 0011    | 0000 0011       |
| 4       | 0100    | 0000 0100       |
| 5       | 0101    | 0000 0101       |
| 6       | 0110    | 0000 0110       |
| 7       | 0111    | 0000 0111       |
| 8       | 1000    | 0000 1000       |
| 9       | 1001    | 0000 1001       |
| 10      | 1010    | 0000 1010       |
| 11      | 1011    | 0000 1011       |
| 12      | 1100    | 0000 1100       |
| 13      | 1101    | 0000 1101       |
| 14      | 1110    | 0000 1110       |
| 15      | 1111    | 0000 1111       |

**Merkregel Finger-Zaehlen (eine Hand):**

Jeder Finger entspricht einer Zweierpotenz:

| Finger         | Wert |
|----------------|------|
| Daumen         | 1    |
| Zeigefinger    | 2    |
| Mittelfinger   | 4    |
| Ringfinger     | 8    |
| Kleiner Finger | 16   |

Finger hoch = 1, Finger unten = 0. Mit einer Hand sind die Werte 0 bis 31 darstellbar.

---

## Aufgabe 2: Festspeicher-Groessen berechnen

Beispiel: **512 GB SSD** (Herstellerangabe, dezimal)

### Dezimal (Herstellerangabe, 1 KB = 1000 B)

| Einheit      | Wert                  |
|--------------|-----------------------|
| Byte (B)     | 512'000'000'000 B     |
| Kilobyte (KB)| 512'000'000 KB        |
| Megabyte (MB)| 512'000 MB            |
| Gigabyte (GB)| 512 GB                |
| Terabyte (TB)| 0.512 TB              |

### Binaer / IEC (Betriebssystem, 1 KiB = 1024 B)

| Einheit        | Wert               |
|----------------|--------------------|
| Byte (B)       | 512'000'000'000 B  |
| Kibibyte (KiB) | 499'511'718.75 KiB |
| Mebibyte (MiB) | 487'804.49 MiB     |
| Gibibyte (GiB) | 476.84 GiB         |
| Tebibyte (TiB) | 0.466 TiB          |

**Erklaerung der Differenz:** Hersteller rechnen mit 1 KB = 1000 B, das Betriebssystem mit 1 KiB = 1024 B. Daher zeigt Windows/macOS bei einer 512 GB SSD nur ca. 476 GiB an. Die Datenmenge ist identisch, nur die Berechnungsgrundlage unterscheidet sich.

---

## Aufgabe 3: Erkenntnisse (Lernjournal)

**Binaersystem:** Computer arbeiten mit zwei Zustaenden (0 und 1), weil Transistoren entweder Strom leiten oder nicht. Ein Bit ist die kleinste Informationseinheit.

**Datenmenge:** 8 Bit = 1 Byte. Mit N Bit lassen sich 2^N verschiedene Zustaende darstellen. Ein Byte kann 256 Zustaende (0 bis 255) repraesentieren.

**Speichereinheiten:** Es gibt zwei Systeme: dezimal (1 KB = 1000 B, Hersteller) und binaer (1 KiB = 1024 B, Betriebssystem). Daraus entstehen die bekannten Unterschiede bei der angezeigten Festplattenkapazitaet.

**Nibble:** 4 Bit werden als Nibble bezeichnet. Binaerzahlen werden oft in Nibbles gruppiert dargestellt, z.B. `0000 0101` fuer den dezimalen Wert 5.

**Geschichte:** Vom Abacus (500 v.Chr.) ueber Zuse Z3 (1941) bis zum ENIAC (1945) fuehrte die Entwicklung von mechanischen zu elektronischen Computern. Elektronenroehren wurden ab 1953 durch Transistoren ersetzt, was die moderne Computertechnik ermoeglichte.

---

## Aufgabe 4: Binaer-Dezimal Trainingsrechner

Uebungsbeispiele zur manuellen Umrechnung:

| Binaer      | Dezimal | Rechenweg              |
|-------------|---------|------------------------|
| 0000 1010   | 10      | 8 + 2 = 10             |
| 0001 1111   | 31      | 16 + 8 + 4 + 2 + 1 = 31 |
| 0101 0101   | 85      | 64 + 16 + 4 + 1 = 85   |
| 1000 0000   | 128     | 128                    |
| 1111 1111   | 255     | 128+64+32+16+8+4+2+1 = 255 |

**Umrechnungsmethode Dezimal zu Binaer (Division durch 2):**

```
42 / 2 = 21 Rest 0
21 / 2 = 10 Rest 1
10 / 2 =  5 Rest 0
 5 / 2 =  2 Rest 1
 2 / 2 =  1 Rest 0
 1 / 2 =  0 Rest 1
```

Reste von unten nach oben lesen: **42 dezimal = 0010 1010 binaer**

---

## Aufgabe 5: Git-Uebungen A1 und A2

Link zu den Uebungen:
```
https://gitlab.com/ch-tbz-it/Stud/m114/-/tree/main/A.%20Daten%20codieren
```

**A1 - Binaer codieren:** Umrechnung von Dezimalzahlen in Binaer und umgekehrt. Methode: Division durch 2 (Dezimal zu Binaer) bzw. Stellenwerte addieren (Binaer zu Dezimal).

**A2 - Speichereinheiten:** Umrechnung zwischen Bit, Byte, KB/KiB, MB/MiB, GB/GiB, TB/TiB im dezimalen und binaeren System.
