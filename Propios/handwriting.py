import pywhatkit as kit
from PIL import Image

#input a convertir
texto_convertir = input("TExto a convertir: ")

#convertir el texto introducido
kit.text_to_handwriting(texto_convertir, save_to="a_mano.png")

#abrir imagen
Image.open("Propios/a_mano.png", mode='r').show()