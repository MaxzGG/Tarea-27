#Maximiliano Gómez Guevara
#2177546

import subprocess
import re

# Puertos estándar considerados
PUERTOS_ESTANDAR = {22, 25, 80, 465, 587, 8080}

# Función para ejecutar el script de Bash
def ejecutar_script_bash():
    try:
        resultado = subprocess.run(['./monitor_conexiones.sh'], capture_output=True, text=True)
        resultado.check_returncode()  # Verifica si hubo un error en la ejecución
        return resultado.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el script de Bash: {e}")
        print(f"Salida estándar: {e.stdout}")
        print(f"Error estándar: {e.stderr}")
        return None

# Función para analizar las conexiones
def analizar_conexiones(salida_bash):
    conexiones_sospechosas = []
    # Expresión regular para extraer la dirección IP y puerto
    patron = re.compile(r'(\d+\.\d+\.\d+\.\d+):(\d+)\s+.*\s+(\d+\.\d+\.\d+\.\d+):(\d+)')
    
    for linea in salida_bash.splitlines():
        match = patron.search(linea)
        if match:
            ip_origen, puerto_origen, ip_destino, puerto_destino = match.groups()
            puerto_origen = int(puerto_origen)
            puerto_destino = int(puerto_destino)
            
            # Verificar si alguno de los puertos no es estándar
            if puerto_origen not in PUERTOS_ESTANDAR and puerto_destino not in PUERTOS_ESTANDAR:
                conexiones_sospechosas.append(linea)
    
    return conexiones_sospechosas

# Función para generar el reporte
def generar_reporte(conexiones_sospechosas):
    with open('reporte_conexiones_sospechosas.txt', 'w') as archivo:
        archivo.write("Conexiones sospechosas:\n")
        for conexion in conexiones_sospechosas:
            archivo.write(conexion + '\n')

# Ejecución del script
salida_bash = ejecutar_script_bash()
if salida_bash:
    conexiones_sospechosas = analizar_conexiones(salida_bash)
    if conexiones_sospechosas:
        generar_reporte(conexiones_sospechosas)
        print("Reporte generado con éxito.")
    else:
        print("No se encontraron conexiones sospechosas.")
else:
    print("No se pudo analizar la salida del script de Bash.")
