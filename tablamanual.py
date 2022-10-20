import sys
import pymysql
import pandas
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

# Clase principal
class Tabla(QMainWindow):
    # Metodo constructor
    def __init__(self):
        super().__init__()
        # Estos metodos se mandarán llamar al ejecutarse la aplicación
        self.interfaz()
        self.conexion()

    def interfaz(self):
        # Ventana
        self.setFixedSize(900,650)
        self.setWindowTitle("Python QTable")
        self.setStyleSheet("background-color:#0D2E69; color:#8FFFFB")
        self.setWindowIcon(QIcon(r"C:\Users\soporte\Desktop\Python avanzado 19a21\QT.png"))

        # Titulo
        self.titulo = QLabel("Consultas a Bases de Datos MySQL", self)
        self.titulo.setGeometry(QtCore.QRect(250, 20, 400, 50))
        self.titulo.setStyleSheet("background-color:#000000; color:#8FFFFB")
        self.titulo.setFont(QFont("Arial", 18))

        # Tabla
        self.tabla = QTableWidget(self)
        self.tabla.setGeometry(QtCore.QRect(10, 150, 880, 400))
        self.tabla.setStyleSheet("background-color:#FFFFFF; color:#000000")
        # Establecer el numero de columnas
        self.tabla.setColumnCount(16)
        # Establecer el numero de filas
        self.tabla.setRowCount(0)
        # Alternar el color de las filas
        self.tabla.setAlternatingRowColors(True)
        # Asignar un tamaño vertical especifico
        self.tabla.verticalHeader().setDefaultSectionSize(20)
        # Asignar el nombre a las etiquetas de las columnas
        nombreColumnas = ("idempleado","paterno","materno","nombre","año_nacimiento","mes","estado_nacimiento","puesto","sueldo","prox_jubilarse","antiguedad","edad","peso","altura","presion","glucosa")
        # Enviar la tupla a las etiquetas de la QTable
        self.tabla.setHorizontalHeaderLabels(nombreColumnas)

        # Menu
        self.menu = QMenu()
        for indice, columna in enumerate(nombreColumnas, start=0):
            accion = QAction(columna, self.menu)
            accion.setCheckable(True)
            accion.setChecked(True)
            accion.setData(indice)
            self.menu.addAction(accion)

        # Boton vinculado a la logica del objeto menu
        self.btnMostrarOcultar = QPushButton("Mostrar u Ocultar", self)
        self.btnMostrarOcultar.setMenu(self.menu)
        self.btnMostrarOcultar.setGeometry(QtCore.QRect(10, 100, 200, 30))
        self.btnMostrarOcultar.setStyleSheet("background-color:#CEDAE1; color: #000000; border-radius: 15px")
        self.btnMostrarOcultar.setFont(QFont("Arial", 14))
        
        #Mandar llamar el método mostrarOcultar()
        self.menu.triggered.connect(self.mostrarOcultar)
        
        #-------BOTONES--------------
        #Consultar
        self.btnConsultar = QPushButton("Consultar", self)
        self.btnConsultar.setGeometry(QtCore.QRect(150, 580, 100, 40))
        self.btnConsultar.setStyleSheet("QPushButton"
                                        "{"
                                        "background-color:#CEDAE1;"
                                        "color: #000000;"
                                        "border-radius: 15px;"
                                        "}"
                                        "QPushButton::hover"
                                        "{"
                                        "background-color : lightgreen;"
                                        "}"
                                        "QPushButton::pressed"
                                        "{"
                                        "background-color : red;"
                                        "color: white;"
                                        "}")
        self.btnConsultar.setFont(QFont("Arial", 14))
        self.btnConsultar.clicked.connect(self.consultar)
        
        #Exportar
        self.btnExportar = QPushButton("Exportar", self)
        self.btnExportar.setGeometry(QtCore.QRect(300, 580, 100, 40))
        self.btnExportar.setStyleSheet("QPushButton"
                                       "{"
                                       "background-color:#CEDAE1;"
                                       "color: #000000;"
                                       "border-radius: 15px;"
                                       "}"
                                       "QPushButton::hover"
                                       "{"
                                       "background-color : lightgreen;"
                                       "}"
                                       "QPushButton::pressed"
                                       "{"
                                       "background-color : red;"
                                       "color: white;"
                                       "}")
        self.btnExportar.setFont(QFont("Arial", 14))
        self.btnExportar.clicked.connect(self.exportar)
        
        #Eliminar
        self.btnEliminar = QPushButton("Eliminar", self)
        self.btnEliminar.setGeometry(QtCore.QRect(450, 580, 100, 40))
        self.btnEliminar.setStyleSheet("QPushButton"
                                       "{"
                                       "background-color:#CEDAE1;"
                                       "color: #000000;"
                                       "border-radius: 15px;"
                                       "}"
                                       "QPushButton::hover"
                                       "{"
                                       "background-color : #ff003b;"
                                       "}"
                                       "QPushButton::pressed"
                                       "{"
                                       "background-color : red;"
                                       "color: white;"
                                       "}")
        self.btnEliminar.setFont(QFont("Arial", 14))
        self.btnEliminar.clicked.connect(self.eliminar)
        
        #Registrar
        self.btnRegistrar = QPushButton("Registrar", self)
        self.btnRegistrar.setGeometry(QtCore.QRect(600, 580, 100, 40))
        #self.btnRegistrar.setStyleSheet("background-color:#CEDAE1; color: #000000; border-radius: 15px")
        self.btnRegistrar.setStyleSheet("QPushButton"
                                        "{"
                                        #"border-style:solid;"
                                        #"border-width:3px;"
                                        #"border-color: white"
                                        "border: 2px solid red;"
                                        "background-color:white;"
                                        "color: #000000;"
                                        "border-radius: 15px;"
                                        "}"
                                        "QPushButton::hover"
                                        "{"
                                        "background-color : red;"
                                        "color: white;"
                                        "}"
                                        "QPushButton::pressed"
                                        "{"
                                        "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 1 black, stop: 0 red);"
                                        #"background-color : red;"
                                        "color: white;"
                                        "border: 2px solid black;"
                                        "}")
        
        self.btnRegistrar.setFont(QFont("Arial", 14))
        self.btnRegistrar.clicked.connect(self.registrar)
        
    def mostrarOcultar(self, accion):
        columna = accion.data()
        if accion.isChecked():
            self.tabla.setColumnHidden(columna, False)
        else:
            self.tabla.setColumnHidden(columna, True)
    
    def conexion(self):
        try:
            self.con = pymysql.connect(host="localhost",user="root",password="root",db="empresa")
            self.cursor = self.con.cursor()
            #QMessageBox.information(self, "Conexion", "Conexion exitosa")
            #Mandar llamar el método consultar
        except Exception as error:
            QMessageBox.warning(self, "ERROR", "SE presento el error: ", str(error))
            
    def consultar(self):
        self.conexion()
        #variable que contiene la consulta
        consulta = "SELECT * FROM empleados"
        try:
            #ejecuto la variable que tiene la consulta
            self.cursor.execute(consulta)
            #recupero los datos que devuelve la consulta ejecutada
            resultados = self.cursor.fetchall()
            #recorro las tuplas guardadas en "resultados"
            for resultado in resultados:
                print(resultado)
            #las tuplas que estan en Resultados las envio a una variable nueva Datos    
            datos = resultados
            #limpiar la QTable por si ya hay datos previos
            self.tabla.clearContents()
            #variable llamada Fila
            fila = 0
            #ciclo For para cargar datos a la QTable
            for x in datos:
                #agregar una fila nueva a la QTable
                self.tabla.setRowCount(fila + 1)
                
                #enviar los datos a la fila correspondiente
                self.tabla.setItem(fila, 0, QTableWidgetItem(str(x[0])))
                self.tabla.setItem(fila, 1, QTableWidgetItem(str(x[1])))
                self.tabla.setItem(fila, 2, QTableWidgetItem(str(x[2])))
                self.tabla.setItem(fila, 3, QTableWidgetItem(str(x[3])))
                self.tabla.setItem(fila, 4, QTableWidgetItem(str(x[4])))
                self.tabla.setItem(fila, 5, QTableWidgetItem(str(x[5])))
                self.tabla.setItem(fila, 6, QTableWidgetItem(str(x[6])))
                self.tabla.setItem(fila, 7, QTableWidgetItem(str(x[7])))
                self.tabla.setItem(fila, 8, QTableWidgetItem(str(x[8])))
                self.tabla.setItem(fila, 9, QTableWidgetItem(str(x[9])))
                self.tabla.setItem(fila, 10, QTableWidgetItem(str(x[10])))
                self.tabla.setItem(fila, 11, QTableWidgetItem(str(x[11])))
                self.tabla.setItem(fila, 12, QTableWidgetItem(str(x[12])))
                self.tabla.setItem(fila, 13, QTableWidgetItem(str(x[13])))
                self.tabla.setItem(fila, 14, QTableWidgetItem(str(x[14])))
                self.tabla.setItem(fila, 15, QTableWidgetItem(str(x[15])))
                
                fila += 1
            
        except Exception as error:
            QMessageBox.warning(self, "ERROR", "SE presento el error: ", str(error)) 
    
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
                    
            dataFrame.to_excel(r"D:\ProgramAvan\Python\exportacion.xlsx")
            QMessageBox.information(self,"Exportacion", "Exportacion exitosa")
                
        except Exception as error:
            QMessageBox.warning(self, "ERROR", "SE presento el error: ", str(error))
        
    
    def eliminar(self):
        pass
    
    def registrar(self):
        #almacenar los datos ingresados en las variables
        try:
            paterno, ingresar = QInputDialog.getText(self,"Paterno","Apellido paterno:", QLineEdit.Normal,"")
            materno, ingresar = QInputDialog.getText(self,"Materno","Apellido materno:", QLineEdit.Normal,"")
            nombre, ingresar = QInputDialog.getText(self,"Nombre","Nombre:", QLineEdit.Normal,"")
            año_nacimiento, ingresar =QInputDialog.getInt(self, "AñoNacimiento","año de nacimiento:",1990,1950,2000,1)
            #               (default, minimo, maximo, incremento)
            
            tuplaMeses=("ENERO","FEBRERO","MARZO","ABRIL","MAYO","JUNIO","JULIO","AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE")
            mes, ingresar = QInputDialog.getItem(self,"Mes","Mes:",tuplaMeses,0,False)
            
            tuplaEstados=("JALISCO","CDMX","NUEVO LEON","COLIMA")
            estado_nacimiento, ingresar = QInputDialog.getItem(self,"Estado","Estado:",tuplaEstados,False)
            
            tuplaPuestos = ("ADMINISTRATIVO","PRODUCCION","DIRECTIVO")
            puesto, ingresar = QInputDialog.getItem(self,"Puesto","Puesto:",tuplaPuestos,False)
            
            sueldo, ingresar = QInputDialog.getDouble(self,"Sueldo","Sueldo:",1,1,50000,1000)
            
            prox_jubilarse = "NO"
            antiguedad = 0
            edad, ingresar = QInputDialog.getInt(self, "Edad","Edad:",18,18,72,1)
            peso, altura, presion, glucosa = 0,0,0,0
            
        except Exception as error:
            QMessageBox.warning(self, "ERROR", "SE presento el error: ", str(error))
            
        #registro de los datos en la tabla empleados
        try:
            datos = "INSERT INTO empleados (paterno,materno,nombre,año_nacimiento,mes,estado_nacimiento,puesto,sueldo,prox_jubilarse,antiguedad,edad,peso,altura, presion, glucosa) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(paterno,materno,nombre,año_nacimiento,mes,estado_nacimiento,puesto,sueldo,prox_jubilarse,antiguedad,edad,peso,altura, presion, glucosa)
            
            self.cursor.execute(datos)
            self.con.commit()
            QMessageBox.information(self,"REgistro","Registro aplicado correectamente")
            
        except Exception as error:
            QMessageBox.warning(self, "ERROR", "SE presento el error: ", str(error))
        pass
if __name__ == "__main__":
    app = QApplication(sys.argv)
    tabla = Tabla()
    tabla.show()
    sys.exit(app.exec())

