import csv

with open("ward.csv", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
   # print("Number of rows:", len(rows))
    #print("Columns:", list(rows[0].keys()))

import csv

with open("ward.csv", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

values =[]
for row in rows:
    value = float(row["area_km2"])
    values.append(value)

#print("Smallest:", min(values))
#print("Largest:", max(values))
#print("Count:", len(values))

import csv

#with open("ward.csv", encoding="utf-8-sig") as f:
#    rows = list(csv.DictReader(f))

#values = []
#for row in rows:
#    raw = row["area_km2"].strip()
 #   if raw == "":
 #       continue
 #   values.append(float(raw))

#print("Smallest:", min(values))
#print("Largest:", max(values))
#print("Count:", len(values))

import csv

def inspect_column(filename, column_name):
    with open(filename, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    values = []
    for row in rows:
        raw = row[column_name].strip()
        if raw == "":
            continue
        values.append(float(raw))
    return {
        "smallest": min(values),
        "largest": max(values),
        "count": len(values)
    }


area_result = inspect_column("ward.csv", "area_km2")
pop_result = inspect_column("ward.csv", "population")

print("Area:", area_result)
print("Population:", pop_result)

