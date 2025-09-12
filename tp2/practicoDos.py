import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Codigo de Ejercicio 3
import Complementos.ejercicio3 as ej3

class ProcesadorImagenesGUI:
    def __init__(self, master):
        self.master = master
        master.title("Procesador de Imágenes")

        self.imagen1 = None
        self.imagen2 = None

        # Botones
        self.btn_abrir = tk.Button(master, text="Abrir Imagen 1", command=self.abrir_imagen1)
        self.btn_abrir.pack()
        
        self.btn_abrir = tk.Button(master, text="Abrir Imagen 2", command=self.abrir_imagen2)
        self.btn_abrir.pack()

        self.btn_mostrar = tk.Button(master, text="Mostrar Imagenes", command=self.mostrar_imagenes)
        self.btn_mostrar.pack()

        self.btn_mostrar = tk.Button(master, text="Sumar Imagenes (mismas dimensiones)", command=self.sumar_imagenes)
        self.btn_mostrar.pack()

        self.btn_mostrar = tk.Button(master, text="Restar Imagenes (mismas dimensiones)", command=self.restar_imagenes)
        self.btn_mostrar.pack()

        # Botones para ejercicio 3
        self.btn_producto = tk.Button(master, text="Multiplicar Imágenes", command=self.multiplicar_imagenes)
        self.btn_producto.pack()

        self.btn_cociente = tk.Button(master, text="Dividir Imágenes", command=self.dividir_imagenes)
        self.btn_cociente.pack()

    def abrir_imagen1(self):
        ruta_archivo = filedialog.askopenfilename()
        if ruta_archivo:
            try:
                self.imagen1 = imageio.imread(ruta_archivo)
                print(f"Imagen cargada desde: {ruta_archivo}")
            except Exception as e:
                print(f"Error al cargar la imagen: {e}")

    def abrir_imagen2(self):
        ruta_archivo = filedialog.askopenfilename()
        if ruta_archivo:
            try:
                self.imagen2 = imageio.imread(ruta_archivo)
                print(f"Imagen cargada desde: {ruta_archivo}")
            except Exception as e:
                print(f"Error al cargar la imagen: {e}")

    def mostrar_imagenes(self):
        if self.imagen1 is not None and self.imagen2 is not None:
            fig, axs = plt.subplots(1, 2, figsize=(12, 4))
            axs[0].imshow(self.imagen1)
            axs[0].set_title("Imagen 1")
            axs[0].axis('off')
            axs[1].imshow(self.imagen2)
            axs[1].set_title("Imagen 2")
            axs[1].axis('off')
            plt.show()
        else:
            print("No hay imagen/es cargada.")
        
    def sumar_imagenes(self):
        if self.imagen1.shape == self.imagen2.shape:
            suma_clampeada = np.clip(self.imagen1.astype(np.int32) + self.imagen2.astype(np.int32), 0, 255).astype(np.uint8)
            plt.imshow(suma_clampeada)
            plt.title("Suma Clampeada")
            plt.axis('off')
            plt.show()
        else:
            print("Las imágenes no tienen las mismas dimensiones")
    
    def restar_imagenes(self):
        if self.imagen1.shape == self.imagen2.shape:
            suma_clampeada = np.clip(self.imagen1.astype(np.int32) - self.imagen2.astype(np.int32), 0, 255).astype(np.uint8)
            plt.imshow(suma_clampeada)
            plt.title("Resta Clampeada")
            plt.axis('off')
            plt.show()
        else:
            print("Las imágenes no tienen las mismas dimensiones")

    # Funciones para el ejercicio 3
    def multiplicar_imagenes(self):
        if self.imagen1 is not None and self.imagen2 is not None:
            if self.imagen1.shape == self.imagen2.shape:
                # Llama a la función 'producto' del otro archivo
                resultado = ej3.producto(self.imagen1, self.imagen2)
                if resultado is not None:
                    plt.imshow(resultado.astype(np.uint8))
                    plt.title("Producto de Imágenes")
                    plt.axis('off')
                    plt.show()
            else:
                print("Las imágenes deben tener las mismas dimensiones.")
        else:
            print("Cargue ambas imágenes primero.")

    def dividir_imagenes(self):
        if self.imagen1 is not None and self.imagen2 is not None:
            if self.imagen1.shape == self.imagen2.shape:
                # Llama a la función 'cociente' del otro archivo
                resultado = ej3.cociente(self.imagen1, self.imagen2)
                if resultado is not None:
                    # Normaliza el resultado del cociente para la visualización
                    resultado_normalizado = (resultado - resultado.min()) / (resultado.max() - resultado.min())
                    plt.imshow(resultado_normalizado)
                    plt.title("Cociente de Imágenes")
                    plt.axis('off')
                    plt.show()
            else:
                print("Las imágenes deben tener las mismas dimensiones.")
        else:
            print("Cargue ambas imágenes primero.")

root = tk.Tk()
app = ProcesadorImagenesGUI(root)
root.mainloop()