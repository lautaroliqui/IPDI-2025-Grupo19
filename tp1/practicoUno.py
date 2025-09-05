import numpy as np
import matplotlib.pyplot as plt
import imageio
import os
import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

IMAGEN_PATH = os.path.join(".\\IPDI-2025-Grupo19\\tp1\\imagenes", "titocaldern-zq4a.png")

class ProcesadorImagenesGUI:
    def __init__(self, master):
        self.master = master
        master.title("Procesador de Imágenes")

        # Variables para la imagen
        self.imagen_original = None
        self.imagen_modificada = None

        # Botones de la interfaz
        self.btn_abrir = tk.Button(master, text="Abrir Imagen", command=self.abrir_imagen)
        self.btn_abrir.pack()

        self.btn_mostrar = tk.Button(master, text="Mostrar Imagen", command=self.mostrar_imagen)
        self.btn_mostrar.pack()
        
        self.btn_modificar = tk.Button(master, text="Modificar Imagen", command=self.modificar_imagen_gui)
        self.btn_modificar.pack()
        
        self.btn_componentes = tk.Button(master, text="Mostrar Componentes", command=self.mostrar_componentes_gui)
        self.btn_componentes.pack()
        
        self.btn_guardar = tk.Button(master, text="Guardar Imagen", command=self.guardar_imagen_gui)
        self.btn_guardar.pack()

    def abrir_imagen(self):
        # Abre un cuadro de diálogo para que el usuario elija un archivo
        ruta_archivo = filedialog.askopenfilename()
        if ruta_archivo:
            try:
                self.imagen_original = imageio.imread(ruta_archivo)
                print(f"Imagen cargada desde: {ruta_archivo}")
            except Exception as e:
                print(f"Error al cargar la imagen: {e}")

    def mostrar_imagen(self):
        if self.imagen_original is not None:
            fig, ax = plt.subplots()
            ax.imshow(self.imagen_original)
            ax.set_title("Imagen Original")
            ax.axis('off')
            plt.show()
        else:
            print("No hay imagen cargada.")

    def modificar_imagen_gui(self):
        if self.imagen_original is not None:
            self.imagen_modificada = self.imagen_original.copy()
            self.imagen_modificada[:, :, 0] = np.clip(self.imagen_modificada[:, :, 0] + 100, 0, 255)
            fig, ax = plt.subplots()
            ax.imshow(self.imagen_modificada)
            ax.set_title('Imagen Modificada')
            ax.axis('off')
            plt.show()
        else:
            print("No hay imagen cargada para modificar.")

    def mostrar_componentes_gui(self):
        if self.imagen_original is not None:
            rojo = self.imagen_original[:, :, 0]
            verde = self.imagen_original[:, :, 1]
            azul = self.imagen_original[:, :, 2]
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
            axs[3].imshow(self.imagen_original)
            axs[3].set_title("Original")
            axs[3].axis('off')
            plt.show()
        else:
            print("No hay imagen cargada para mostrar sus componentes.")

    def guardar_imagen_gui(self):
        if self.imagen_modificada is not None:
            ruta_guardado = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
            if ruta_guardado:
                imageio.imwrite(ruta_guardado, self.imagen_modificada)
                print(f"Imagen guardada en: {ruta_guardado}")
        else:
            print("No hay una imagen modificada para guardar.")

root = tk.Tk()
app = ProcesadorImagenesGUI(root)
root.mainloop()