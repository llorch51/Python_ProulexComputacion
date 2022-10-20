#pip install pandas
import pandas

#serie: estructura d datos de una dimension
#crear una serie y le metemos una lista
serie = pandas.Series(["LUNES","MARTES", "MIERCOLES","JUEVES", "VIERNES","SABADO","DOMINGO"])

print(serie)
print("El tamanio de la serie es: ", serie.size)
print("Sus indices son: ", serie.index)


print("--------------------------------")

serie2 = ["LUNES","MARTES", "MIERCOLES","JUEVES", "VIERNES","SABADO","DOMINGO"]
print(serie2)

