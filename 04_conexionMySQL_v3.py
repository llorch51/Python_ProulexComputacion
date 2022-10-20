# Lunes 29 de agosto

from distutils.log import error
import pymysql;

# definir una clase
# Clase es una plantilla de metodos y atributos
# objeto es una instancia de una clase

# metodos son las acciones que puede realizar el objeto
# atributos son las propiedades

#Tupla (inmutable): es un arreglo en donde sus elementos NO puden ser modificados durante la ejecucion del programa
#Lista (mutable): es un arreglo que SÍ puede ser modificado en tiempo de ejecucion

# objeto hereda metodos y atributos de la clase

class DataBase:
    # metodo constructor
    def __init__(self) -> None:
        try:
            self.conexion = pymysql.connect(host="localhost", user="root", password="root", db="repositorio")
            self.cursor = self.conexion.cursor()
            
            print("Conexion establecida exitosamente")
            
        except Exception as error:
            print("Error: " + str(error))
            
    def seleccionar_registro(self, id): # self es como un 'this' en java
        consulta = "SELECT * FROM publicaciones WHERE idpublicacion = '{}'".format(id)
        
        try:
            self.cursor.execute(consulta)
            resultado = self.cursor.fetchone() #perimera fila de datos
            # todos los FETCH nos regresan tuplas como tipo de dato
            #print("idpublicacion: ", resultado[0])
            print("idpublicacion: ", resultado[0])
            print("editorial: ", resultado[1])
            print("")
            print("")
            print("")
            print("")
        
        except Exception as error:
            print("Error: ", error)
            
    def selccionar_todos(self):
        consulta = "SELECT * FROM publicaciones"
        
        try:
            self.cursor.execute(consulta)
            resultado = self.cursor.fetchall()
            
            for fila in resultado:
                print(fila)
        except Exception as error:
            print("Error: ", error)    
    
# instancia
database = DataBase();
#database.seleccionar_registro(10)
database.selccionar_todos()

# () es tupla en el resultado
#tuplas, listas y diccionarios