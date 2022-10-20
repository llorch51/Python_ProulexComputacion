import pandas as pd

df = pd.read_csv(r"D:\ProgramAvan\Python\votos.csv", encoding="utf8")
#imprimir la cantidad de filas de una columna
print("El total de datos por columnas es: ", df.count())


#cuantas veces se repite cada estado
print(df["estado"].value_counts())

#calculos aplicados a los votos
print("Suma de votos:",df["votos"].sum())
print("Valor minimo de los votos:",df["votos"].min())
print("Valor maximo de los votos",df["votos"].max())
print("Media de los votos:",df["votos"].mean())
print("Desviacion estandar de los votos:",df["votos"].std())


#Consultas
consulta1 = df.query("votos > 10000")
consulta2 = df.query('candidato == "Hillary Clinton"')
consulta3 = df.query('estado_ab in ["AK","AL","TX"]')
consulta4 = df.query('votos > 12000 and partido == "Democrat"')

if consulta1.shape[0] == 0:
    print("La consulta 1 esta vacia")
else:
    consulta1.to_csv(r"D:\ProgramAvan\Python\consulta1.csv")
    
if consulta2.shape[0] == 0:
    print("La consulta 1 esta vacia")
else:
    consulta1.to_html(r"D:\ProgramAvan\Python\consulta1.html")