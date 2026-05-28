# A1 Loesung: Zahlensysteme und numerische Codes

---

## Aufgabe 1: BIN-DEC-HEX Zahlentabelle

**MSB** = Most Significant Bit = das hoeChstwertigste Bit (ganz links)
**LSB** = Least Significant Bit = das kleinstwertigste Bit (ganz rechts)

| BIN (MSB) | BIN | BIN | BIN (LSB) | DEC | HEX |
|:---------:|:---:|:---:|:---------:|:---:|:---:|
| 0 | 0 | 0 | 0 |  0 | 0 |
| 0 | 0 | 0 | 1 |  1 | 1 |
| 0 | 0 | 1 | 0 |  2 | 2 |
| 0 | 0 | 1 | 1 |  3 | 3 |
| 0 | 1 | 0 | 0 |  4 | 4 |
| 0 | 1 | 0 | 1 |  5 | 5 |
| 0 | 1 | 1 | 0 |  6 | 6 |
| 0 | 1 | 1 | 1 |  7 | 7 |
| 1 | 0 | 0 | 0 |  8 | 8 |
| 1 | 0 | 0 | 1 |  9 | 9 |
| 1 | 0 | 1 | 0 | 10 | A |
| 1 | 0 | 1 | 1 | 11 | B |
| 1 | 1 | 0 | 0 | 12 | C |
| 1 | 1 | 0 | 1 | 13 | D |
| 1 | 1 | 1 | 0 | 14 | E |
| 1 | 1 | 1 | 1 | 15 | F |

---

## Aufgabe 2: Dezimal 911 -> Binaer

Methode: Wiederholte Division durch 2, Reste von unten nach oben lesen.

| Division | Ergebnis | Rest |
|----------|----------|------|
| 911 / 2  | 455      | 1    |
| 455 / 2  | 227      | 1    |
| 227 / 2  | 113      | 1    |
| 113 / 2  |  56      | 1    |
|  56 / 2  |  28      | 0    |
|  28 / 2  |  14      | 0    |
|  14 / 2  |   7      | 0    |
|   7 / 2  |   3      | 1    |
|   3 / 2  |   1      | 1    |
|   1 / 2  |   0      | 1    |

**Ergebnis: 911 (DEC) = 1110'0011'1 (BIN)**

Probe: 512 + 256 + 128 + 0 + 0 + 0 + 8 + 4 + 2 + 1 = 911

---

## Aufgabe 3: Binaer 1011'0110 -> Dezimal

```
Bit-Position:  7    6    5    4    3    2    1    0
Binaer:        1    0    1    1    0    1    1    0
Wert:        128    0   32   16    0    4    2    0
```

128 + 32 + 16 + 4 + 2 = **182**

**Ergebnis: 1011'0110 (BIN) = 182 (DEC)**

---

## Aufgabe 4: Binaer 1110'0010'1010'0101 -> Hexadezimal

Jede Gruppe von 4 Bit entspricht genau einer HEX-Ziffer:

```
1110  0010  1010  0101
 E     2     A     5
```

**Ergebnis: 1110'0010'1010'0101 (BIN) = E2A5 (HEX)**

---

## Aufgabe 5: ALU Addierer

**Zahl-A:** 1101'1001  
**Zahl-B:** 0111'0101

Binaere Addition:

```
  1101 1001
+ 0111 0101
-----------
1 0100 1110
^
Carry-Bit (Uebertrag)
```

Schrittweise (von rechts):

| Position | A | B | Carry-in | Summe | Carry-out |
|----------|---|---|----------|-------|-----------|
| 0        | 1 | 1 | 0        | 0     | 1         |
| 1        | 0 | 0 | 1        | 1     | 0         |
| 2        | 0 | 1 | 0        | 1     | 0         |
| 3        | 1 | 0 | 0        | 1     | 0         |
| 4        | 1 | 1 | 0        | 0     | 1         |
| 5        | 0 | 1 | 1        | 0     | 1         |
| 6        | 1 | 1 | 1        | 1     | 1         |
| 7        | 1 | 0 | 1        | 0     | 1         |

Das 8-Bit-Resultatregister enthaelt: **0100'1110**  
Das Carry-Bit ist gesetzt: **1**

**Erklaerung:** Zahl-A = 217 (DEC), Zahl-B = 117 (DEC), Summe = 334 (DEC).  
334 ueberschreitet den maximalen 8-Bit-Wert von 255. Es tritt ein **Data Overflow** auf. Das Carry-Bit wird gesetzt. Das Resultatregister enthaelt nur den unteren Teil der Summe (334 - 256 = 78 = 0100'1110).

---

## Aufgabe 6: Wireshark OSI-Layer3 (IPv4-Adresse)

Binaer: `1100 0000 . 1010 1000 . 0100 1100 . 1101 0011`

Jedes Oktett in Dezimal umwandeln:

| Binaer      | Dezimal |
|-------------|---------|
| 1100 0000   | 192     |
| 1010 1000   | 168     |
| 0100 1100   |  76     |
| 1101 0011   | 211     |

**Ergebnis: 192.168.76.211**

Es handelt sich um eine **IPv4-Adresse** im privaten Adressbereich (192.168.x.x gemaess RFC 1918). Diese Adresse wird in lokalen Netzwerken (LAN) verwendet und ist im Internet nicht routingfaehig. Die Adresse ist auf OSI-Layer 3 (Netzwerkschicht/Network Layer) angesiedelt.

---

## Aufgabe 7: Wireshark OSI-Layer2 (MAC-Adresse)

Binaer: `1011 1110 - 1000 0011 - 1000 0101 - 1101 0101 - 1110 0100 - 1111 1110`

Jedes Byte in Hexadezimal umwandeln:

| Binaer      | HEX |
|-------------|-----|
| 1011 1110   | BE  |
| 1000 0011   | 83  |
| 1000 0101   | 85  |
| 1101 0101   | D5  |
| 1110 0100   | E4  |
| 1111 1110   | FE  |

**Ergebnis: BE:83:85:D5:E4:FE**

Es handelt sich um eine **MAC-Adresse** (Media Access Control). MAC-Adressen sind auf OSI-Layer 2 (Sicherungsschicht/Data Link Layer) angesiedelt und identifizieren Netzwerkkarten eindeutig weltweit. Sie bestehen aus 6 Byte (48 Bit) und werden in HEX-Notation geschrieben.

---

## Aufgabe 8: chmod 751 CreateWeeklyReport

Der Befehl `chmod 751 CreateWeeklyReport` setzt die Zugriffsrechte auf die Datei `CreateWeeklyReport`.

Die Zahl 751 wird in drei oktale Ziffern aufgeteilt:

| Ziffer | Benutzerkreis | Binaer | Rechte           |
|--------|---------------|--------|------------------|
| 7      | Owner         | 111    | rwx (lesen, schreiben, ausfuehren) |
| 5      | Group         | 101    | r-x (lesen, ausfuehren)            |
| 1      | Others        | 001    | --x (nur ausfuehren)               |

**Bedeutung:** Der Eigentuemer darf die Datei lesen, beschreiben und ausfuehren. Mitglieder der Gruppe duerfen sie lesen und ausfuehren, aber nicht schreiben. Alle anderen duerfen die Datei nur ausfuehren.

---

## Aufgabe 9: Matterhorn-Express, 107 Gondeln

Gefragt: Wie viele Bits benoetigt man, um 107 Gondeln eindeutig zu adressieren?

```
2^6 =  64  -> zu wenig (64 < 107)
2^7 = 128  -> genuegt (128 >= 107)
```

**Ergebnis: 7 Bit** sind mindestens noetig, um alle 107 Gondeln eindeutig zu nummerieren (adressierbar von 0000000 bis 1101010).

---

## Aufgabe 10: Register ADD-Operation

Register-1 (8 Bit): `1001 1110`  
Register-2 (8 Bit): `1100 1101`

```
  1001 1110   (= 158 DEC)
+ 1100 1101   (= 205 DEC)
-----------
1 0110 1011
^
Carry-Bit gesetzt -> Overflow!
```

158 + 205 = 363 > 255 -> **Data Overflow**

**Register-3 enthaelt: 0110'1011** (= 107 DEC)  
Das Carry-Bit ist gesetzt. Das mathematisch korrekte Resultat (363) kann in einer 8-Bit-Speicherzelle nicht dargestellt werden.

---

## Aufgabe 11: Arbeitsspeicher 4 kiB

```
4 kiB = 4 * 1024 Byte = 4096 Byte
1 Byte = 8 Bit
4096 Byte * 8 Bit/Byte = 32768 Bit
```

**Ergebnis: 32768 Bit = 32 kiB**

---

## Aufgabe 12: Arbeitsspeicher 12-Bit-Adressbus, 16-Bit-Datenbus

**Speicherkapazitaet:**

```
Anzahl Speicherstellen: 2^12 = 4096
Datenbusbreite:         16 Bit = 2 Byte pro Speicherstelle
Kapazitaet:             4096 * 2 Byte = 8192 Byte = 8 kiB
```

**Speicherkapazitaet: 8 kiB**

**Erste Speicheradresse:** `0x000` (= 0000 0000 0000 in Binaer = 0 in Dezimal)

**Letzte Speicheradresse:** `0xFFF` (= 1111 1111 1111 in Binaer = 4095 in Dezimal)

---

## Aufgabe 13: Serielle Leitung mit 1 MHz Taktsignal

**Seriell (1 Bit pro Takt):**

```
1 MHz = 1'000'000 Takte/Sekunde
1 Bit pro Takt
-> 1'000'000 bit/s / 8 = 125'000 Byte/s = 125 kB/s
```

**Seriell: 125'000 Byte pro Sekunde (125 kB/s)**

**Parallel (8 Bit pro Takt):**

```
1 MHz = 1'000'000 Takte/Sekunde
8 Bit (1 Byte) pro Takt
-> 1'000'000 Byte/s = 1 MB/s
```

**Parallel 8-Bit: 1'000'000 Byte pro Sekunde (1 MB/s)**

Die parallele Uebertragung ist 8x schneller als die serielle.

---

## Aufgabe 14: Signed und Unsigned Integer (1 Byte = 8 Bit)

### a. Unsigned (Vorzeichenlos)

| | Binaer | Dezimal |
|---|--------|---------|
| Kleinster Wert | 0000 0000 | 0 |
| Groesster Wert | 1111 1111 | 255 |

Wertebereich: 0 bis 255

### b. Signed (Vorzeichenbehaftet, Zweierkomplement)

| | Binaer | Dezimal |
|---|--------|---------|
| Kleinster Wert | 1000 0000 | -128 |
| Groesster Wert | 0111 1111 | +127 |

Wertebereich: -128 bis +127

### c. +82 als vorzeichenbehafteter Binaerwert (Signed)

Da +82 positiv ist, entspricht es direkt der binaeren Darstellung mit fuehrender 0:

82 = 64 + 16 + 2 = 0101'0010

**Ergebnis: +82 (DEC) = 0101'0010 (BIN, Signed)**

---

## Aufgabe 15: Fliesskommazahlen (Floating Point)

**Problem mit Ganzzahlen:** `1 / 3 * 3` ergibt als Integer 0 (statt 1), da der Nachkommaanteil verloren geht.

**Loesung:** Fliesskommazahlen nach dem IEEE 754 Standard.

Eine Fliesskommazahl besteht aus drei Teilen:

| Teil | Single Precision (32 Bit) | Double Precision (64 Bit) |
|------|---------------------------|---------------------------|
| Vorzeichen (S) | 1 Bit | 1 Bit |
| Exponent (E)   | 8 Bit | 11 Bit |
| Mantisse (M)   | 23 Bit | 52 Bit |

**Formel:** `Wert = (-1)^S * 1.M * 2^(E - Bias)`

Beispiel: Die Zahl 5.75 in Single Precision (32 Bit):

```
5.75 (DEC) -> 101.11 (BIN) -> 1.0111 * 2^2

Vorzeichen: 0 (positiv)
Exponent:   2 + 127 (Bias) = 129 = 1000 0001
Mantisse:   01110000000000000000000

Binaer: 0 10000001 01110000000000000000000
```

---

## Aufgabe 16: Autosilo mit BCD (Binary Coded Dezimal)

**BCD = Binary Coded Decimal:** Jede Dezimalziffer (0-9) wird separat mit 4 Bit kodiert.

**Konzept fuer den Autosilo (Parkslots 1-10):**

Eingabe am Terminal (Ziffern 0-9) wird direkt in BCD umgewandelt:

| Dezimal | BCD (4 Bit) |
|---------|-------------|
| 1       | 0001        |
| 2       | 0010        |
| 3       | 0011        |
| 4       | 0100        |
| 5       | 0101        |
| 6       | 0110        |
| 7       | 0111        |
| 8       | 1000        |
| 9       | 1001        |
| 10      | 0001 0000   |

**Realisierung:**

Die Liftsteuerung empfaengt den BCD-kodierten Wert vom Eingabeterminal. Slot 10 wird mit zwei BCD-Stellen dargestellt (0001 0000). Die 10 Lampen fuer freie Slots sind jeweils einem Bit zugeordnet (1 = frei, 0 = belegt). Die Steuerung vergleicht die eingegebene BCD-Zahl mit der gespeicherten Slot-Adresse und faehrt den Lift zur entsprechenden Etage.
