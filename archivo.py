import subprocess as sp
import tkinter as tk 
from tkinter import messagebox as mb
from tkinter import filedialog

#Baner
# Banner
banner = r"""
                    )         (                 )
    )  (         ( /(     (   )\   (         ( /(  
 ( /(  )(    (   )\()) (  )\ ((_) ))\  (     )\()) 
 )(_))(()\   )\ ((_)\  )\((_) _  /((_) )\ ) (_))/
((_)_  ((_) ((_)| |(_)((_)(_)| |(_))  _(_/( | |_
/ _` || '_|/ _| | ' \ (_-<| || |/ -_)| ' \))|  _|
\__,_||_|  \__| |_||_|/__/|_||_|\___||_||_|  \__|

"""

# Definir los comandos a ejecutar
comandos = [
    "whoami",
    "hostname",
    "wmic bios get serialnumber",
    "wmic diskdrive get model, serialnumber",
    "wmic memorychip get devicelocator, serialnumber",
    "wmic memphysical get maxcapacity, memoryDevices",
    "ip config /all"
]

# Crear una ventana de tkinter para seleccionar la ubicación del archivo
root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal

# Mostrar un cuadro de diálogo para seleccionar la ubicación del archivo
ruta_salida = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])

# Verificar si se seleccionó una ubicación de archivo válida
if ruta_salida:
    # Abrir el archivo en modo escritura
    with open(ruta_salida, "w") as archivo:
        # Escribir el banner en el archivo
        archivo.write(banner)

        # Iterar sobre los comandos y ejecutarlos
        for comando in comandos:
            # Agregar una línea al archivo indicando el comando que se está ejecutando
            archivo.write(f"resultado de :{comando}\n")

            # Ejecutar el comando y capturar la salida
            resultado = sp.run(comando, capture_output=True, text=True)

            # Verificar si la ejecución fue exitosa y escribir la salida en el archivo
            if resultado.returncode == 0:
                archivo.write(resultado.stdout)
                archivo.write("\n")
            else:
                archivo.write(f"Error al ejecutar el comando: {comando}\n\n")

    # Mostrar un mensaje indicando que se completó la ejecución
    print(f"Los resultados se han guardado en {ruta_salida}")
else:
    mb.showinfo("aviso", "No se ha seleccionado ninguna direccion para guardar el archivo")
