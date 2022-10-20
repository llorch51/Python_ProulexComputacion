
numero_terminos = int(input("Numero de terminos: "))

#primeros dos terminos. SOn d cajon
n1, n2 = 0, 1
count = 0

#validar que el termino sea mayor que uno
if numero_terminos <= 0:
    print("Introducir numero positivo")

#si sólo es el primer termino
elif numero_terminos == 1:
    print("Secuencia fibonacci: ", numero_terminos, ":")
    print(n1)
#genrar secuencia fibonacci
else: #todo lo que sea diferente de 1, en el numero de terminos
    print("Fibonacci: ")
    while count < numero_terminos:
        print(n1, end=" ")
        acumulador = n1 + n2
        #actualizar valores
        n1 = n2
        n2 = acumulador
        count += 1