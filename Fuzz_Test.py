import socket
from boofuzz import * #La documentación de esta libreria esta en github :D
def get_ip():
    print("Con que dato cuenta:\n1--IP\n2--Dominio")
    op=input()
    if op=="1":
        ip=input("Introduzca la ip a analizar (ipv4 EJ: 0.0.0.0):\n")
    elif op=="2":
        print("introduzca el dominio a analizar (Ej: google.com):")
        dom=input()
        print("Verificando dominio.....")
        try:
            ip=socket.gethostbyname(dom)
            print(f"La dirección IP de su dominio es:\n{ip}")
        except Exception as e:
            print(f"Se produjo un error al querer conectar con el dominio: {e}")
    else:
        print("Opción invalida")
    return ip

def fuzz_test(ip):
    prueba= Session(target=Target(connection=TCPSocketConnection(ip, 80)))
    try:
        s_initialize("Request")
        s_string("Prueba")
        s_string(" ")
        s_string("Fuzzme", fuzzable=True)
        prueba.connect(s_get("Request"))
        prueba.fuzz
    except Exception as e:
        print(f"Algo salio con la petición: {e}")

        
    



