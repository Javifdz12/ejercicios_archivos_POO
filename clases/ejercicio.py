import pandas as pd

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
            asistencia=columnas[2]
            parcial1=columnas[3]
            parcial2=columnas[4]
            ordinario1=columnas[5]
            ordinario2=columnas[6]
            practicas=columnas[7]
            ordinario_practicas=columnas[8]
            alumnos.append({"Apellidos":apellidos,"Nombre":nombre,"Asistencia":asistencia,"Parcial1":float(parcial1),"Parcial2":float(parcial2),"Ordinario1":float(ordinario1),"Ordinario2":float(ordinario2),"Practicas":float(practicas),"OrdinarioPracticas":float(ordinario_practicas)})
        return(alumnos)

#print(informacion_alumnos("calificaciones2.csv"))

def calificacion_final(lista):
    for diccionario in lista:
        if diccionario["Ordinario1"]==0 and diccionario["Ordinario2"]==0 and diccionario["OrdinarioPracticas"]==0:
            nota_final=(diccionario["Parcial1"]*0.3)+(diccionario["Parcial2"]*0.3)+(diccionario["Practicas"]*0.4)
        elif diccionario["Ordinario1"]!=0 and diccionario["Ordinario2"]!=0 and diccionario["OrdinarioPracticas"]!=0:
            nota_final=(diccionario["Ordinario1"]*0.3)+(diccionario["Ordinario2"]*0.3)+(diccionario["OrdinarioPracticas"]*0.4)
        elif diccionario["Ordinario1"]==0 and diccionario["Ordinario2"]!=0 and diccionario["OrdinarioPracticas"]!=0:
            nota_final=(diccionario["Parcial1"]*0.3)+(diccionario["Ordinario2"]*0.3)+(diccionario["OrdinarioPracticas"]*0.4)
        elif diccionario["Ordinario1"]!=0 and diccionario["Ordinario2"]==0 and diccionario["OrdinarioPracticas"]!=0:
            nota_final=(diccionario["Ordinario1"]*0.3)+(diccionario["Parcial2"]*0.3)+(diccionario["OrdinarioPracticas"]*0.4)
        elif diccionario["Ordinario1"]!=0 and diccionario["Ordinario2"]!=0 and diccionario["OrdinarioPracticas"]==0:
            nota_final=(diccionario["Ordinario1"]*0.3)+(diccionario["Ordinario2"]*0.3)+(diccionario["Practicas"]*0.4)
        elif diccionario["Ordinario1"]==0 and diccionario["Ordinario2"]==0 and diccionario["OrdinarioPracticas"]!=0:
            nota_final=(diccionario["Parcial1"]*0.3)+(diccionario["Parcial2"]*0.3)+(diccionario["OrdinarioPracticas"]*0.4)
        elif diccionario["Ordinario1"]==0 and diccionario["Ordinario2"]!=0 and diccionario["OrdinarioPracticas"]==0:
            nota_final=(diccionario["Parcial1"]*0.3)+(diccionario["Ordinario2"]*0.3)+(diccionario["Practicas"]*0.4)
        elif diccionario["Ordinario1"]!=0 and diccionario["Ordinario2"]==0 and diccionario["OrdinarioPracticas"]==0:
            nota_final=(diccionario["Ordinario1"]*0.3)+(diccionario["Parcial2"]*0.3)+(diccionario["Practicas"]*0.4)
        diccionario["NotaFinal"]=nota_final
    return lista

#print(calificacion_final(informacion_alumnos("calificaciones2.csv")))

def aprobados_y_suspensos(lista):
    aprobados=[]
    suspensos=[]
    for diccionario in lista:
        if diccionario["NotaFinal"]<5:
            suspensos.append(diccionario["Nombre"])
        else:
            if diccionario["Ordinario1"]==0 and diccionario["Ordinario2"]==0 and diccionario["OrdinarioPracticas"]==0:
                if diccionario["Parcial1"]>4 and diccionario["Parcial2"]>4 and diccionario["Practicas"]>4:
                    aprobados.append(diccionario["Nombre"])
                else:
                    suspensos.append(diccionario["Nombre"])
            elif diccionario["Ordinario1"]!=0 and diccionario["Ordinario2"]!=0 and diccionario["OrdinarioPracticas"]!=0:
                if diccionario["Ordinario1"]>4 and diccionario["Ordinario2"]>4 and diccionario["OrdinarioPracticas"]>4:
                    aprobados.append(diccionario["Nombre"])
                else:
                    suspensos.append(diccionario["Nombre"])
            elif diccionario["Ordinario1"]==0 and diccionario["Ordinario2"]!=0 and diccionario["OrdinarioPracticas"]!=0:
                if diccionario["Parcial1"]>4 and diccionario["Ordinario2"]>4 and diccionario["OrdinarioPracticas"]>4:
                    aprobados.append(diccionario["Nombre"])
                else:
                    suspensos.append(diccionario["Nombre"])
            elif diccionario["Ordinario1"]!=0 and diccionario["Ordinario2"]==0 and diccionario["OrdinarioPracticas"]!=0:
                if diccionario["Ordinario1"]>4 and diccionario["Parcial2"]>4 and diccionario["OrdianrioPracticas"]>4:
                    aprobados.append(diccionario["Nombre"])
                else:
                    suspensos.append(diccionario["Nombre"])
            elif diccionario["Ordinario1"]!=0 and diccionario["Ordinario2"]!=0 and diccionario["OrdinarioPracticas"]==0:
                if diccionario["Ordinario1"]>4 and diccionario["Ordinario2"]>4 and diccionario["Practicas"]>4:
                    aprobados.append(diccionario["Nombre"])
                else:
                    suspensos.append(diccionario["Nombre"])
            elif diccionario["Ordinario1"]==0 and diccionario["Ordinario2"]==0 and diccionario["OrdinarioPracticas"]!=0:
                if diccionario["Parcial1"]>4 and diccionario["Parcial2"]>4 and diccionario["OrdinarioPracticas"]>4:
                    aprobados.append(diccionario["Nombre"])
                else:
                    suspensos.append(diccionario["Nombre"])
            elif diccionario["Ordinario1"]==0 and diccionario["Ordinario2"]!=0 and diccionario["OrdinarioPracticas"]==0:
                if diccionario["Parcial1"]>4 and diccionario["Ordinario2"]>4 and diccionario["Practicas"]>4:
                    aprobados.append(diccionario["Nombre"])
                else:
                    suspensos.append(diccionario["Nombre"])
            elif diccionario["Ordinario1"]!=0 and diccionario["Ordinario2"]==0 and diccionario["OrdinarioPracticas"]==0:
                if diccionario["Ordinario1"]>4 and diccionario["Parcial2"]>4 and diccionario["Practicas"]>4:
                    aprobados.append(diccionario["Nombre"])
                else:
                    suspensos.append(diccionario["Nombre"])
    return aprobados,suspensos

print(aprobados_y_suspensos(calificacion_final(informacion_alumnos("calificaciones2.csv"))))
file=pd.read_csv("calificaciones2.csv",sep=";")
data=pd.DataFrame(file,columns=file.columns)
print(data)