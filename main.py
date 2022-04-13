from clases.ejercicio import informacion_alumnos,calificacion_final,aprobados_y_suspensos

if __name__ == '__main__':
    #print(informacion_alumnos("calificaciones2.csv"))
    #print(calificacion_final(informacion_alumnos("calificaciones2.csv")))
    print(aprobados_y_suspensos(calificacion_final(informacion_alumnos("calificaciones2.csv"))))