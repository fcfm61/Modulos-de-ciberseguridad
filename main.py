import honeypots #Hecho por Valeria Duron
import mw_test #Hecho por Jorge Diaz
import Fuzz_Test #Hecho por Jorge Diaz
import IPAnalyse #Hecho por Briseidy Oranday
import encryptmsg #Hecho por Briseidy Oranday
def menu():
    print("Elija una de las 5 tareas a realizar:")
    print("1--Busqueda de Honeypots\n2--Prueba de Fuzzing")
    print("3--Escaneo de red\n4--Análisis de malware en un archivo\n5--Encriptación de un mensaje")
    while True: 
        op=input("Elija una opción del 1 al 5, si desea salir del programa oprima el numero 6.\n")

        if op=="1":
            print("Bienvenido a la busqueda de Honeypots con el API de Shodan")
            honeypots.request_honeypot()
        elif op=="2":
            print("Prueba de Fuzzing")
            ip=Fuzz_Test.get_ip()
            print(f"Analizando la ip: {ip}")
            Fuzz_Test.fuzz_test(ip)
        elif op=="3":
            print("Bienvenido al escaneo de red con el API del Abuse Data Base")
            ipadress=input("Introduzca una IP que quiera analizar:")
            resp=IPAnalyse.analyzeIP(ipadress)
            print(resp)
        elif op=="4":
            print("Procedamos con el analisis de malware en un archivo...(Con el API de virustotal)")
            mw_test.malware_test()
        elif op=="5":
            print("Encriptación de un mensaje")
            encryptmsg.encrypt_msg()
        elif op=="6":
            print("Saliendo del programa.....")
            break
        else:
            print("Opción no valida")
if __name__=="__main__":
    menu()

