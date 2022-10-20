# Martes 30 de agosto y 31 de agosto

import pymysql

class Operaciones:
    def __init__(self) -> None: #metodo constructor
        try:
            self.conexion = pymysql.connect(host="localhost", user="root", password="root", db="banco")
            self.cursor = self.conexion.cursor()
            print("Conexion establecida exitosamente")
            print("==============================================")
            
        except Exception as error:
            print(error)
    
    def seleccionar_todos_clientes(self):
        consulta = "SELECT * FROM clientes"
        
        try:
            self.cursor.execute(consulta)
            resultado = self.cursor.fetchall()
            for fila in resultado:
                print(fila)
        
        except Exception as error:
            print(error)
    
    def seleccionar_un_cliente(self, id):
        consulta = "SELECT * FROM clientes WHERE idcliente = '{}'".format(id)
        try:
            self.cursor.execute(consulta)
            resultado = self.cursor.fetchone()
            print("ID cliente: ", resultado[0])
            print("Apellido Paterno: ", resultado[1])
            print("Apellido Materno: ", resultado[2])
            print("Nombre: ", resultado[3])
            print("Teléfono: ", resultado[4])
            print("Correo: ", resultado[5])
            
        except Exception as error:
            print(error)
    
    def insertar_cliente(self, paterno, materno, nombre, tel, correo):
        registro = "INSERT INTO clientes(paterno, materno, nombre, telefono, correo) values('{}','{}','{}','{}','{}')".format(paterno, materno, nombre, tel, correo)
        
        try:
            self.cursor.execute(registro) #ejecuta query
            self.conexion.commit() #commit hace que los cambios sean permanentes en la BBDD
            print("Registro realizado correctamente!")
            
        except Exception as error:
            print(error)
            print("Error de registro")
    
    def eliminar_cliente(self, id):
        validar = "SELECT * FROM clientes WHERE idcliente = '{}'".format(id)
        
        try:
            self.cursor.execute(validar)
            resultado = self.cursor.fetchone()
            print(resultado)
            if resultado == None:
                print("El Id: '{}'".format(id) +" ingresado no existe")
            else:  
                eliminar = "DELETE FROM clientes WHERE idcliente = '{}'".format(id)
                self.cursor.execute(eliminar)
                self.conexion.commit()
                print("********************************")
                print("registro eliminado correctamente con ID: '{}'".format(id))
        except Exception as error:
            print(error)
    
    def actualizar_cliente(self, id):
        validar = "SELECT * FROM clientes WHERE idcliente = '{}'".format(id)
        
        try:
            self.cursor.execute(validar)
            resultado = self.cursor.fetchone()
            
            if resultado == None:
                print("ID no existe")
            else:
                print("Los datos actuales del cliente son: ")
                print()
                print("Teléfono: ", resultado[4])
                print("Correo: ", resultado[5])
                print()
                telefono = str(input("Ingrese nuevo teléfono: "))
                correo = str(input("Ingrese nuevo Correo: "))
                
                actualizar = "UPDATE clientes SET telefono = '{}', correo = '{}' WHERE idcliente = '{}'".format(telefono, correo, id)
                self.cursor.execute(actualizar)
                self.conexion.commit()
                
                actualizado_validar = "SELECT * FROM clientes WHERE idcliente = '{}'".format(id)
                self.cursor.execute(actualizado_validar)
                actualizado_validar = self.cursor.fetchone()
                
                print("Los nuevos datos del cliente son: ")
                print()
                print("Teléfono: ", resultado[4])
                print("Correo: ", resultado[5])
                print()
                
        except Exception as error:
            print(error)
    