 $redes= Get-NetAdapter #Con get-netadapter tenemos info de los adaptadores de red disponibles en el sistema
 foreach ($red in $redes) {  #se inicia cilo para cada una de las redes encontradas
     $name=$red.name
     $red_estadisticas= Get-NetAdapterStatistics -Name $red.name #De la red encontrada se comienzan a bsucar las estadisticas para iniciar el monitoreo de rendimiento
     $red_bytes_r=$red_estadisticas.ReceivedBytes / 1
     $red_bytes_s=$red_estadisticas.SentBytes / 1
     $red_errors=$red_estadisticas.receiveerrors
     $red_errors_s=$red_estadisticas.senterrors
     Write-Host "Nombre de red:" $name
     Write-Host "Bytes recibidos en la red:" $red_bytes_r
     Write-Host "Bytes enviados:" $red_bytes_s "MB"
     Write-Host "Errores recibidos: " $red_errors
     Write-Host "Errores enviados:" $red_errors_s
 }
