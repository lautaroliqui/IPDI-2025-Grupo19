import numpy as np
import matplotlib.pyplot as plt
import imageio

def MostrarImagen():
    img = imageio.imread('C:\\Users\\epere\\PROGRAMACION\\Introduccion a Imagenes\\imagenes\\titocaldern-zq4a.png')  #Direccion de imagen
    plt.imshow(img)
    plt.axis('off')
    plt.show()

def ModificarImagen():
    img = imageio.imread('C:\\Users\\epere\\PROGRAMACION\\Introduccion a Imagenes\\imagenes\\titocaldern-zq4a.png')
    modificada = img.copy()
    modificada[:, :, 0] = np.clip(modificada[:, :, 0] + 100, 0, 255)
    plt.imshow(modificada)
    plt.axis('off')
    plt.show()

def MostrarComponentes():
    img = imageio.imread('C:\\Users\\epere\\PROGRAMACION\\Introduccion a Imagenes\\imagenes\\titocaldern-zq4a.png')
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

def AumentarBrilloCanalRojo():
    img = imageio.imread('C:\\Users\\epere\\PROGRAMACION\\Introduccion a Imagenes\\imagenes\\titocaldern-zq4a.png')
    fig, ax = plt.subplots()
    modificada = img.copy()
    modificada[:, :, 0] = np.clip(modificada[:, :, 0] + 80, 0, 255)
    plt.imshow(modificada)
    ax.set_title('Componente Roja Aumentada')
    plt.axis('off')
    plt.show()

