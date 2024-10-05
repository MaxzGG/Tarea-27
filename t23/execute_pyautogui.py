import pyautogui    
import subprocess  
import datetime     
import os          
def capturar_pantalla():
    try:
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nombre_imagen = f"captura_{fecha_hora}.png"
        captura = pyautogui.screenshot()
        captura.save(nombre_imagen)
        print(f"Captura de pantalla guardada como: {nombre_imagen}")
    except Exception as e:
        print(f"Error al capturar la pantalla: {e}")

def listar_procesos():
    try:
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nombre_archivo = f"procesos_{fecha_hora}.txt"
        resultado = subprocess.run("tasklist", capture_output=True, text=True, shell=True)
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(resultado.stdout)
        print(f"Lista de procesos guardada como: {nombre_archivo}")
    except Exception as e:
        print(f"Error al listar los procesos: {e}")

def main():
    try:
        print("Iniciando captura de pantalla y registro de procesos...")
        capturar_pantalla() 
        listar_procesos()  
        print("Tarea completada.")
    except Exception as e:
        print(f"Ha ocurrido un error durante la ejecución: {e}")

if __name__ == "__main__":
    main()