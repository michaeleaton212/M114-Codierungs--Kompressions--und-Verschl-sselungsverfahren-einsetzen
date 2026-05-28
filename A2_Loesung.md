# A2 Loesung: Alphanumerische Codes ASCII und Unicode

---

## Aufgabe: Welche Datei ist ASCII, UTF-8 und UTF-16 BE-BOM?

### Erkennungsmerkmal: BOM (Byte Order Mark)

Jede Kodierung hinterlaesst am Dateianfang eine charakteristische Signatur im HEX-Dump:

| Kodierung     | BOM (Hex-Bytes am Anfang) | Beschreibung                      |
|---------------|---------------------------|-----------------------------------|
| ASCII         | keiner                    | Kein BOM, Text beginnt direkt     |
| UTF-8 (o.BOM) | keiner                    | Kein BOM, wie ASCII erkennbar     |
| UTF-8 (m.BOM) | EF BB BF                  | Optionaler BOM                    |
| UTF-16 BE-BOM | **FE FF**                 | Big-Endian Markierung             |
| UTF-16 LE-BOM | FF FE                     | Little-Endian Markierung          |

**Zuordnung der drei Textsamples:**

- **Textsample mit FE FF am Anfang** = UTF-16 BE-BOM
- **Textsample ohne BOM, aber Sonderzeichen 2-Byte-kodiert (z.B. C3 A4 fuer ae)** = UTF-8
- **Textsample ohne BOM, Sonderzeichen 1-Byte-kodiert (z.B. E4 fuer ae)** = ASCII (ISO 8859-1)

---

## Aufgabe: Wie viele Zeichen enthaelt der Text?

Da alle drei Dateien denselben Text enthalten, zaehlt man die Zeichen in der ASCII-Datei (1 Byte = 1 Zeichen). Die Anzahl Bytes der ASCII-Datei entspricht direkt der Zeichenanzahl des Textes.

**Methode:** Dateigroesse der ASCII-kodierten Datei in Bytes = Anzahl Zeichen.

---

## Aufgabe: Dateigrössen und Erklaerung der Unterschiede

### Theorie der Dateigroessen

Angenommen der Text hat **n Zeichen**, davon **k Sonderzeichen** (z.B. ae, oe, ue, ss):

| Kodierung    | Dateigroesse (Bytes)       | Erklaerung                                              |
|--------------|----------------------------|---------------------------------------------------------|
| ASCII        | n                          | 1 Byte pro Zeichen, immer                               |
| UTF-8        | n + k                      | ASCII-Zeichen 1 Byte, Sonderzeichen 2 Byte              |
| UTF-16 BE    | 2 * n + 2                  | Jedes Zeichen 2 Byte, plus 2 Byte BOM (FE FF)           |

### Beispiel mit 50 Zeichen, davon 2 Sonderzeichen (ae, oe):

| Kodierung    | Berechnung         | Groesse |
|--------------|--------------------|---------|
| ASCII        | 50 * 1             | 50 Byte |
| UTF-8        | 48 * 1 + 2 * 2     | 52 Byte |
| UTF-16 BE    | 50 * 2 + 2         | 102 Byte|

### Warum zeigt Windows "0 Byte auf Datentraeger"?

Das Windows-Dateisystem NTFS speichert sehr kleine Dateien direkt in der MFT (Master File Table) anstatt in einem eigenen Cluster. Da kein separater Speicherblock auf dem Datentraeger belegt wird, zeigt Windows "0 Byte auf Datentraeger" an, obwohl die Datei Daten enthaelt.

---

## Aufgabe: Welche Zeichen sind in ASCII und UTF-8 unterschiedlich kodiert?

UTF-8 ist in den ersten 128 Zeichen (U+0000 bis U+007F) deckungsgleich mit ASCII. Unterschiede entstehen nur bei Zeichen ausserhalb dieses Bereichs, also bei Sonderzeichen wie deutschen Umlauten.

**Die zwei unterschiedlich kodierten Zeichen** (typisch fuer deutschsprachige Texte):

| Zeichen | ASCII (ISO 8859-1) | UTF-8     |
|---------|--------------------|-----------|
| ae (ae) | E4                 | C3 A4     |
| oe (oe) | F6                 | C3 B6     |
| ue (ue) | FC                 | C3 BC     |
| ss (ss) | DF                 | C3 9F     |

Der Lehrtext gibt an, dass es **genau zwei** unterschiedliche Zeichen sind. Diese findet man, indem man die HEX-Dumps der ASCII- und der UTF-8-Datei byteweise vergleicht. An den Stellen der Sonderzeichen weichen die Bytes ab: ASCII verwendet 1 Byte, UTF-8 verwendet 2 Bytes, was den Vergleich ab dieser Stelle auch versetzt.

---

## Aufgabe: Was bedeuten Big-Endian (BE) und Little-Endian (LE)?

Bei Multi-Byte-Werten (z.B. 2-Byte-Zeichen in UTF-16) muss festgelegt werden, in welcher Reihenfolge die Bytes gespeichert werden.

**Big-Endian (BE):** Das hoeChstwertige Byte (Most Significant Byte) kommt zuerst.  
**Little-Endian (LE):** Das niedrigstwertige Byte (Least Significant Byte) kommt zuerst.

### Beispiel: Das Zeichen 'A' (Unicode U+0041) in UTF-16

| Byte-Reihenfolge | Byte 1 | Byte 2 | Analoge |
|------------------|--------|--------|---------|
| Big-Endian       | 00     | 41     | wie wir Zahlen schreiben: 2025 |
| Little-Endian    | 41     | 00     | Bytes umgekehrt: 5202 |

### Alltagsanalogie aus dem Lehrtext

| Datumsformat | Bedeutung     | Beispiel     |
|--------------|---------------|--------------|
| yyyy.mm.dd   | Big-Endian    | 2025.05.21   |
| dd.mm.yyyy   | Little-Endian | 21.05.2025   |

Die BOM (Byte Order Mark) am Anfang einer UTF-16-Datei teilt dem Leseprogramm mit, welche Byte-Reihenfolge verwendet wird:

- FE FF am Anfang = Big-Endian
- FF FE am Anfang = Little-Endian

---

## Aufgabe: Notepad++ Kodierung umschalten

In Notepad++ kann man unter **Codierung** (frueherer Menuepunkt: Format) zwischen ASCII/ANSI, UTF-8, UTF-8 BOM und UTF-16 umschalten.

Was sich bei der Umschaltung aendert:

| Von -> Nach        | Sichtbare Aenderung                                       |
|--------------------|-----------------------------------------------------------|
| ASCII -> UTF-8     | Sonderzeichen koennen korrekt angezeigt werden, Datei wird minimal groesser |
| UTF-8 -> UTF-16    | Dateigroesse verdoppelt sich (ca.), BOM FE FF wird eingefuegt |
| UTF-8 -> ASCII     | Sonderzeichen ausserhalb 0-127 werden moeglicherweise falsch dargestellt oder als ? angezeigt |

Der Dateiinhalt (Bytes) aendert sich, der angezeigte Text bleibt derselbe - solange alle Zeichen in der Zielkodierung darstellbar sind.

---

## Aufgabe (Anspruchsvoll): Wie erkennt ein Textreader UTF-8 Start- und Folgebytes?

UTF-8 nutzt ein cleveres Bit-Muster, damit ein Leseprogramm immer erkennen kann, ob ein Byte ein neues Zeichen beginnt oder zu einem vorigen gehoert.

### UTF-8 Byte-Struktur

| Zeichenlaenge | Startbyte Muster | Folgebyte Muster | Codepoint-Bereich |
|---------------|------------------|------------------|-------------------|
| 1 Byte        | 0xxxxxxx         | (keiner)         | U+0000 - U+007F   |
| 2 Byte        | 110xxxxx         | 10xxxxxx         | U+0080 - U+07FF   |
| 3 Byte        | 1110xxxx         | 10xxxxxx         | U+0800 - U+FFFF   |
| 4 Byte        | 11110xxx         | 10xxxxxx         | U+10000 - U+10FFFF|

### Regeln fuer den Textreader

**Startbyte erkennen:**
- Beginnt das Byte mit `0` -> 1-Byte-Zeichen (ASCII-kompatibel), fertig
- Beginnt das Byte mit `110` -> 2-Byte-Zeichen, naechstes Byte ist Folgebyte
- Beginnt das Byte mit `1110` -> 3-Byte-Zeichen, naechste 2 Bytes sind Folgebytes
- Beginnt das Byte mit `11110` -> 4-Byte-Zeichen, naechste 3 Bytes sind Folgebytes

**Folgebyte erkennen:**
- Beginnt das Byte mit `10` -> es ist ein Folgebyte, kein neues Zeichen

### Konkretes Beispiel: ae (ae, U+00E4)

```
UTF-8 Darstellung: C3 A4

C3 = 1100 0011  -> Startbyte (110xxxxx = 2-Byte-Zeichen)
A4 = 1010 0100  -> Folgebyte (10xxxxxx)

Nutzlast-Bits extrahieren:
C3: 110[00011] -> 00011
A4: 10[100100] -> 100100

Zusammengesetzt: 00011 100100 = 0000 1110 0100 = U+00E4 = ae
```

### Vorteil dieses Systems

- Der Reader kann an jeder beliebigen Position im Bytestream einsteigen und sofort erkennen, ob er ein Start- oder Folgebyte vor sich hat
- Fehler oder fehlende Bytes koennen erkannt werden (ein 10-Byte ohne vorheriges Startbyte ist ungueltig)
- Rueckwaertskompatibilitaet mit ASCII: Alle Bytes mit fuehrender 0 sind identisch zu ASCII

---

## Zusammenfassung: ASCII vs. UTF-8 vs. UTF-16

| Eigenschaft          | ASCII (ISO 8859-1) | UTF-8            | UTF-16 BE        |
|----------------------|--------------------|------------------|------------------|
| Bit pro Zeichen      | 8 (fix)            | 8 bis 32 (variabel) | 16 bis 32 (variabel) |
| BOM                  | keiner             | optional (EF BB BF) | FE FF          |
| Kompatibel mit ASCII | ja (0-127)         | ja (0-127)       | nein             |
| Sonderzeichen (ae)   | 1 Byte (E4)        | 2 Byte (C3 A4)   | 2 Byte (00 E4)   |
| Zeichenvorrat        | 256                | 1'114'112        | 1'114'112        |
| Typische Anwendung   | Legacy-Systeme     | Web, Linux, macOS | Windows intern  |
