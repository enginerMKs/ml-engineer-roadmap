import csv
import numpy as np

with open(r"d:\ml-engineer-roadmap\mes1\train.csv") as f: 
    rows = list(csv.DictReader(f))

precios = np.array(
    [float(r["SalePrice"]) for r in rows if r["SalePrice"].strip()],
    dtype=np.float64
)

caras   = precios[precios > 200_000]
baratas = precios[precios <= 200_000]

p25, p50, p75 = np.percentile(precios, [25, 50, 75])
iqr = p75 - p25

norm = (precios - precios.min()) / (precios.max() - precios.min())

p25, p75 = np.percentile(precios, [25, 75])
iqr = p75 - p25

lim_inf = p25 - 1.5 * iqr
lim_sup = p75 + 1.5 * iqr

outliers = precios[(precios < lim_inf) | (precios > lim_sup)]
limpios  = precios[(precios >= lim_inf) & (precios <= lim_sup)]

print(f"Caras  : {len(caras):,}  | Media: ${caras.mean():,.0f}")
print(f"Baratas: {len(baratas):,} | Media: ${baratas.mean():,.0f}")

print(f"P25 : ${p25:,.0f}")
print(f"P50 : ${p50:,.0f}  ← mediana")
print(f"P75 : ${p75:,.0f}")
print(f"IQR : ${iqr:,.0f}  ← rango intercuartílico")

print(f"Antes → mín: {precios.min():.0f} | máx: {precios.max():.0f}")
print(f"Después → mín: {norm.min():.4f} | máx: {norm.max():.4f}")
print(f"Primer precio normalizado: {norm[0]:.4f}")

print(f"Outliers detectados: {len(outliers)}")
print(f"Dataset limpio     : {len(limpios)} filas")
print(f"Media sin outliers : ${limpios.mean():,.2f}")

print(f"Media   : ${precios.mean():,.2f}")
print(f"Mediana : ${np.median(precios):,.2f}")
print(f"Mín     : ${precios.min():,.2f}")
print(f"Máx     : ${precios.max():,.2f}")
print(f"Desv est: ${precios.std():,.2f}")
print(f"Varianza : ${precios.var():,.2f}")
