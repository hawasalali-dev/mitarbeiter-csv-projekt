import csv

with open("mitarbeiter.csv", "w", newline="", encoding="utf-8") as datei:
    writer = csv.writer(datei, delimiter=";")

    # Kopfzeile
    writer.writerow(["ID", "Name", "Abteilung", "Gehalt"])

    # Mitarbeiterdaten
    writer.writerow([101, "Anna Schmidt", "IT", 45000])
    writer.writerow([102, "Max Müller", "Vertrieb", 42000])
    writer.writerow([103, "Sophie Becker", "Personal", 40000])

print("CSV-Datei erstellt.")


with open("mitarbeiter.csv", "a", newline="", encoding="utf-8") as datei:
    writer = csv.writer(datei, delimiter=";")

    writer.writerow([104, "Lukas Weber", "Marketing", 39000])

print("Neuer Mitarbeiter hinzugefügt.")

print("\nMitarbeiterliste:")

with open("mitarbeiter.csv", "r", encoding="utf-8") as datei:
    reader = csv.DictReader(datei, delimiter=";")

    for mitarbeiter in reader:
        print(
            f"[{mitarbeiter['ID']}] "
            f"{mitarbeiter['Name']} arbeitet in der Abteilung "
            f"{mitarbeiter['Abteilung']}."
        )
        
        summe = 0
anzahl = 0

with open("mitarbeiter.csv", "r", encoding="utf-8") as datei:
    reader = csv.DictReader(datei, delimiter=";")

    for mitarbeiter in reader:
        summe += int(mitarbeiter["Gehalt"])
        anzahl += 1

durchschnitt = summe / anzahl

print(f"\nDurchschnittsgehalt: {durchschnitt:.2f} €")