# 26 de agosto
import pymysql;

# crear un objeto de conexion
conexion = pymysql.connect(host="localhost", user="root", password="root", db="repositorio");

#generar cursor para recorrer informacion
cursor = conexion.cursor();

# generar consulta
cursor.execute("SELECT * FROM publicaciones");

# recuperar datos, mostrar consulta
#mostrar UNA fila
resultado_sencillo = cursor.fetchone();
print(resultado_sencillo);

# mostrar varias filas
resultado_varios = cursor.fetchmany(10);
print(resultado_varios);

# mostrar tods las filas
resultado_todos = cursor.fetchall();
#print(resultado_todos);

# mostrar los resultaos por fila
for fila in resultado_todos:
    print(fila)

# cerrar cursor
cursor.close();

#tupla, lista, diccionario