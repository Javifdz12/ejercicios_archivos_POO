import pandas as pd

file1 = pd.read_csv('calificaciones2.csv',sep=";")


def informacion_alumnos(archivo):
    sep=";"
    with open(archivo) as archivo:
        next(archivo)
        alumnos=[]
        for linea in archivo:
            linea=linea.rstrip("/n")
            columnas=linea.split(sep)
            apellidos=columnas[0]
            nombre=columnas[1]
            parcial1=columnas[2]
            parcial2=columnas[3]
            ordinario1=columnas[4]
            ordinario2=columnas[5]
            practicas=columnas[6]
            ordinario_practicas=columnas[7]
            alumnos.append({"Apellidos":apellidos,"Nombre":nombre,"Parcial1":parcial1,"Parcial2":parcial2,"Ordinario1":ordinario1,"Ordinario2":ordinario2,"Practicas":practicas,"OrdianrioPracticas":ordinario_practicas})
        return(alumnos)

print(informacion_alumnos("calificaciones2.csv"))



