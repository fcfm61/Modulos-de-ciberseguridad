import subprocess
import logging
import argparse
logging.basicConfig(filename='Registros_Uso.log', level=logging.INFO)
def process_history():#Realizada por Jorge Diaz
    print("Obteniendo historial de procesos.....")
    param1=input("Introduzca el día del que se quiera obtener el historial de los procesos:\nFormato(AAAA/MM/DD)\n")
    logging.info("Fecha ingresada: " + str(param1))
    try:
        LinPS="powershell -Executionpolicy Bypass -File Historial_procesos.ps1 -fecha " + param1 
        runimp=subprocess.run(LinPS, capture_output=True, text=True)
        print("El historial se a generado con exito")
        print(runimp.stdout)
        logging.info("Historial generado con exito")
    except Exception as e:
        print(f"A ocurrido un error: {e}")
        logging.error("A ocurrido un error al querer generar el historial de procesos: " + str(e))
        
def Netad_scan():#Realizada por Jorge Diaz
    print("Obteniendo escaneo de adaptadores de red del equipo....")
    try:
        LinPS="powershell -Executionpolicy Bypass -File Monitoreo_Red.ps1"
        runNetscan=subprocess.run(LinPS, capture_output=True, text=True)
        print("Escaneo completado")
        print(runNetscan.stdout)
        logging.info("Escaneo completado con exito")
    except Exception as e:
        print(f"A ocurrido un error en el escaneo de adaptadores: {e}")
        logging.error("A ocurrido un error en el escaneo de adaptadores:" + str(e))

def honeypots(): #Realizada por Valeria Duron
    print("Generando Honeypots con el API de SHODAN....")
    try:
        LinPS="powershell -Executionpolicy Bypass -File Honeypots.ps1"
        runNetscan=subprocess.run(LinPS, capture_output=True, text=True)
        print("Escaneo completado")
        print(runNetscan.stdout)
        logging.info("Escaneo completado con exito")
    except Exception as e:
        print(f"A ocurrido un error en la generación de Honeypots: {e}")
        logging.error("A ocurrido un error en la generación de honeypots:" + str(e))
        
def obtener_ips():
    try:
        dom=input("Ingrese el dominio al que le quiera sacar la IP:\n")
        print("Obteniendo ip.....")
        lineaPS = "powershell -Executionpolicy ByPass -Command Resolve_DnsName -Name " + dom
        runningProcesses = subprocess.run(lineaPS, capture_output=True, text=True)
        print(runningProcesses.stdout)
    except Exception as e:
        print(f"A ocurrido un error en la busqueda de la dirección IP: {e}")
        logging.error("A ocurrido un error al sacar la dirección IP del dominio:" + str(e))
def IPS_scan():#Realizado por Briseidy
    print("Escaneando IP....")#Hay que editar la dirección IP directamente del codigo de powershell
    try:
        LinPS="powershell -Executionpolicy Bypass -File API.ps1"
        runNetscan=subprocess.run(LinPS, capture_output=True, text=True)
        print("Escaneo completado")
        print(runNetscan.stdout)
        logging.info("Escaneo completado con exito")
    except Exception as e:
        print(f"A ocurrido un error en la generación de Honeypots: {e}")
        logging.error("A ocurrido un error en la generación de honeypots:" + str(e))




def menu():
    print("Elija una de las 5 tareas a realizar:")
    print("1--Historial de procesos\n2--Escaneo de adaptadores de red")
    print("3--Generación de Honeypots con el API de SHODAN\n4--Busqueda de dirección de IP de un dominio\n5--Analizis de dirección IP")
    while True: 
        op=input("Elija una opción del 1 al 5, si desea salir del programa oprima el numero 6.\n")

        if op=="1":
            process_history()
        elif op=="2":
            Netad_scan()
        elif op=="3":
            honeypots()
        elif op=="4":
            obtener_ips()
        elif op=="5":
            IPS_scan()
        elif op=="6":
            print("Saliendo del programa.....")
            break
        else:
            print("Opción no valida")
if __name__=="__main__":
    menu()

    


        
    




    

