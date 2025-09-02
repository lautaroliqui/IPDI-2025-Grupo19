import numpy as np
import matplotlib.pyplot as plt
import imageio
import os

IMAGEN_PATH = os.path.join(".\\IPDI-2025-Grupo19\\tp1\\imagenes", "titocaldern-zq4a.png")

def mostrarImagen(imagen):
    img = imageio.imread(imagen)
    plt.imshow(img)
    plt.axis('off')
    plt.show()

def guardarImagen(imagen, nombre_archivo):
    imageio.imwrite(nombre_archivo, imagen)

def modificarImagen(imagen):
    img = imageio.imread(imagen)
    modificada = img.copy()
    modificada[:, :, 0] = np.clip(modificada[:, :, 0] + 100, 0, 255)
    guardarImagen(modificada, ".\\IPDI-2025-Grupo19\\tp1\\imagenes\\imagen_modificada.png")
    plt.imshow(modificada)
    plt.axis('off')
    plt.show()

def mostrarComponentes(imagen):
    img = imageio.imread(imagen)
    rojo = img[:, :, 0]
    verde = img[:, :, 1]
    azul = img[:, :, 2]
    fig, axs = plt.subplots(1, 4, figsize=(12, 4))
    axs[0].imshow(rojo, cmap="gray")
    axs[0].set_title("Componente Roja")
    axs[0].axis('off')
    axs[1].imshow(verde, cmap="gray")
    axs[1].set_title("Componente Verde")
    axs[1].axis('off')
    axs[2].imshow(azul, cmap="gray")
    axs[2].set_title("Componente Azul")
    axs[2].axis('off')
    axs[3].imshow(img)
    axs[3].set_title("Original")
    axs[3].axis('off')
    plt.show()

def aumentarBrilloCanalRojo(imagen):
    img = imageio.imread(imagen)
    fig, ax = plt.subplots()
    modificada = img.copy()
    modificada[:, :, 0] = np.clip(modificada[:, :, 0] + 80, 0, 255)
    plt.imshow(modificada)
    ax.set_title('Componente Roja Aumentada')
    plt.axis('off')
    plt.show()

modificarImagen(IMAGEN_PATH)
