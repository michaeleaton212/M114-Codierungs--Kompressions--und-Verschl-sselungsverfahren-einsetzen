# Auftrag: Zusammengesetzte Codierung und Barcodes – Lösungen

---

## Aufgabe 1: Einfacher QR-Code erstellen und lesen

### Vorgehensweise

Als Botschaft wurde gewählt:

```
Hallo TBZ! M114 QR-Code Test – Michael 2026
```

Der QR-Code wurde mit dem Python-Skript `generate_qrcodes.py` erstellt (Bibliothek: `qrcode[pil]`).  
Alternativ kann jede Online-Applikation verwendet werden, die alphanumerischen Text in einen QR-Code und zurück wandelt (z. B. qr-code-generator.com oder zxing.org/w/decode.jspx).

### Ergebnis

Die Datei `aufgabe1_einfacher_qr.png` enthält den QR-Code.  
Beim Scannen mit einem QR-Reader (Smartphone-Kamera, ZXing Decoder) erscheint exakt die obige Botschaft – der Test war erfolgreich.

---

## Aufgabe 2: Zusammengesetzte Daten in einem QR-Code (Stadionticket)

### 2.1 Datenformat des Tickets

Das Ticket enthält alle geforderten Informationen in einem kompakten, für Offline-QR-Reader lesbaren String-Format:

```
DT:<ISO8601>|TKT:<alphanumerisch>|SEAT:<nummer>|SEC:<sektor>|ID:<passnummer>|CHK:<4hex>
```

| Feld  | Bedeutung                               | Beispielwert       |
|-------|-----------------------------------------|--------------------|
| `DT`  | Datum und Uhrzeit der Veranstaltung     | `20260614T183000`  |
| `TKT` | Fortlaufende alphanumerische Ticketnummer (seit Tag-0) | `A1B2C3` |
| `SEAT`| Numerische Sitzplatznummer              | `042`              |
| `SEC` | Tribünensektor A–Z                      | `A`                |
| `ID`  | ID- oder Passnummer des Besuchers       | `X4921837462`      |
| `CHK` | 4-stellige Hex-Prüfsumme (Fälschungsschutz) | `84DE`        |

**Trennzeichen `|` (Pipe):** Ermöglicht einfaches Splitten ohne Parser-Ambiguität.  
**ISO-8601-Datumsformat** (`YYYYMMDDTHHmmss`): International standardisiert, kompakt, maschinenlesbar.

### 2.2 Fortlaufende alphanumerische Ticketnummer

Die Ticketnummer `TKT` ist eine **Base-36-Zahl** (Ziffern 0–9 und Buchstaben A–Z).  
Sie wird für jedes neu ausgestellte Ticket um 1 erhöht (analoger Zähler seit dem ersten Tag des Ticketsystems, „Tag-0").

Beispiel:
```
Tag-0:  TKT = 000000  (= 0 in Dezimal)
        TKT = 000001
        ...
        TKT = A1B2C3  (= 13.435.839 in Dezimal)
        TKT = ZZZZZZ  (= 2.176.782.335, maximaler Wert mit 6 Stellen)
```

Vorteil gegenüber rein numerischen IDs: deutlich kompakter und trotzdem eindeutig, menschenlesbar auf dem gedruckten Ticket.

### 2.3 Fälschungsschutz – Prüfsumme (CHK)

Das Ticket ist **ohne Prüfsumme fälschbar**: Ein Angreifer könnte den QR-Code entschlüsseln, die `ID`-Nummer oder den `SEAT`-Wert ändern und einen neuen QR-Code drucken.

**Lösung: Truncated SHA-256**

```
Payload = "DT:...|TKT:...|SEAT:...|SEC:...|ID:..."
CHK     = SHA-256(Payload).hexdigest()[:4].upper()
```

Der Platzanweiser-Reader berechnet dieselbe Prüfsumme aus den gelesenen Feldern und vergleicht sie mit dem `CHK`-Feld im QR-Code.  
Stimmt die Prüfsumme **nicht** überein → Ticket wurde manipuliert, Zugang verweigert.

**Stärke der Prüfsumme:**  
4 Hex-Zeichen = 16 Bit → Wahrscheinlichkeit einer zufälligen Kollision: 1/65.536.  
Für kritische Systeme könnte man 8 Zeichen (32 Bit) verwenden.

> **Hinweis:** Ein echter kryptografischer Fälschungsschutz würde einen **HMAC** (Hash-based Message Authentication Code) mit einem geheimen Schlüssel verwenden, den nur das Ticketsystem und die Stadionleser kennen. Dann kann selbst ein Angreifer, der das Format kennt, keine gültigen Tickets fälschen.

### 2.4 Ablauf am Stadioneingang

```
Besucher zeigt Ticket
       ↓
QR-Reader liest String
       ↓
System splittet Felder (Trennzeichen |)
       ↓
Prüfsumme CHK neu berechnen
  → stimmt nicht → ZUGANG VERWEIGERT ✗
       ↓
Passnummer ID mit Ausweisdokument abgleichen
  → stimmt nicht → ZUGANG VERWEIGERT ✗
       ↓
Datum/Uhrzeit DT prüfen (heutiges Datum?)
  → ungültig → ZUGANG VERWEIGERT ✗
       ↓
SEAT und SEC anzeigen → Besucher zum Platz leiten ✓
```

### 2.5 Generierte Tickets (fiktive Veranstaltungen)

#### Ticket 1 – FC Zürich vs. YB, 14.06.2026, 18:30 Uhr

**QR-Code-Datei:** `ticket1_fcz_yb_sektorA.png`

```
DT:20260614T183000|TKT:A1B2C3|SEAT:042|SEC:A|ID:X4921837462|CHK:84DE
```

| Feld | Wert |
|------|------|
| Veranstaltung | FC Zürich vs. YB |
| Datum/Zeit | 14.06.2026, 18:30 Uhr |
| Ticketnummer | A1B2C3 |
| Sitzplatz | 042 |
| Sektor | A |
| Besucher ID | X4921837462 |
| Prüfsumme | 84DE |

---

#### Ticket 2 – FC Basel vs. FC Luzern, 21.06.2026, 15:00 Uhr

**QR-Code-Datei:** `ticket2_fcb_fcl_sektorM.png`

```
DT:20260621T150000|TKT:D4E5F6|SEAT:107|SEC:M|ID:C8812345678|CHK:4A80
```

| Feld | Wert |
|------|------|
| Veranstaltung | FC Basel vs. FC Luzern |
| Datum/Zeit | 21.06.2026, 15:00 Uhr |
| Ticketnummer | D4E5F6 |
| Sitzplatz | 107 |
| Sektor | M |
| Besucher ID | C8812345678 |
| Prüfsumme | 4A80 |

---

#### Ticket 3 – Grasshoppers vs. Servette, 28.06.2026, 20:30 Uhr (VIP)

**QR-Code-Datei:** `ticket3_gc_servette_sektorZ.png`

```
DT:20260628T203000|TKT:G7H8I9|SEAT:001|SEC:Z|ID:P5509876543|CHK:3870
```

| Feld | Wert |
|------|------|
| Veranstaltung | Grasshoppers vs. Servette |
| Datum/Zeit | 28.06.2026, 20:30 Uhr |
| Ticketnummer | G7H8I9 |
| Sitzplatz | 001 |
| Sektor | Z (VIP) |
| Besucher ID | P5509876543 |
| Prüfsumme | 3870 |

---

### 2.6 QR-Code-Eigenschaften

Alle Tickets wurden mit **Fehlerkorrektur-Level H** (30%) generiert.  
Das bedeutet: bis zu 30% der QR-Grafik können beschädigt oder verschmutzt sein, ohne die Lesbarkeit zu beeinträchtigen – ideal für gedruckte Tickets, die gefaltet, nass oder zerkratzt sein könnten.

Die kodierten Strings sind ca. 60–70 Zeichen lang, was einem QR-Code der Version 3–4 entspricht (deutlich kleiner als das Maximum von 177×177 Modulen / ~4300 alphanumerische Zeichen).

---

## Zusammenfassung: Ist das Ticket fälschungssicher?

| Schutzmassnahme | Vorhanden | Schutz gegen |
|-----------------|-----------|--------------|
| Prüfsumme CHK (SHA-256 truncated) | ✓ | Zufällige Fehler, einfache Manipulation |
| ID-Pflichtabgleich vor Ort | ✓ | Ticketweitergabe, Kopie |
| Nicht-übertragbares Format (ID im Code) | ✓ | Ticket-Schwarzmarkt |
| HMAC mit geheimem Schlüssel | ✗ (empfohlen) | Gezieltes Fälschen durch Kenntnis des Formats |
| Zentrales Einlesesystem (Online) | ✗ (offline) | Mehrfachverwendung desselben Tickets |

**Fazit:** Das Ticket ist gegen alltägliche Fälschungsversuche geschützt. Für ein produktives System wäre ein HMAC-Schlüssel und eine Online-Validierung (einmaliges Entwerten) empfehlenswert.
