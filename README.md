# ETL-Pipeline: CSV -> PostgreSQL

Mein erstes Data-Engineering-Projekt.
Ein Python-Script liest verkaufsdaten aus einer CSV-Datei, bereinigt sie und lädt sie in eine PostgreSQL-Datenbank.

## Was das Script macht

- **Extract:** liest 'prodaja.csv' mit pandas.
- **Transform:** füllt fehlende Mengen mit 0, berechnet 'ukupno' (Menge x Preis), rundet auf 2 Nachkommastellen.
- **Load:** schreibt die Daten in die Tabelle 'prodaja' in PostgreSQL.

Zusätlich:
- Kein doppelter import (Tabelle wird vor jedem Lauf geleert -> idempotent)
- Fehlerbehandlung bei fehlender CSV oder fehlender DB-Verbindung
- Zugangsdaten in einer '.env'-Datei statt im Code


## Technologien 

- Python 3 (pandas, psycopg2, python-dotenv)
- PostgreSQL 
- Ubuntu (VM)


## Starten 

1. Virtuelle umgebung erstellen und Pakete installieren:
'''bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
'''

2. Eine '.env' -Datei anlegen
'''
    DB_HOST=localhost
    DB_NAME=de_modul1
    DB_USER=dein_user
    DB_PASSWORD=dein_passwort
'''

3. Script starten:
''' bash
    python load_data.py
'''

### Was ich gelernt habe

- SQL: GROUP BY, HAVING, ORDER BY, LIMIT, Aggregatfunktionen
- ETL-Prozess mit python und pandas 
- Fehlerbehandlung mit try/except
- Zugangsdaten sicher mit .env verwalten
















