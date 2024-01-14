import subprocess
import tkinter as tk
from tkinter import filedialog

# Definir el banner
banner = """
*********************************************
*                                           *
*          Información del sistema          *
*                                           *
*********************************************
\n
"""

# Definir los comandos a ejecutar
comandos = [
    "wmic bios get serialnumber",
    "wmic diskdrive get model, serialnumber",
    "wmic memorychip get devicelocator, serialnumber",
    "wmic memphysical get maxcapacity, memoryDevices"
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
            archivo.write(f"Resultados del comando: {comando}\n\n")

            # Ejecutar el comando y capturar la salida
            resultado = subprocess.run(comando, capture_output=True, text=True)

            # Verificar si la ejecución fue exitosa y escribir la salida en el archivo
            if resultado.returncode == 0:
                archivo.write(resultado.stdout)
                archivo.write("\n\n")
            else:
                archivo.write(f"Error al ejecutar el comando: {comando}\n\n")

    # Mostrar un mensaje indicando que se completó la ejecución
    print(f"Los resultados se han guardado en {ruta_salida}")
else:
    print("No se seleccionó ninguna ubicación para guardar el archivo.")
