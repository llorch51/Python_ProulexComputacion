
print("Numero de líneas: ", end="")
filas = int(input())
num = 1

for i in range(filas):
    for j in range(i + 1):
        print(num, end=" ")
        num = num + 1
    print()