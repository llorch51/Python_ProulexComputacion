# Importar las librerias
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymysql
import pandas

# Clase que hereda QMainWindow
class Ventana(QMainWindow):
    # Metodo contructor de la clase
    def __init__(self):
        super().__init__()
        # Cargar la interfaz del QT Designer
        uic.loadUi(r"D:\ProgramAvan\Python\ProyectoUI\ventanaConexion.ui", self)
        # Cargr icono para la ventana
        self.setWindowIcon(QIcon(r"D:\ProgramAvan\Python\ProyectoUI\proyecto.py"))
        # Modificar el titulo de la ventana
        self.setWindowTitle("Conexión")
        #formato password a la txtPassword
        self.txtPassword.setEchoMode(QLineEdit.Password)
        # Asociar los botones a los metodos
        self.btnConectar.clicked.connect(self.conexion)
        self.btnCancelar.clicked.connect(self.salirConexion)
        #Establecer el tamaño maximo de mi ventana
        #self.setMaximumSize(728,607)
        #self.setMinimumSize(728,607)
        
        
    def abrirConsultas(self):
        self.hide()
        consultas = Consultas(self)#Instancia de la Clase para abrir la ventana
        consultas.show()#Mostrarla
    
    def salirConexion(self):
        pregunta = QMessageBox.question(self, "ATENCION", "¿Quieres salir?", QMessageBox.Yes, QMessageBox.No)
        if pregunta == QMessageBox.Yes:
            self.close()
        else:
            QMessageBox.information(self, "ATENCION", "Continuarás en la aplicacion")
    
    def conexion(self):
        global h,u,p,datos
        
        h = self.txtHost.text()
        u = self.txtUser.text()
        p = self.txtPassword.text()
        datos = self.txtDB.text()
        
        try:
            self.con = pymysql.connect(host=h, user=u, passwd=p, db=datos)
            self.cursor = self.con.cursor()
            QMessageBox.information(self, "Conexion", "conexion establcida exitosamente")
            #Mostrar la interfaz de las consultas consultas
            self.abrirConsultas()
            
        except Exception as error:
            QMessageBox.warning(self, "Error", str(error))
            
    
#clase consultas
class Consultas (QMainWindow):#Hereda de QMainWindow
    # parent: padre/madre | none: ninguno
    def __init__(self, parent=None):
        super(Consultas, self).__init__(parent)
        #cargar la intrfaz de la clase consultas
        uic.loadUi(r"D:\ProgramAvan\Python\ProyectoUI\ventanaConsultas.ui", self)
        #mandar llamar la carga de datos en la comboBox
        self.mostrarTablas()
        #asociar los botones a los metodos
        self.btnSalir.clicked.connect(self.regresarConexion)
        self.btnExportar.clicked.connect(self.exportar)
        self.btnConsultar.clicked.connect(self.recuperarDatos)
        
    def conexionConsultas(self,h,u,p,datos):
        try:
            self.con = pymysql.connect(host=h, user=u, passwd=p, db=datos)
            self.cursor = self.con.cursor()
            
        except Exception as error:
            print(error)
    
    def mostrarTablas(self):
        global h,u,p,datos
        self.conexionConsultas(h,u,p,datos)
        
        try:
            #consulta para recuperar el nombre de las tablas
            nombre_tablas = "SHOW TABLES"
            #ejecutar la consulta
            self.cursor.execute(nombre_tablas)
            #recuperar los resultados
            nombre_tablas = self.cursor.fetchall()
            #print(nombre_tablas)
            #recorrer el nombr de las tablas
            for n in nombre_tablas:
                self.cbTablas.addItem(str(n[0]))
            
        except Exception as error:
            print(error)
        pass
    
    def regresarConexion(self):
        pregunta = QMessageBox.question(self,"Atención","¿Realmente desea cerrar y abrir otra conexión?", QMessageBox.Yes, QMessageBox.No)

        if pregunta == QMessageBox.Yes:
            self.parent().show()
            self.close()
        else:
            QMessageBox.information(self,"Atención","Se canceló la operación")

    
    def recuperarDatos(self):
        global h,u,p,datos

        self.conexionConsultas(h,u,p,datos)

        # Etapa para recuperar la cantidad de columnas de la tabla seleccionada
        try:
            # Recuperar el nombre de la tabla seleccionada
            tabla = self.cbTablas.currentText()
            # Crear la consulta
            campos = "SELECT COUNT(COLUMN_NAME) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = '{}' AND TABLE_NAME = '{}'".format(datos,tabla)
            # Ejecutar la consulta
            self.cursor.execute(campos)
            # Recuperar el valor
            campos = self.cursor.fetchone()
            # Recorrer el resultado guardado en "campos" y almacenar el valor en una variable nueva
            for c in campos:
                cantidad = int(c)
                print(cantidad)
            # Enviar la cantidad a las columnas de la QTable
            self.tabla.setColumnCount(cantidad)
        except Exception as error:
            print(error)

        # Etapa para recuperar el nombre de las columnas de la tabla seleccionada
        try:
            # Consulta
            nombre_columnas = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = '{}' AND TABLE_NAME = '{}' order by ORDINAL_POSITION".format(datos,tabla)
            # Ejecutar la consulta
            self.cursor.execute(nombre_columnas)
            # Recuperar los valores
            nombre_columnas = self.cursor.fetchall()
            # Declarar una lista
            lista = []
            # Recorres el nombre de las columas
            for n in nombre_columnas:
                valor = n[0]
                lista.append(valor)
            # Declarar una tupla
            tupla = tuple(lista)
            # Establecer las etiquetas de la QTable
            self.tabla.setHorizontalHeaderLabels(tupla)
        except Exception as error:
            print(error)

        # Etapa 3 para recuperar los datos de la tabla MySQL hacía la QTable
        try:
            # Consulta
            consulta = "SELECT * FROM {}".format(tabla)
            # Ejecutar la consulta
            self.cursor.execute(consulta)
            # Recuperar los datos
            consulta = self.cursor.fetchall()
            # Imprimir en terminal
            for row in consulta:
                print(row)
            
            #guardamos las tuplas recuperadas en un nuevo objeto
            tuplas = consulta
            #variable de doble proposito llamada "fila"
            # 1- me servirá para agregar nuevas filas a la QTable - setRowCount()
            # 2- Indicarle a python donde posicionar un dato dentro de la QTable - setItem()
            fila = 0
            #Limpiar la QTAble antes de enviarle nuevos datos
            self.tabla.clearContents()
            #comienza la carga de datos hacia la QTable
            for tupla in tuplas:
                #agregar una nueva fila a la QTable
                self.tabla.setRowCount(fila + 1)
                #generar una variable llamada columna
                columna = 0
                # ciclo while
                #mientras la variable columna sea menor a la variable Cantidad,
                #seguiré agregando items a la fila de la QTable
                while columna <= cantidad -1:
                    #añadir el item a la fila
                    self.tabla.setItem(fila, columna, QTableWidgetItem(str(tupla[columna])))
                    #generar el incremento de la variable
                    #evaluar si la variable x == y, si es así incremento z
                    
                    columna += 1
                    
                fila += 1
                
            
        except Exception as error:
            print(error)
    
    def exportar(self):
        try:
            #crear una lista para los ncabezados de la Qtable
            encabezados = []
            #reccorrer las columnas de la Qtable
            for c in range(self.tabla.model().columnCount()):
                #agregar el valor String de las columnas al array
                encabezados.append(self.tabla.horizontalHeaderItem(c).text())
            
            #enviar el valor de las columnas al objeto dataFrame    
            dataFrame = pandas.DataFrame(columns=encabezados)
            
            #recorrer las filas de la QTable
            for f in range(self.tabla.rowCount()):
                #recorrer las celdas de cada fila
                for celda in range(self.tabla.columnCount()):
                    #agregar al dataFrame las celdas de cada fila
                    dataFrame.at[f, encabezados[celda]] = self.tabla.item(f, celda).text()
            
            tabla = self.cbtablas.currentText()      
            dataFrame.to_excel("D:\ProgramAvan\Python\{}.xlsx").format(tabla)
            QMessageBox.information(self,"Exportacion", "Exportacion exitosa")
                
        except Exception as error:
            QMessageBox.warning(self, "ERROR", "SE presento el error: ", str(error))
        

# Constructor general
if __name__ == "__main__":
    # Instancia para iniciar la aplicacion
    app = QApplication(sys.argv)
    # Crear un objeto de la clase padre/madre
    ventana = Ventana()
    # Mostrar el objeto
    ventana.show()
    # Ejecutar la app
    app.exec()
