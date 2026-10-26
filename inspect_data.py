import csv


def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
    return {
        "smallest": min(values),
        "largest": max(values),
        "count": len(values),
    }


length_result = inspect_column("streams_data.csv", "length")
straight_result = inspect_column("streams_data.csv", "straight_m")

print("Length (m):", length_result)
print("Straight-line distance (m):", straight_result)