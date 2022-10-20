# Miercoles 3 de agosto y 1 de septiembre

from logging import exception
import sys, os, pymysql, pandas
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore

class VentanaConexion(QMainWindow):
    def __init__(self) -> None: #Metodo constructor / todo aqui se ejecuta primero
        super().__init__()
        self.interfaz()
        
    def interfaz(self): 
        #ventana
        self.setFixedSize(650, 300)
        self.setWindowTitle("Unión de Repúblicas Socialistas Soviéticas")
        self.setStyleSheet("background-color: red")
        self.setWindowIcon(QIcon(r"D:\ProgramAvan\Python\qt.png"))
        
        #titulo
        #geometria (columna, fila, tamaño H, tamaño V)
        self.lbtitulo = QLabel("¡Proletarios del mundo, uníos!", self)
        self.lbtitulo.setGeometry(QtCore.QRect(150,15,350,25))
        self.lbtitulo.setStyleSheet("background-color: yellow; color: black")
        self.lbtitulo.setFont(QFont("Consolas", 16))
        
        #Host
        self.lbhost = QLabel("Host: ", self)
        self.lbhost.setGeometry(QtCore.QRect(20,70,50,25))
        self.lbhost.setStyleSheet("background-color: gray; color: black")
        self.lbhost.setFont(QFont("Consolas", 14))
        
        self.txthost = QLineEdit(self)
        #self.txthost = QLabel("Host: ", self)
        self.txthost.setGeometry(QtCore.QRect(80,70,500,25))
        self.txthost.setStyleSheet("background-color: gray; color: black")
        self.txthost.setFont(QFont("Consolas", 16))
        self.txthost.setText("localhost")
        self.txthost.setPlaceholderText("Escribe el host...")
        self.txthost.setFocus()
        
        #usuario
        self.lbusuario = QLabel("Usuario: ", self)
        self.lbusuario.setGeometry(QtCore.QRect(20,120,80,25))
        self.lbusuario.setStyleSheet("background-color: gray; color: black")
        self.lbusuario.setFont(QFont("Consolas", 14))
        
        self.txtusuario = QLineEdit(self)
        self.txtusuario.setGeometry(QtCore.QRect(110,120,200,25))
        self.txtusuario.setStyleSheet("background-color: gray; color: black")
        self.txtusuario.setFont(QFont("Consolas", 16))
        self.txtusuario.setText("root")
        self.txtusuario.setPlaceholderText("Josef Stalin")
        
        
        #contraseña
        self.lbcontrasena = QLabel("Contraseña: ", self)
        self.lbcontrasena.setGeometry(QtCore.QRect(320,120,80,25))
        self.lbcontrasena.setStyleSheet("background-color: gray; color: black")
        self.lbcontrasena.setFont(QFont("Consolas", 14))
        
        self.txtcontrasena = QLineEdit(self)
        self.txtcontrasena.setGeometry(QtCore.QRect(410,120,200,25))
        self.txtcontrasena.setStyleSheet("background-color: gray; color: black")
        self.txtcontrasena.setFont(QFont("Consolas", 16))
        self.txtcontrasena.setText("root")
        self.txtcontrasena.setPlaceholderText("666")
        self.txtcontrasena.setEchoMode(QLineEdit.Password)
        
        
        #base de datos
        self.lbBD = QLabel("BBDD: ", self)
        self.lbBD.setGeometry(QtCore.QRect(20,170,80,25))
        self.lbBD.setStyleSheet("background-color: gray; color: black")
        self.lbBD.setFont(QFont("Consolas", 14))
        
        self.txtBD = QLineEdit(self)
        self.txtBD.setGeometry(QtCore.QRect(110,170,300,25))
        self.txtBD.setStyleSheet("background-color: gray; color: black")
        self.txtBD.setFont(QFont("Consolas", 16))
        self.txtBD.setText("banco")
        self.txtBD.setPlaceholderText("Nombre del Gulag")
        
        #Botones
        self.btnaceptar = QPushButton("Aceptar", self)
        self.btnaceptar.setGeometry(200, 220, 100, 50)
        self.btnaceptar.setStyleSheet("background-color: yellow; color: black")
        self.btnaceptar.setFont(QFont("Consolas", 14))
        self.btnaceptar.clicked.connect(self.variablesConexion)#Asociacion del boton a un método
        
        self.btncancelar = QPushButton("Cancelar", self)
        self.btncancelar.setGeometry(350, 220, 100, 50)
        self.btncancelar.setStyleSheet("background-color: yellow; color: black")
        self.btncancelar.setFont(QFont("Consolas", 14))
        self.btncancelar.clicked.connect(self.cerrar)#Asociacion del boton a un método
        
    def cerrar(self):
        self.close()
        
    def variablesConexion(self):
        global hospedador
        global usuario
        global contrasena
        global base_datos
        
        hospedador = self.txthost.text()
        usuario = self.txtusuario.text()
        contrasena = self.txtcontrasena.text()
        base_datos = self.txtBD.text()
        
        self.conexion(hospedador, usuario, contrasena, base_datos)
        
    def conexion(self, hospedador, usuario, contrasena, base_datos):
        try:
            self.con = pymysql.connect(host= hospedador, user= usuario, password=contrasena, db= base_datos)
            
            self.cursor = self.con.cursor()
            QMessageBox.information(self, "Conexion", "Conexion establecida exitosamente")
            #Si la conexion fue exitosa, mostrar la ventana paara las consultas
            self.mostrar_consultas()
        except Exception as error:
            QMessageBox.warning(self,"Error: ", str(error))
            
    def mostrar_consultas(self):
        self.ventana_consultas = QWidget()#instancia
        self.interfaz_consultas = VentanaConsultas()#instancia de la clase de abajo
        self.interfaz_consultas.ventana(self.ventana_consultas)#método de la clase de abajo. Le mandamos como parametro ésta misma ventana
        self.ventana_consultas.show()
        self.close()

class VentanaConsultas(object):#self.interfaz_consultas = VentanaConsultas() object creado con el metodo 'mostrar_consultas'
    def ventana(self, v):
        #creacion de la segunda ventana
        v.setFixedSize(650, 300)
        v.setWindowTitle("Consultas MySQL")
        v.setStyleSheet("background-color: red")
        v.setWindowIcon(QIcon(r"D:\ProgramAvan\Python\qt.png"))
        
        #titulo
        v.lbtitulo = QLabel("¡Proletarios del mundo, uníos!", v)
        v.lbtitulo.setGeometry(QtCore.QRect(150,15,350,25))
        v.lbtitulo.setStyleSheet("background-color: yellow; color: black")
        v.lbtitulo.setFont(QFont("Consolas", 16))
        
        #Botones para los reportes
        v.btnReporte1 = QPushButton("Reporte 1", v)
        v.btnReporte1.setGeometry(100, 70, 200, 100)
        v.btnReporte1.setStyleSheet("background-color: yellow; color: black")
        v.btnReporte1.setFont(QFont("Consolas", 14))
        v.btnReporte1.clicked.connect(ventana_consultas.reporte_uno)
        
        v.btnRporte2 = QPushButton("Reporte 2", v)
        v.btnRporte2.setGeometry(350, 70, 200, 100)
        v.btnRporte2.setStyleSheet("background-color: yellow; color: black")
        v.btnRporte2.setFont(QFont("Consolas", 14))
        v.btnRporte2.clicked.connect(ventana_consultas.reporte_dos)
        
        v.btnReporte3 = QPushButton("Reporte 3", v)
        v.btnReporte3.setGeometry(100, 190, 200, 100)
        v.btnReporte3.setStyleSheet("background-color: yellow; color: black")
        v.btnReporte3.setFont(QFont("Consolas", 14))
        v.btnReporte3.clicked.connect(ventana_consultas.reporte_tres)
        
        v.btnReporte4 = QPushButton("Reporte 4", v)
        v.btnReporte4.setGeometry(350, 190, 200, 100)
        v.btnReporte4.setStyleSheet("background-color: yellow; color: black")
        v.btnReporte4.setFont(QFont("Consolas", 14))
        v.btnReporte4.clicked.connect(ventana_consultas.reporte_cuatro)
        
    def conexion_consultas(v):
        try:
            v.con = pymysql.connect(host = hospedador, user=usuario, password=contrasena, db=base_datos)
            v.cursor = v.con.cursor()
            print("Conexion establecida")
        except Exception as error:
            print(error)
    
    def reporte_uno(v):
        v.conexion_consultas()
        consulta = "SELECT * FROM clientes"
        
        try:
            v.cursor.execute(consulta)
            resultado = v.cursor.fetchall()
            for fila in resultado:
                print(fila)
                
            directorio = os.getcwd()
            print(directorio)
            df = pandas.DataFrame(data=resultado)
            df.to_excel(directorio + "/reporte1.xlsx")
            
            #mandar llamar el aviso
            
        except Exception as error:
            #mandar llamar la alerta
            print(error)
    
    def reporte_dos(v):
        v.conexion_consultas()

        consulta = "SELECT tipo, numero, estatus FROM tarjetas_credito UNION SELECT tipo, numero, estatus FROM tarjetas_debito"

        try:
            v.cursor.execute(consulta)
            resultado = v.cursor.fetchall()
            for fila in resultado:
                print(fila)

            # directorio = os.getcwd()
            # print(directorio)
            df = pandas.DataFrame(data=resultado)
            # df.to_excel(directorio + "/reporte1.xlsx")
            #df.to_csv(r"C:\Users\soporte\Desktop\reporte2.csv")
            df.to_csv(r"D:\ProgramAvan\Python\reporte2.csv")
            # mandar llamar el aviso
            v.aviso()
        except:
            # mandar llamar la alerta
            v.alerta()
    
    def reporte_tres(v):
        v.conexion_consultas()

        consulta = "SELECT * FROM cajeros WHERE estatus = 'ACTIVO'"

        try:
            v.cursor.execute(consulta)
            resultado = v.cursor.fetchall()
            for fila in resultado:
                print(fila)

            # directorio = os.getcwd()
            # print(directorio)
            df = pandas.DataFrame(data=resultado)
            # df.to_excel(directorio + "/reporte1.xlsx")
            df.to_html(r"D:\ProgramAvan\Python\reporte3.html")
            # mandar llamar el aviso
            v.aviso()
        except:
            # mandar llamar la alerta
            v.alerta()

    
    def reporte_cuatro(v):
        v.conexion_consultas()

        consulta = "SELECT * FROM asesores"

        try:
            v.cursor.execute(consulta)
            resultado = v.cursor.fetchall()
            for fila in resultado:
                print(fila)

            # directorio = os.getcwd()
            # print(directorio)
            df = pandas.DataFrame(data=resultado)
            # df.to_excel(directorio + "/reporte1.xlsx")
            df.to_json(r"D:\ProgramAvan\Python\reporte4.json")
            # mandar llamar el aviso
            v.aviso()
        except:
            # mandar llamar la alerta
            v.alerta()
            
    def aviso(v):
        dialogo = QMessageBox()
        dialogo.setWindowTitle("Información")
        dialogo.setText("Reporte generado con exito")
        aceptar = QPushButton("Aceptar")
        dialogo.addButton(aceptar, QMessageBox.YesRole)
        dialogo.setWindowIcon(QIcon(r"D:\ProgramAvan\Python\qt.png"))
        dialogo.setStyleSheet("background-color:black; color:gray")
        dialogo.exec()

    def alerta(v):
        dialogo = QMessageBox()
        dialogo.setWindowTitle("Atención")
        dialogo.setText("Error al generar el reporte")
        aceptar = QPushButton("Aceptar")
        dialogo.addButton(aceptar, QMessageBox.YesRole)
        dialogo.setWindowIcon(QIcon(r"D:\ProgramAvan\Python\qt.png"))
        dialogo.setStyleSheet("background-color:orange; color:black")
        dialogo.exec()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_conexion = VentanaConexion()
    ventana_consultas = VentanaConsultas()
    ventana_conexion.show()
    sys.exit(app.exec())