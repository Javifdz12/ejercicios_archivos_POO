import pandas as pd
import numpy as np

file1 = pd.read_csv('calificaciones2.csv',sep=";")
data=pd.DataFrame(file1,columns=file1.columns)
print(data)

def informacion(archivo):
    pass


