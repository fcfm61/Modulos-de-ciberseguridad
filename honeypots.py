import shodan
import json
def request_honeypot(): #El codigo se puso en una funcion debido a que se ejecutaba por si solo en el script principal
    #Configurando API KEY
    API_KEY= "8FP9fCCcvalrgwj2zbCHwsF8GvVXLEoa"
    shodan_cliente= shodan.Shodan(API_KEY)
    #Diccionario con los honeypots a consultar en Shodan
    consultas={
        "Cowrie": "product:cowrie",             #Honeypot tipo SSH y Telnet
        "Dionaea": "product:dionaea",           #Honeypot tipo Malware y de red   
        "Conpot": "product:conpot",             #Honeypot tipo SCADA/IoT
        "Honeyd": "product:honeyd",      #Honeypot tipo red
        "Wordpot": "product:wordpot"         #Honeypot de tipo WEB
    }
    #Crear funcion para realizar las consultas
    def search_honeypots(consultas, limite=5): #Se implemta limite de busquedas para no saturar Shodan
        honeypots_encontrados=[]  #Se crea lista para almacenar los honeypots encontrados
        for honeypot, consulta in consultas.items(): #Se crea bucle para iterar cada elemento del diccionario (honeypot)
           print(f"Buscando {honeypot} en Shodan...")
           try:
               resultados=shodan_cliente.search(consulta, limit=limite) #Realizando busqueda en Shodan
               for resultado in resultados['matches']: #Unicamente los resultados que fueron satisfactorios en la busqueda
                   honeypot_info={   #se crea diccionario para almacenar la info de cada honeypot
                       "Honeypot": honeypot,
                       "IP":resultado.get('ip_str'),
                       "port": resultado.get('port'),
                       "hostname": resultado.get('hostnames'),
                       "Pais": resultado.get('location', {}).get('country_name'),
                       "Banner": resultado.get('data'),
                       "timestamp": resultado.get('timestamp')
                    }
                   honeypots_encontrados.append(honeypot_info)  #Agregar el diccionario a la lista
           except Exception as e:      
                print(f"Error en la búsqueda de {honeypot}: {e}")    #Si hubo algun error en la búsqueda muestra el porque
         #Guardar resultados en archivo JSON
        with open ('honeypots_shodan.json', 'w') as archivo_json: #Se crea archivo
          json.dump(honeypots_encontrados, archivo_json, indent=4 )#Guardar Archivo
        print( f"Se ha creado un archivo JSON, honeypots_shodan.json, con la información recabada")
        return honeypots_encontrados

        search_honeypots(consultas, limite=5)
request_honeypot()


                
               
                   
                   
                   
               
