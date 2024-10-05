# monitor_servicios.ps1
# Obtener información de los servicios del sistema y exportar a CSV

Get-Service | Select-Object Name, DisplayName, Status, StartType |
Export-Csv -Path "D:\Programacion Clase\t27\servicios.csv" -NoTypeInformation -Encoding UTF8