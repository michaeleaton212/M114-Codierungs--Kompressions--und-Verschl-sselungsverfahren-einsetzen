"""
M114 – QR-Code Generator fuer Stadiontickets
Aufgabe 2: Zusammengesetzte Daten in einem QR-Code
"""

import qrcode
import hashlib
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))


def ticket_checksum(data: str) -> str:
    """
    4-stellige Hex-Prüfsumme (Truncated SHA-256).
    Verhindert unbemerkte Manipulation einzelner Felder.
    """
    digest = hashlib.sha256(data.encode("utf-8")).hexdigest()
    return digest[:4].upper()


def build_ticket(event_dt: str, ticket_nr: str, seat: str, sector: str, passport: str) -> str:
    """
    Zusammensetzt den Ticket-String im Format:
      DT:<ISO8601>|TKT:<alphanumerisch>|SEAT:<nummer>|SEC:<A-Z>|ID:<passnummer>|CHK:<4hex>
    """
    payload = f"DT:{event_dt}|TKT:{ticket_nr}|SEAT:{seat}|SEC:{sector}|ID:{passport}"
    chk = ticket_checksum(payload)
    return f"{payload}|CHK:{chk}"


def make_qr(data: str, filename: str):
    qr = qrcode.QRCode(
        version=None,           # auto-size
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # 30% Fehlerkorrektur
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    path = os.path.join(OUTPUT_DIR, filename)
    img.save(path)
    print(f"  Gespeichert: {filename}")
    print(f"  Daten:       {data}\n")


# ---------------------------------------------------------------------------
# Aufgabe 1: Einfacher QR-Code (kurze Botschaft)
# ---------------------------------------------------------------------------
simple_message = "Hallo TBZ! M114 QR-Code Test – Michael 2026"
print("=== Aufgabe 1: Einfacher QR-Code ===")
make_qr(simple_message, "aufgabe1_einfacher_qr.png")


# ---------------------------------------------------------------------------
# Aufgabe 2: Stadiontickets (3 fiktive Veranstaltungen)
# ---------------------------------------------------------------------------
print("=== Aufgabe 2: Stadiontickets ===")

tickets = [
    {
        "desc": "Ticket 1 – FC Zuerich vs. YB, Sektor A",
        "event_dt": "20260614T183000",   # 14.06.2026, 18:30 Uhr
        "ticket_nr": "A1B2C3",           # alphanumerisch, seit Tag-0
        "seat": "042",
        "sector": "A",
        "passport": "X4921837462",
        "file": "ticket1_fcz_yb_sektorA.png",
    },
    {
        "desc": "Ticket 2 – FC Basel vs. Luzern, Sektor M",
        "event_dt": "20260621T150000",   # 21.06.2026, 15:00 Uhr
        "ticket_nr": "D4E5F6",
        "seat": "107",
        "sector": "M",
        "passport": "C8812345678",
        "file": "ticket2_fcb_fcl_sektorM.png",
    },
    {
        "desc": "Ticket 3 – GC vs. Servette, Sektor Z (VIP)",
        "event_dt": "20260628T203000",   # 28.06.2026, 20:30 Uhr
        "ticket_nr": "G7H8I9",
        "seat": "001",
        "sector": "Z",
        "passport": "P5509876543",
        "file": "ticket3_gc_servette_sektorZ.png",
    },
]

for t in tickets:
    print(f"--- {t['desc']} ---")
    ticket_str = build_ticket(
        t["event_dt"], t["ticket_nr"], t["seat"], t["sector"], t["passport"]
    )
    make_qr(ticket_str, t["file"])

print("Fertig! Alle QR-Codes wurden im Skript-Verzeichnis gespeichert.")
