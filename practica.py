import csv

with open("practica.csv", newline="") as archivo:
    lector = csv.reader(archivo)

    for fila in lector:
        print(fila)