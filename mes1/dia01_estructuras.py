import csv
from collections import defaultdict

casas_filtradas = []
news = []
MSZoning = []
ignoradas = 0
precios = []
caras = []
baratas = []
with open(r"d:\ml-engineer-roadmap\mes1\train.csv") as f: 
    reader = csv.DictReader(f)  
    rows =  list(reader)
    columnas = reader.fieldnames
    for fila in rows:
          # Asegúrate de que el nombre de la columna sea correcto
        nueva = fila['SaleType']
        mszoning = fila['MSZoning']
        if(mszoning != 'RM'):
            MSZoning.append(mszoning)
        if nueva == 'New':
            news.append(fila)
        if fila["SalePrice"].strip():
            precios.append(float(fila["SalePrice"]))
        else:
            ignoradas += 1
        if fila["SalePrice"].strip() and float(fila["SalePrice"]) > 200000:
            casas_filtradas.append(fila)
        
def mediana(lista):
    ordenada = sorted(lista)
    n = len(ordenada)
    mid = n // 2
    if n % 2 == 0:
        return (ordenada[mid - 1] + ordenada[mid]) / 2
    return ordenada[mid]
def carasybaratas(lista, umbral):
    for item in lista:
        if item["SalePrice"].strip():
            precio = float(item["SalePrice"])
            if precio > umbral:
                caras.append(item)
            else:
                baratas.append(item)
    return len(caras), len(baratas)


print(f"cuantas filas hay: {len(rows)}")
print(f"cuantas columnas hay: {len(columnas)}")
print(f"Casas caras y baratas con umbral de 200,000: {carasybaratas(rows, 200000)}")
print("Nombres:", ", ".join(columnas))
print(f"Media: {sum(precios)/len(precios):.2f}")
print(f"Mediana (Puro): ${mediana(precios):,.2f}")
print(f"Mín: {min(precios)} | Máx: {max(precios)}")
print(f"Ignoradas: {ignoradas} no tiene costo (empty)")
print(f"quitar duplicados: {len(set(tuple(row) for row in rows))}")
print(f"casas precio mayor a 200, 000: {len(casas_filtradas)}")
print(f"casas nuevas: {len(news)}")
print(f"direferentes de la zona RM: {len(MSZoning)}")

