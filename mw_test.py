import hashlib
from virus_total_apis import PublicApi
def malware_test():
    api_key="314017e3611f7835bf68766315e6aa8f6c581a8cd92d9f34dbfa674e13f35173" #Aqui poner su propia api key de virus total
    api=PublicApi(api_key)
    ruta=input("Ingrese la ruta del archivo que quiere analizar:\n") #Se puede introducir el nombre del archivo si esta en la misma carpeta que el script
                                                                        #Si no es el caso, introducir toda la ruta del archivo
    print("Analizando archivo....")
    try:
        with open(ruta, "rb") as file:
            hash_arch=hashlib.md5(file.read()).hexdigest()
        response=api.get_file_report(hash_arch)
        print(response)
        if response["response_code"]=="200": #Aqui se busca directamente desde el diccionario que se genera al hacer la petición con el API
            if response["results"]["positives"]:
                print("PRECAUCION!\nArchivo sospechoso")
            else:
                print("Archivo analizado es seguro")
        else:
            print("El archivo no se a podido analizar")
    except FileNotFoundError:
        print("El archivo no existe, favor de checar la ruta")
    except Exception as e:
        print(f"Algo salio mal codigo de error: {e}")

