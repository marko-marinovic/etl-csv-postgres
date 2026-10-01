import pandas as pd
import psycopg2
import sys
import os
from dotenv import load_dotenv
load_dotenv()
try:
    df = pd.read_csv("prodaja.csv")
except FileNotFoundError:
    print("FEHLER: prodaja.csv wurde nicht gefunden")
    sys.exit(1)
print("Sirovi podaci:")
print(df)


df["kolicina"] = df["kolicina"].fillna(0).astype(int)

df["ukupno"] =(df["kolicina"] * df["cijena"]).round(2)

print("\nOciscenje podaci:")
print(df)
try:
    conn = psycopg2.connect(
	host=os.getenv("DB_HOST"),
	database=os.getenv("DB_NAME"),
	user=os.getenv("DB_USER"),
	password=os.getenv("DB_PASSWORD")
    )
except psycopg2.OperationalError as e:
    print("FEHLER: Keine Verbindung zur Datenbank")
    print("Details:", e)
    sys.exit(1)

cur =conn.cursor()

cur.execute("""
	CREATE TABLE IF NOT EXISTS prodaja (
		id SERIAL PRIMARY KEY,
	  	datum DATE,
		proizvod TEXT,
		kategorija TEXT,
		kolicina INTEGER,
		cijena NUMERIC,
		ukupno NUMERIC
)
""")

cur.execute("TRUNCATE TABLE prodaja RESTART IDENTITY;")

for _, row in df.iterrows():
	cur.execute(
		"INSERT INTO prodaja (datum, proizvod, kategorija, kolicina, cijena, ukupno) VALUES (%s, %s, %s, %s, %s, %s)",
		(row["datum"], row["proizvod"], row["kategorija"], row["kolicina"], row["cijena"], row["ukupno"])
	)

conn.commit()
cur.close()
conn.close()
print("\nGotovo - podaci ubaceni u bazu.")
