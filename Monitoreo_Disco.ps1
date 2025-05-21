  $discos= Get-PSDrive -PSProvider FileSystem  #Funcion con Get_PSDrive para monitorear uso del disco en el sistema
  foreach ($disco in $discos) { #Se realiza ciclo en dado caso que se cuenten con múltiples discos
      $name=$disco.name #Nombre del disco
      $espacio_disco=$disco.used / 1   #Espacio usado
      $espacio_libre=$disco.free / 1    #Espacio disponible
      $espacio_total= ($disco.used + $disco.free) / 1  #Espacio total
      $porcentaje_uso=($espacio_disco/$espacio_total) * 100  #Porcentaje en uso
      Write-Host "Nombre del disco:" $name
      Write-Host "Espacio de disco usado:" $espacio_disco "gb"
      Write-Host "Espacio libre del disco:" $espacio_libre "gb"
      Write-Host "Espacio total del disco:" $espacio_total "gb"
      Write-Host "Porcentaje de uso del disco:" $porcentaje_uso "gb"
  }

