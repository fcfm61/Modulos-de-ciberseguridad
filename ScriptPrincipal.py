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
        
def get_ips():
    try:
        dominio = input("Ingrese un dominio:\n")
        lineaPS = "powershell -Executionpolicy ByPass -Command resolve-dnsname -Name "+ dominio
        runningProcesses = subprocess.check_output(lineaPS)
        print(runningProcesses.decode())
        logging.info(f"Información sobre {dominio}:\n{runningProcesses}")
    except Exception as e:
        print(f"A ocurrido un error en la busqueda de la dirección IP: {e}")
        logging.error("A ocurrido un error al sacar la dirección IP del dominio:" + str(e))
def IPS_scan():#Realizado por Briseidy
    ip=input("Ingresa una de las direcciones IPV4 de algún dominio:\n")
    print("Escaneando IP....")
    try:
        LinPS="powershell -Executionpolicy Bypass -File API.ps1 -ipAddress "+ip
        runNetscan=subprocess.run(LinPS, capture_output=True, text=True)
        print("Escaneo completado")
        print(runNetscan.stdout)
        logging.info("Escaneo completado con exito")
    except Exception as e:
        print(f"A ocurrido un error en la generación de Honeypots: {e}")
        logging.error("A ocurrido un error en la generación de honeypots:" + str(e))

def disk_ussage():
    print("Obteniendo escaneo de uso del disco del equipo....")
    try:
        LinPS="powershell -Executionpolicy Bypass -File Monitoreo_Disco.ps1"
        runNetscan=subprocess.run(LinPS, capture_output=True, text=True)
        print("Escaneo completado")
        print(runNetscan.stdout)
        logging.info("Escaneo del disco completado con exito")
    except Exception as e:
        print(f"A ocurrido un error en el escaneo del disco: {e}")
        logging.error("A ocurrido un error en el escaneo del disco:" + str(e))

def menu():
    print("Elija una de las 5 tareas a realizar:")
    print("1--Historial de procesos\n2--Escaneo de adaptadores de red")
    print("3--Generación de Honeypots con el API de SHODAN\n4--Busqueda de dirección de IP de un dominio\n5--Analizis de dirección IP\n6--Escaneo de uso del disco")
    while True: 
        op=input("Elija una opción del 1 al 6, si desea salir del programa oprima el numero 7.\n")

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
            disk_ussage()
        elif op=="7":
            print("Saliendo del programa.....")
            break
        else:
            print("Opción no valida")

def menu_argparse():
    try:
        parser=argparse.ArgumentParser()
        parser.add_argument("-t", dest="tarea", help="'historial','disco','getip','scanip','honeypots','scanadpt'")
        args=parser.parse_args()
        if args.tarea == "historial":
            process_history()
        elif args.tarea == "scanadpt":
            Netad_scan()
        elif args.tarea == "honeypots":
            honeypots()
        elif args.tarea == "getip":
            get_ips()
        elif args.tarea == "scanip":
            IPS_scan()
        elif args.tarea == "disco":
            disk_ussage()
    except Exception as e:
        print(f"El codigo de error es: {e}")

if __name__=="__main__":
    menu_argparse()






    


    


        
    




    

