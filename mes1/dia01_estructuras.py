import csv
from collections import defaultdict

with open("train.csv") as f:
    rows = list(csv.DictReader(f))

precios = [float(r["SalePrice"]) for r in rows if r["SalePrice"]]
print(f"Media: {sum(precios)/len(precios):.2f}")
print(f"Mín: {min(precios)} | Máx: {max(precios)}")