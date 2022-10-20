#DataFrame: estructura de datos de dos dimensiones
import pandas

#creacion de un diccionario de python
datos = {'Nombre':['Maria','Gerardo','Esther','Alejandro'],
         'Edad':[18, 22, 30, 35],
         'Altura':[1.62, 1.95, 1.53, 1.80],
         'Disciplina':['Fisica','Matematicas','Administración','Informatica'],
         'Vigente':[True,True,True,False]
       }

#enviar el diccionario a un DataFrame
df = pandas.DataFrame(datos)

#imprimir algunas caracteristicas de DataFrame
#imprimir forma
print(df.shape)
print("----------------------")
print(df.size)
print("----------------------")
print(df.columns)
print("----------------------")
print(df.dtypes)
print("----------------------")
print(df.head(1))
print("----------------------")
print(df.tail(1))
print("----------------------")
print(df.get("Nombre"))
print("----------------------")
