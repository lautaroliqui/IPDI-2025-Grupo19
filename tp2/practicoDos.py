import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
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

# Ejercicio 4

def resta_valor_absoluto(img1, img2):
    # Asegurarse de que las imágenes tengan las mismas dimensiones
    if img1.shape == img2.shape:
        # Calcular la resta y luego el valor absoluto
        diferencia = np.abs(img1.astype(np.int32) - img2.astype(np.int32))
        return diferencia.astype(np.uint8)
    else:
        print("Las imágenes deben tener las mismas dimensiones.")
        return None

# Ejercicio 5

def if_darker(img1, img2):
    """
    Compara dos imágenes píxel a píxel y devuelve la más oscura.
    """
    if img1.shape != img2.shape:
        print("Las imágenes deben tener las mismas dimensiones.")
        return None
    
    # np.minimum compara los elementos de dos arrays y devuelve el mínimo
    resultado = np.minimum(img1, img2)
    return resultado

def if_lighter(img1, img2):
    """
    Compara dos imágenes píxel a píxel y devuelve la más clara.
    """
    if img1.shape != img2.shape:
        print("Las imágenes deben tener las mismas dimensiones.")
        return None
    
    # np.maximum compara los elementos de dos arrays y devuelve el máximo
    resultado = np.maximum(img1, img2)
    return resultado

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

        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(8, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack()
        self.ax1.axis('off')
        self.ax2.axis('off')

        frame_rgb = tk.LabelFrame(master, text="Suma y Resta Clampeada (Misma Dimensión)")
        frame_rgb.pack(padx=10, pady=10, fill="x")

        tk.Button(frame_rgb, text="Sumar", command=self.sumar_imagenes).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(frame_rgb, text="Restar", command=self.restar_imagenes).grid(row=0, column=1, padx=5, pady=5)

        frame_yiq = tk.LabelFrame(master, text="Suma y Resta Clampeada YIQ")
        frame_yiq.pack(padx=10, pady=10, fill="x")

        tk.Button(frame_yiq, text="Sumar", command=self.sumar_imagenes_yiq).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(frame_yiq, text="Restar", command=self.restar_imagenes_yiq).grid(row=0, column=1, padx=5, pady=5)

        frame_extra = tk.LabelFrame(master, text="Operaciones Extras")
        frame_extra.pack(padx=10, pady=10, fill="x")

        tk.Button(frame_extra, text="Multiplicar", command=self.multiplicar_imagenes).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(frame_extra, text="Dividir", command=self.dividir_imagenes).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(frame_extra, text="Resta Absoluta", command=self.resta_absoluta).grid(row=0, column=2, padx=5, pady=5)

        frame_extra = tk.LabelFrame(master, text="Operaciones If-darker y If-lighter")
        frame_extra.pack(padx=10, pady=10, fill="x")

        self.btn_if_darker = tk.Button(frame_extra, text="'If-darker'", command=self.if_darker_op).grid(row=0, column=0, padx=5, pady=5)
        # self.btn_if_darker.pack()

        self.btn_if_lighter = tk.Button(frame_extra, text="'If-lighter'", command=self.if_lighter_op).grid(row=0, column=1, padx=5, pady=5)
        # self.btn_if_lighter.pack()

    # En la clase ProcesadorImagenesGUI
    def abrir_imagen1(self):
        ruta_archivo = filedialog.askopenfilename()
        if ruta_archivo:
            try:
                self.imagen1 = imageio.imread(ruta_archivo)
                print(f"Imagen cargada desde: {ruta_archivo}")
                self.ax1.clear()
                self.ax1.imshow(self.imagen1)
                self.ax1.set_title("Imagen 1")
                self.ax1.axis('off')
                self.canvas.draw()
            except Exception as e:
                print(f"Error al cargar la imagen: {e}")

    def abrir_imagen2(self):
        ruta_archivo = filedialog.askopenfilename()
        if ruta_archivo:
            try:
                self.imagen2 = imageio.imread(ruta_archivo)
                print(f"Imagen cargada desde: {ruta_archivo}")
                self.ax2.clear()
                self.ax2.imshow(self.imagen2)
                self.ax2.set_title("Imagen 2")
                self.ax2.axis('off')
                self.canvas.draw()
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

    # Funciones para el ejercicio 4
    def resta_absoluta(self):
        if self.imagen1 is not None and self.imagen2 is not None:
            if self.imagen1.shape == self.imagen2.shape:
                # Llama a la función 'resta_valor_absoluto' del otro archivo
                resultado = resta_valor_absoluto(self.imagen1, self.imagen2)
                if resultado is not None:
                    plt.imshow(resultado)
                    plt.title("Resta con Valor Absoluto")
                    plt.axis('off')
                    plt.show()
            else:
                print("Las imágenes deben tener las mismas dimensiones.")
        else:
            print("Cargue ambas imágenes primero.")
    
    # Funciones para el ejercicio 5
    def if_darker_op(self):
        if self.imagen1 is not None and self.imagen2 is not None:
            resultado = if_darker(self.imagen1, self.imagen2)
            if resultado is not None:
                plt.imshow(resultado)
                plt.title("Operación 'If-darker'")
                plt.axis('off')
                plt.show()
        else:
            print("Cargue ambas imágenes primero.")

    def if_lighter_op(self):
        if self.imagen1 is not None and self.imagen2 is not None:
            resultado = if_lighter(self.imagen1, self.imagen2)
            if resultado is not None:
                plt.imshow(resultado)
                plt.title("Operación 'If-lighter'")
                plt.axis('off')
                plt.show()
        else:
            print("Cargue ambas imágenes primero.")


root = tk.Tk()
app = ProcesadorImagenesGUI(root)
root.mainloop()