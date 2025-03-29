<#
.SYNOPSIS
Este es el script principal del 1er entregable del PIA de Programación en Ciberseguridad.
Este realiza un conjunto de tareas que se enfocan en mantener seguro un equipo en el que se esta trabajando
Tiene 3 tareas principales:
-Generar una lista de archivos ocultos en un directorio especificado
-Hacer una revisión de los recursos del equipo
-Generar un reporte del historial de los procesos en el equipo en un día especificado
La interfaz principal es un menu que va del 1 al 3 segun la tarea que quieras realizar.
.OPTION 1
En esta opcion se ejecutara la funcion encargada de listar los archivos ocultos
.FUNCTION get-HiddDirectory
Nos muestra listado de archivos en un directorio especificado
.OPTION 2
En esta opcion se nos desplegara un submenu según sea el recurso que queramos revisar
.FUNCTION Get-Memory
Nos muestra el uso de la memoria del equipo en el que se esta trabajando
.FUNCTION Get-Disk
Nos muestra varios datos del uso del disco (o diferentes discos) del equipo en el que se esta trabajando
.FUNCTION Get-Processor
Nos muestra el porcentaje del uso del procesador del equipo
.FUNCTION Get-Red
Nos muestra los datos de la red a la que se encuentra concetada nuestro equipo
.OPTION 3
En esta opción se generara una lista de procesos según el dia en que se ejecutaron
.FUNCTION get-processhistory
Funcion encargada de generar una lista de procesos con una fecha especificada por el usuario.
.PARAMETER $contenido
Variable en la que se almacenara el contenido del reporte de los procesos, al desplegar la función se proporcionara una fecha de maximo 10 dias de antigüedad 
debido a que si se pone una fecha mas antigüa (Al menos en el equipo en el que se realizo el modulo) No generará reporte alguno
.PARAMETER $rep
Variable que según sea S o N nos permitira generar un archivo .txt con el contenido del reporte, el cual se generará en la carpeta del modulo (¿?)

#>
Write-Host
"Bienvenido, por favor elija una de las siguientes opciones:
1.- Archivos ocultos en alguna carpeta.
2.- Revisión de recursos del sistema.
3.- Registro de procesos en algún día determinado.
"
$resp=Read-Host "Seleccione una de las 3 opciones"
switch ($resp){
1 {
write-host "Archivos ocultos en el equipo"
get-HiddDirectory
break
}2{
Write-Host "Revisión de Recursos del sistema"
Write-Host "¿Qué quiere revisar?
    -Memoria....[M]
    -Disco......[D]
    -Procesador.[P]
    -Red........[R]
    "
    $r=Read-Host 
    
    switch($r){
    'M'{
    Write-Host "Chequeo de Memoria"
        Get-Memory
        break
    }'D'{
    Write-Host "Chequeo de Disco"
        Get-Disk
        break
    }'P'{
    Write-Host "Chequeo de procesador"
        Get-Processor
        break
    }'R'{
    Write-Host "Chequeo de red"
        Get-Red
        break
    }default{
        Write-Host
        "Opción no valida"
    }
    }
break
}3{
Write-Host "Registro de procesos en algún día determinado (Ultimos 8 dias)"
$contenido= get-processhistory
$contenido
$rep=read-host "¿Desea generar un archivo con los datos?
[S]-si/[N]-no"
if ($rep -eq "S"){
Write-Host "Generando archivo..."
write-report $contenido
Write-Host "Listo ;)"#El Archivo se genera en la carpeta de modulo?¿
break
}elseif($rep -eq "N"){
Write-Host "No se generará un archivo"  
break
}else{
Write-Host "No se eligio una opción correcta"
}
}default{
Write-Host "Opción no valida"
}
}