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

def RGB_to_YIQ(rgb):
    yiq = np.zeros(rgb.shape)
    yiq[:,:,0] = 0.229*rgb[:,:,0] + 0.587*rgb[:,:,1] + 0.114*rgb[:,:,2]
    yiq[:,:,1] = 0.595716*rgb[:,:,0] - 0.274453*rgb[:,:,1] - 0.321263*rgb[:,:,2]
    yiq[:,:,2] = 0.211456*rgb[:,:,0] - 0.522591*rgb[:,:,1] + 0.311135*rgb[:,:,2]
    return yiq

def suma_imagenes(img1, img2, titulo):
    if img1.shape == img2.shape:
        suma_clampeada = np.clip(img1.astype(np.int32) + img2.astype(np.int32), 0, 255).astype(np.uint8)
        plt.imshow(suma_clampeada)
        plt.title(titulo)
        plt.axis('off')
        plt.show()
    else:
        print("Las imágenes deben tener las mismas dimensiones.")

def resta_imagenes(img1, img2, titulo):
    if img1.shape == img2.shape:
        resta_clampeada = np.clip (img1.astype(np.int32) - img2.astype(np.int32), 0, 255).astype(np.uint8)
        plt.imshow(resta_clampeada)
        plt.title(titulo)
        plt.axis('off')
        plt.show()
    else:
        print("Las imágenes deben tener las mismas dimensiones.")

class ProcesadorImagenesGUI:
    def __init__(self, master):
        self.master = master
        master.title("Procesador de Imágenes")

        self.imagen1 = None
        self.imagen2 = None

        frame_cargar = tk.LabelFrame(master, text="Cargar Imágenes")
        frame_cargar.pack(padx=10, pady=10, fill="x")

        self.btn_abrir1 = tk.Button(frame_cargar, text="Abrir Imagen 1", command=self.abrir_imagen1)
        self.btn_abrir1.pack(side=tk.LEFT, padx=5)

        self.btn_abrir2 = tk.Button(frame_cargar, text="Abrir Imagen 2", command=self.abrir_imagen2)
        self.btn_abrir2.pack(side=tk.LEFT, padx=5)

        frame_rgb = tk.LabelFrame(master, text="Suma y Resta Clampeada (Misma Dimensión)")
        frame_rgb.pack(padx=10, pady=10, fill="x")

        tk.Button(frame_rgb, text="Sumar", command=self.sumar_imagenes).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(frame_rgb, text="Restar", command=self.restar_imagenes).grid(row=0, column=1, padx=5, pady=5)

        frame_yiq = tk.LabelFrame(master, text="Suma y Resta Clampeada YIQ")
        frame_yiq.pack(padx=10, pady=10, fill="x")

        tk.Button(frame_yiq, text="Sumar", command=self.sumar_imagenes_yiq).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(frame_yiq, text="Restar", command=self.restar_imagenes_yiq).grid(row=0, column=1, padx=5, pady=5)

        frame_extra = tk.LabelFrame(master, text="Operaciones Extra")
        frame_extra.pack(padx=10, pady=10, fill="x")

        tk.Button(frame_extra, text="Multiplicar", command=self.multiplicar_imagenes).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(frame_extra, text="Dividir", command=self.dividir_imagenes).grid(row=0, column=1, padx=5, pady=5)

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
            print('Carque ambas imágenes primero.') 

    # Funciones para el ejercicio 1
    def sumar_imagenes(self):
        if self.imagen1 is not None and self.imagen2 is not None:
            suma_imagenes(self.imagen1, self.imagen2, 'Suma Clampeada')
        else:
            print('Carque ambas imágenes primero.')
    
    def restar_imagenes(self):
        if self.imagen1 is not None and self.imagen2 is not None:
            resta_imagenes(self.imagen1, self.imagen2, 'Resta Clampeada')
        else:
            print('Carque ambas imágenes primero.')

    # Funciones para el ejercicio 2
    def sumar_imagenes_yiq (self):
        if self.imagen1 is not None and self.imagen2 is not None:
            imagen1 = RGB_to_YIQ(self.imagen1)
            imagen2 = RGB_to_YIQ(self.imagen2)
            suma_imagenes(imagen1, imagen2, 'Suma Clampeada YIQ')
        else:
            print('Carque ambas imágenes primero.')

    def restar_imagenes_yiq (self):
        if self.imagen1 is not None and self.imagen2 is not None:
            imagen1 = RGB_to_YIQ(self.imagen1)
            imagen2 = RGB_to_YIQ(self.imagen2)
            resta_imagenes(imagen1, imagen2, 'Resta Clampeada YIQ')
        else:
            print('Carque ambas imágenes primero.')

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