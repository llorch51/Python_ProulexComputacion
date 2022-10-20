# Martes 30 de agosto y 31 de agosto
#ambos archivos necesitan estar en la misma carpeta

import operacionesBanco;

class Control:
    def __init__(self) -> None:
        print("Bienvenidos al sistema de bases de datos")
        while True:
            try:
                print("==============================================")
                print("Menu de operaciones Banco")
                print("1)- Seleccionar todos los clientes")
                print("2)- Seleccionar un cliente")
                print("3)- Insertarun nuevo cliente")
                print("4)- Eliminar un cliente")
                print("5)- Actualizar datos de contacto del cliente")
                print("6)- Salir")
                print("============================================")
                opcion = int(input("Seleccione una opcion: "))
            except ValueError:
                print("Favor de ingresar una opcion válida")
            else:
                if opcion < 1 or opcion > 6:
                    print("No es una opción válida")
                    continue
                if opcion == 1:
                    operaciones.seleccionar_todos_clientes()
                elif opcion == 2:
                    id = int(input("Ingresa un ID: "))
                    print("Los resultaos de la consulta son: ", "\n")
                    operaciones.seleccionar_un_cliente(id)
                elif opcion == 3:
                    print("Ingrese los datos del cliente que desea registrar: ")
                    paterno = str(input("Apellido paterno: "))
                    materno = str(input("Apellido materno: "))
                    nombre = str(input("Nombre: "))
                    tel = str(input("Teléfono: "))
                    correo = str(input("Correo: "))
                    
                    operaciones.insertar_cliente(paterno, materno, nombre, tel, correo)
                    
                elif opcion == 4:
                    #print("Ingrese el ID del cliente a eliminar: ")
                    id = int(input("Ingrese el ID del cliente a eliminar: "))
                    operaciones.eliminar_cliente(id)
                    
                elif opcion == 5:
                    id = int(input("Ingrese el ID del cliente a actualizar: "))
                    operaciones.actualizar_cliente(id)
                else:
                    break
                print("*****************************************")
                print("** Gracias por usar nuestra aplicación **")
                
operaciones =  operacionesBanco.Operaciones()
control = Control()
    
    
