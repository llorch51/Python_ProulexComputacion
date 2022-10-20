import pandas

#serie con datos numericos
serie = pandas.Series([98,77,66,86,65,99,70,89,60,90,99])

#numero de elementos
print("La serie contiene ", serie.count(), " elementos")
#sumar numeros
print("La suma es: ", serie.sum())
#suma cumulada de la serie
print("La suma cumulada es: ", serie.cumsum())
#calcular la frecuencia
print(serie.value_counts())
#maximo y minimo
print("El valor maximo es: ", serie.max(), " y el minimo es: ", serie.min())
#calcular la media
print("La media es:", serie.mean())
#desviacion estandar
print("Desviacion estandar: ", serie.std())
# metodo de descripcion
print(serie.describe())