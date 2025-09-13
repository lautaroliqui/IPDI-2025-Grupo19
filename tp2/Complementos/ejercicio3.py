import numpy as np

def producto(imagen1, imagen2):
    # Asegúrate de que las imágenes tengan el mismo tamaño
    if imagen1.shape == imagen2.shape:
        # El producto de píxeles se puede hacer directamente
        resultado_producto = imagen1 * imagen2
        return resultado_producto
    else:
        print("Las imágenes deben tener las mismas dimensiones.")
        return None

def cociente(imagen1, imagen2):
    # Evitar la división por cero
    imagen2[imagen2 == 0] = 1 # Reemplaza los píxeles con valor 0 para evitar la división por cero
    if imagen1.shape == imagen2.shape:
        # Realiza la división
        resultado_cociente = imagen1 / imagen2
        return resultado_cociente
    else:
        print("Las imágenes deben tener las mismas dimensiones.")
        return None