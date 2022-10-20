#Lunes 5 d septiembre

# pip install pillow
# pip install qrcode

from doctest import master
from gc import isenabled
import sys
import time
from tkinter import EXCEPTION
import pymysql
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtPrintSupport import *

#Importar nustra propia clase
from crearQR import *

# Ajustar la ventana al monitor
# Tamaño de la ventana proporcional al monitor

class VentanaAdministracion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.iniciar()

    def iniciar(self):
        # Ventana
        self.setFixedSize(600,700)
        self.setWindowTitle("Registro de personas")
        self.setStyleSheet("background-color:#1D919F; color:white")
        
        #titulo
        self.titulo = QLabel("Administracion de personas", self)
        self.titulo.setGeometry(QRect(150, 10, 310, 30))
        self.titulo.setStyleSheet("background-color: #000000; color:#00FF2F")
        self.titulo.setFont(QFont("Consolas", 16))
        
        #idpersona
        self.lbidpersona = QLabel("ID persona", self)
        self.lbidpersona.setGeometry(QRect(10, 60, 200, 30))
        self.lbidpersona.setStyleSheet("background-color: #000000; color:#00FF2F")
        self.lbidpersona.setFont(QFont("Consolas", 16))
        
        self.txtidpersona = QLineEdit(self)
        self.txtidpersona.setGeometry(QRect(250, 60, 310, 30))
        self.txtidpersona.setStyleSheet("background-color: #000000; color:#00FF2F")
        self.txtidpersona.setFont(QFont("Consolas", 16))
        self.txtidpersona.setEnabled(False)
        
        #Paterno
        self.lbpaterno = QLabel("Paterno: ", self)
        self.lbpaterno.setGeometry(QRect(10, 95, 200, 30))
        self.lbpaterno.setStyleSheet("background-color: #000000; color:#00FF2F")
        self.lbpaterno.setFont(QFont("Consolas", 16))
        
        self.txtpaterno = QLineEdit(self)
        self.txtpaterno.setGeometry(QRect(250, 95, 310, 30))
        self.txtpaterno.setStyleSheet("background-color: #000000; color:#00FF2F")
        self.txtpaterno.setFont(QFont("Consolas", 16))
        
        #Materno
        self.lbmaterno = QLabel("Materno: ", self)
        self.lbmaterno.setGeometry(QRect(10, 130, 200, 30))
        self.lbmaterno.setStyleSheet("background-color: #000000; color:#00FF2F")
        self.lbmaterno.setFont(QFont("Consolas", 16))
        
        self.txtmaterno = QLineEdit(self)
        self.txtmaterno.setGeometry(QRect(250, 130, 310, 30))
        self.txtmaterno.setStyleSheet("background-color: #000000; color:#00FF2F")
        self.txtmaterno.setFont(QFont("Consolas", 16))
        
        #nombre
        self.lbnombre = QLabel("Nombre: ", self)
        self.lbnombre.setGeometry(QRect(10, 165, 200, 30))
        self.lbnombre.setStyleSheet("background-color: #000000; color:#00FF2F")
        self.lbnombre.setFont(QFont("Consolas", 16))
        
        self.txtnombre = QLineEdit(self)
        self.txtnombre.setGeometry(QRect(250, 165, 310, 30))
        self.txtnombre.setStyleSheet("background-color: #000000; color:#00FF2F")
        self.txtnombre.setFont(QFont("Consolas", 16))
        
        #CURP
        self.lbcurp = QLabel("CURP: ", self)
        self.lbcurp.setGeometry(QRect(10, 200, 200, 30))
        self.lbcurp.setStyleSheet("background-color: #000000; color:#00FF2F")
        self.lbcurp.setFont(QFont("Consolas", 16))
        
        self.txtcurp = QLineEdit(self)
        self.txtcurp.setGeometry(QRect(250, 200, 310, 30))
        self.txtcurp.setStyleSheet("background-color: #000000; color:#00FF2F")
        self.txtcurp.setFont(QFont("Consolas", 16))
        
        #fecha naciminto
        self.lbfecha_nacimiento = QLabel("FEcha nacimiento: ", self)
        self.lbfecha_nacimiento.setGeometry(QRect(10,235, 200, 30))
        self.lbfecha_nacimiento.setStyleSheet("background-color: #000000; color:#00FF2F")
        self.lbfecha_nacimiento.setFont(QFont("Consolas", 16))
        
        self.txtfecha_nacimiento = QLineEdit(self)
        self.txtfecha_nacimiento.setGeometry(QRect(250,235, 310, 30))
        self.txtfecha_nacimiento.setStyleSheet("background-color: #000000; color:#00FF2F")
        self.txtfecha_nacimiento.setFont(QFont("Consolas", 16))
        
        #correo
        self.lbcorreo = QLabel("Correo: ", self)
        self.lbcorreo.setGeometry(QRect(10, 270, 200, 30))
        self.lbcorreo.setStyleSheet("background-color: #000000; color:#00FF2F")
        self.lbcorreo.setFont(QFont("Consolas", 16))
        
        self.txtcorreo = QLineEdit(self)
        self.txtcorreo.setGeometry(QRect(250, 270, 310, 30))
        self.txtcorreo.setStyleSheet("background-color: #000000; color:#00FF2F")
        self.txtcorreo.setFont(QFont("Consolas", 16))
        
        #fecha_registro
        self.lbfecha_registro = QLabel("fecha registro: ", self)
        self.lbfecha_registro.setGeometry(QRect(10, 305, 200, 30))
        self.lbfecha_registro.setStyleSheet("background-color: #000000; color:#00FF2F")
        self.lbfecha_registro.setFont(QFont("Consolas", 16))
        
        self.txtfecha_registro = QLineEdit(self)
        self.txtfecha_registro.setGeometry(QRect(250, 305, 310, 30))
        self.txtfecha_registro.setStyleSheet("background-color: #000000; color:#00FF2F")
        self.txtfecha_registro.setFont(QFont("Consolas", 16))
        self.txtfecha_registro.setEnabled(False)
        
        #rol ------- combobox
        self.lbrol = QLabel("Rol: ", self)
        self.lbrol.setGeometry(QRect(10, 340, 200, 30))
        self.lbrol.setStyleSheet("background-color: #000000; color:#00FF2F")
        self.lbrol.setFont(QFont("Consolas", 16))
        
        #self.txtrol = QLineEdit(self)
        self.cbrol = QComboBox(self)
        self.cbrol.addItem("Administrativo")
        self.cbrol.addItem("Estudiante")
        self.cbrol.addItem("Profesor")
        self.cbrol.addItem("Otro")
        self.cbrol.setGeometry(QRect(250, 340, 310, 30))
        self.cbrol.setStyleSheet("background-color: #000000; color:#00FF2F")
        self.cbrol.setFont(QFont("Consolas", 16))
        
        #qr
        self.lbqr = QLabel("QR: ", self)
        self.lbqr.setGeometry(QRect(10, 375, 200, 30))
        self.lbqr.setStyleSheet("background-color: #000000; color:#00FF2F")
        self.lbqr.setFont(QFont("Consolas", 16))
        
        self.txtqr = QLineEdit(self)
        self.txtqr.setGeometry(QRect(250, 375, 310, 30))
        self.txtqr.setStyleSheet("background-color: #000000; color:#00FF2F")
        self.txtqr.setFont(QFont("Consolas", 16))
        
        #BOTONES
        self.btnregistrar = QPushButton("Registrar", self)
        self.btnregistrar.setGeometry(QRect(10,430,130,50))
        self.btnregistrar.setStyleSheet("background-color: #D2DEDE; color:#000000")
        self.btnregistrar.setFont(QFont("Consolas", 16))
        self.btnregistrar.clicked.connect(self.variables_registrar)
        
        self.btneliminar = QPushButton("Eliminar", self)
        self.btneliminar.setGeometry(QRect(150,430,130,50))
        self.btneliminar.setStyleSheet("background-color: #D2DEDE; color:#000000")
        self.btneliminar.setFont(QFont("Consolas", 16))
        self.btneliminar.clicked.connect(self.variable_eliminar)
        
        self.btnactualizar = QPushButton("Buscar", self)
        self.btnactualizar.setGeometry(QRect(290,430,130,50))
        self.btnactualizar.setStyleSheet("background-color: #D2DEDE; color:#000000")
        self.btnactualizar.setFont(QFont("Consolas", 16))
        self.btnactualizar.clicked.connect(self.buscar_persona)
        
        self.btnlimpiar = QPushButton("Limpiar", self)
        self.btnlimpiar.setGeometry(QRect(430,430,130,50))
        self.btnlimpiar.setStyleSheet("background-color: #D2DEDE; color:#000000")
        self.btnlimpiar.setFont(QFont("Consolas", 16))
        self.btnlimpiar.clicked.connect(self.limpiar)

        '''
        # Imagen GIF
        self.lbgif = QLabel(self)
        self.lbgif.setGeometry(10,10,450,210)
        self.lbgif.setStyleSheet("background-color:red")
        self.gif = QMovie(r"D:\ProgramAvan\Python\qr.gif")
        self.lbgif.setMovie(self.gif)
        self.gif.start()
        '''
        
    def prueba(self):
        crearqr = CrearQR()
        crearqr.crear_qr()

    def conexion(self):
        try:
            self.con = pymysql.connect(host="localhost", user="root", password="root", db="administracion")
            self.cursor = self.con.cursor()
            QMessageBox.information(self, "Conexion", "Conexion establecida exitosamente")
            
        except Exception as error:
            QMessageBox.warning(self, "atencion", str(error))
        
        
    def variables_registrar(self):
        global paterno, materno, nombre, curp, fecha_nacimiento,correo,fecha_registro, rol, qr
        
        #guardar los valores de cada qlineEdit en sus variables
        paterno = self.txtpaterno.text()
        materno = self.txtmaterno.text()
        nombre = self.txtnombre.text()
        curp = self.txtcurp.text()
        fecha_nacimiento = self.txtfecha_nacimiento.text()
        correo = self.txtcorreo.text()
        fecha_registro =time.strftime("%c")#--------fecha del sistema
        self.txtfecha_registro.setText(str(fecha_registro))#------
        rol = self.cbrol.currentText().upper()
        qr = rol + "-" + curp.upper()
        
        #Enviar el valor de QR a la caja de texto
        self.txtqr.setText(qr)
        
        #mandar llamar el metodo que gener el QR
        crearqr = CrearQR()
        crearqr.crear_qr(rol, curp.upper())
        
        self.registrar(paterno, materno, nombre, curp, fecha_nacimiento,correo,fecha_registro, rol, qr)
        
    def registrar(self, paterno, materno, nombre, curp, fecha_nacimiento,correo,fecha_registro, rol, qr):
        self.conexion()
        registro = "INSERT INTO personas(paterno, materno, nombre, curp, fecha_nacimiento,correo,fecha_registro, rol, qr) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}',)".format(paterno, materno, nombre, curp, fecha_nacimiento,correo,fecha_registro, rol, qr)
        
        try:
            self.cursor.execute(registro)
            self.con.commit()
            QMessageBox.information(self,"REGISTRO", "registro realizado exitosamente")
        except EXCEPTION as error:
            QMessageBox.warning(self,"ERROR", str(error))
            
    def variable_eliminar(self):
        global idpersona
        
        #si la caja de texto está habilitada
        if self.txtidpersona.isEnabled() == True:
            idpersona = self.txtidpersona.text()
            self.eliminar(idpersona)
        else:
            self.txtidpersona.setEnabled(True)
            QMessageBox.information(self, "Aviso", "Capture el ID del registro a eliminar")
    
    def eliminar(self, idpersona):
        self.conexion()
        eliminar = "SELECT * FROM personas WHERE idpersona = '{}'".format(idpersona)
        
        try:
            #Validar que exista el ID
            self.cursor.execute(eliminar)
            eliminar = self.cursor.fetchone()
            print(eliminar)
            if eliminar == None:
                QMessageBox.warning(self, "ATENCION", "El ID ingresado no existe")
            else:
                eliminar = "DELETE FROM personas WHERE idpersona = '{}'".format(idpersona)    
                self.cursor.execute(eliminar)
                self.con.commit()
                QMessageBox.information(self, "ELIMINACION", "REgistro eliminado correctamente")
        except EXCEPTION as error:
            QMessageBox.warning(self, "ERROR", str(error))#error es un objeto que transformamos en string
    
    def buscar_persona(self):
        if self.txtidpersona.isEnabled() == True and self.btnactualizar.text() == "Buscar":
            idpersona = self.txtidpersona.text()
            self.datos_persona(idpersona)
            self.btnactualizar.setText("Actualizar")
        elif self.btnactualizar.text() == "Actualizar":
            self.variables_actualizar()
            self.btnactualizar.setText("Buscar")
        elif self.txtidpersona.isEnabled() == False and self.btnactualizar.text() == "Buscar":
            self.txtidpersona.setEnabled(True)
            QMessageBox.information(self, "AVISO", "capture el ID del registro a buscar")
        else:
            QMessageBox.information(self, "AVISO", "Revisar las condiciones")
            
    
    def datos_persona(self):
        self.conexion()
        datos = "SELECT * FROM personas WHERE idpersona = '{}'".format(idpersona)
        
        try:
            self.cursor.execute(datos)
            datos = self.cursor.fetchone()
            
            self.txtpaterno.setText(datos[1])
            self.txtmaterno.setText(datos[2])
            self.txtnombre.setText(datos[3])
            self.txtcurp.setText(datos[4])
            self.txtfecha_nacimiento.setText(datos[5])
            self.txtcorreo.setText(datos[6])
            self.txtfecha_registro.setText(datos[7])
            self.cbrol.setCurrentIndex(0)#datos[8]
            self.txtqr.setText(datos[9])
            
        except Exception as error:
            QMessageBox.warning(self, "ERROR", str(error))
    
    def variables_actualizar(self):
        pass
    
    def actualizar_persona(self):
        pass
    
    def limpiar(self):
        self.txtpaterno.setText("")
        self.txtmaterno.setText("")
        self.txtnombre.setText("")
        self.txtcurp.setText("")
        self.txtfecha_nacimiento.setText("")
        self.txtcorreo.setText("")
        self.txtfecha_registro.setText("")
        self.cbrol.setCurrentIndex(0)#para combobox
        self.txtqr.setText("")
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    vadministracion = VentanaAdministracion()
    vadministracion.show()
    sys.exit(app.exec())