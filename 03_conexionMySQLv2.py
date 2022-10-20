# 26 de agosto
import pymysql
from pymysql import MySQLError

try:
    conexion = pymysql.connect(host="localhost", user="root", password="root", db="repositorio")
    print("conexion establecida exitosamente")
except Exception as error:
    print(error)
    
try:
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM publicaciones WHERE idpublicacion = 2498")
    resultado = cursor.fetchone() #primera fila de datos
    print(resultado)
except MySQLError as error_consulta:
    print(error_consulta)