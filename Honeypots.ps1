#Configurando API-KEY
   $ApiKey= "GEPcSFGJToA7bYZBXOkvix5x2g3kWyl3"
   $consultas= @{       #se crea un hashtable (diccionario) para almacenar las búsquedas de honeypots por clave-valor
      "Cowrie" ="product:cowrie" #Honeypot tipo SSH y Telnet
      "Dionaea" = "product:dionaea" #Honeypot de tipo malware y de red
      "Conpot" = "product:conpot" #Honeypot de tipo SCADA/IoT
      "Honeyd" = "product:honeyd" #Honeypot de tipo red
      "Wordpot" = "product:wordpot" #Honeypot de tipo WEB
    }
  
   $honeypots_encontrados= @() #Se crea lista para almacenar los honeypots encontrados
   $limit = 5 #Se establece límite de búsqueda por honeypot

   foreach($honeypot in $consultas.Keys) { #Se inicia ciclo foreach para recorrer cada honeypot en "consultas"
       $query= $consultas[$honeypot] #Aqui se establece el query (solicitud de búsqueda) indicando que es en consultas y $honeypots en este caso la clave (honeypot a buscar)
       Write-Host "Buscando honeypots en Shodan..."
       $url= "https://api.shodan.io/shodan/host/search?key=$ApiKey&query=$query&limit=$limit"  #definimos la URL
         try {                    #Iniciamos la búsqueda
           $resultadoAPI= Invoke-RestMethod -Uri $url -Method Get
              foreach ($resultado in $resultadoAPI.matches) {     #Ciclo para recorrer cada uno
                 $honeypot_info = [PSCustomObject]@{    #Se crea hashtable para almacenar la info de cada uno, PSCustomObject para darle estructura clara a la salida
                    Honeypot = $honeypot
                    IP = $resultado.ip_str
                    Port = $resultado.port
                    Hostname = ($resultado.hostnames -join ",")
                    País = $resultado.location.country_name
                    Banner = $resultado.data
                    Timestamp = $resultado.timestamp
                 }
             $honeypots_encontrados += $honeypot_info  #Se agrega la info a la lista principal
             }
          }
        catch {
        Write-Output "Error en la búsqueda de Honeypots en shodan"
        }
    }
    #Generar archivo .csv
    $fechaFile= Get-Date -Format "yyyyMMdd_HHmmss" #Se genera en ese formato para tener toda la info completa de la creación (Año, mes, día, hora, minutos, segundos)
    $reportPath = "reporte_honeypots_shodan_$fechaFile.csv" #Nombre del archivo
    $honeypots_encontrados | Export-Csv -Path $reportPath -NoTypeInformation -Encoding UTF8  #Guardando resultados en .cvs
    $hash= Get-FileHash -Path $reportPath -Algorithm SHA256  #Obtener hash del archivo
    $fecha = Get-Date -Format "dddd, MMMM dd, yyyy" #Fecha en otro formato para mostrar
    Write-Output "Tarea ejecutada: Búsqueda de honeypots en Shodan"
    Write-Output "Fecha de ejecución: $fecha"
    Write-Output "Archivo generado: $(Resolve-Path $reportPath)"
    Write-Output "Hash SHA256 del archivo generado: $($hash.Hash)"






     
     

