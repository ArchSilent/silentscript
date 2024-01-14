import subprocess as sp
import tkinter as tk 
from tkinter import messagebox as mb
from tkinter import filedialog


# Banner
banner = r"""
 ________  ________  ________  ___  ___  ________  ___  ___       _______   ________   _________   
|\   __  \|\   __  \|\   ____\|\  \|\  \|\   ____\|\  \|\  \     |\  ___ \ |\   ___  \|\___   ___\ 
\ \  \|\  \ \  \|\  \ \  \___|\ \  \\\  \ \  \___|\ \  \ \  \    \ \   __/|\ \  \\ \  \|___ \  \_| 
 \ \   __  \ \   _  _\ \  \    \ \   __  \ \_____  \ \  \ \  \    \ \  \_|/_\ \  \\ \  \   \ \  \  
  \ \  \ \  \ \  \\  \\ \  \____\ \  \ \  \|____|\  \ \  \ \  \____\ \  \_|\ \ \  \\ \  \   \ \  \ 
   \ \__\ \__\ \__\\ _\\ \_______\ \__\ \__\____\_\  \ \__\ \_______\ \_______\ \__\\ \__\   \ \__\
    \|__|\|__|\|__|\|__|\|_______|\|__|\|__|\_________\|__|\|_______|\|_______|\|__| \|__|    \|__|
                                           \|_________|                                            
                                                                                                   
                                                                                                   

"""

# Definir los comandos a ejecutar
comandos = [
    "wmic bios get serialnumber",
    "systeminfo",
    "wmic diskdrive get model, serialnumber",
    "wmic memorychip get devicelocator, serialnumber",
    "wmic memphysical get maxcapacity, memoryDevices",
]

# Crear una ventana de tkinter para seleccionar la ubicación del archivo
root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal

# Cuadro de diálogo para seleccionar la ubicación del archivo
ruta_salida = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])

# Verificar si se seleccionó una ubicación de archivo válida
if ruta_salida:
    # Abrir el archivo en modo escritura
    with open(ruta_salida, "w") as archivo:
        # Escribir el banner en el archivo
        archivo.write(banner)

        # Iteracion de comandos y ejecutarlos
        for comando in comandos:
            # Agregar una línea al archivo indicando el comando que se está ejecutando
            archivo.write(f"{comando}\n")

            # Ejecutar el comando y capturar la salida
            resultado = sp.run(comando, capture_output=True, text=True)

            # Verificar si la ejecución fue exitosa y escribir la salida en el archivo
            if resultado.returncode == 0:
                archivo.write(resultado.stdout)
                archivo.write("\n")
            else:
                archivo.write(f"Error al ejecutar el comando: {comando}\n\n")

    # Mensaje que indica donde se ha guardado el archivo
    aviso = f"Los resultados se han guardado en: {ruta_salida}"
    mb.showinfo("info", aviso)
    
else:
    # Mensaje que infica que no se ha seleccionado la direccion/ruta para guardar el archivo
    mb.showinfo("aviso", "No se ha seleccionado ninguna direccion para guardar el archivo")
