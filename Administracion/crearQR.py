# Martes 6 de septiembre

import qrcode, sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtPrintSupport import *

class CrearQR(QMainWindow):
    def __init__(self):
        super(CrearQR, self).__init__()
        
    def crear_qr(self, rol, curp):
        #print("Sí entro al metodo crear_qr de la clase CrearQR")
        #creacion del objeto de tipo qrcode
        try:
        
            qr = qrcode.QRCode(error_correction = qrcode.constants.ERROR_CORRECT_H)
            
            #llenamos de datos el codigo QR
            codigo = rol + "-" + curp
            qr.add_data(codigo)
            qr.make()
            
            #le asignamos color al codigo QR y a su fondo
            color = "black"
            fondo = "white"
            
            #agregamos nuestra imagen al codigo QR
            qr_img = qr.make_image(fill_color = color, back_color = fondo).convert("RGB")
            
            #Guardar la imagen QR en ell directorio correspondiente
            if rol == "ADMINISTRATIVO":
                qr_img.save(f"D:\ProgramAvan\Python\Administracion\ADMINISTRATIVO\{codigo}.png")
            elif rol == "ESTUDIANTE":
                qr_img.save(f"D:\ProgramAvan\Python\Administracion\ESTUDIANTE\{codigo}.png")
            elif rol == "PROFESOR":
                qr_img.save(f"D:\ProgramAvan\Python\Administracion\PROFESOR\{codigo}.png")
            else:
                qr_img.save(f"D:\ProgramAvan\Python\Administracion\OTRO\{codigo}.png")
                
            QMessageBox.information(self, "Credencial QR", f"Se ha generado el QR exitosamente: {codigo}")
            
        except Exception as error:
            print(error)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    crearqr = CrearQR()
    app.exec()