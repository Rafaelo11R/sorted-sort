import csv
import os

data = [
    ["Namn", "Ålder", "Stad"],
    ["Alice", 25, "Stockholm"],
    ["Bob", 30, "Göteborg"],
    ["Charlie", 22, "Malmö"]
]

filnamn = "data.csv"

# Skapar CSV-filen
with open(filnamn, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Kolla om filen skapades och skriv ut sökvägen
if os.path.exists(filnamn):
    print(f"CSV-filen skapades: {os.path.abspath(filnamn)}")
else:
    print("Filen skapades inte.")
