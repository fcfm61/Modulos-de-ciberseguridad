param(
[parameter(mandatory)] [datetime]$fecha)

Write-Host "La fecha especificada para gestionar los procesos es:" $fecha
$pd=Get-WmiObject -Class win32_process | Where-Object {$_.CreationDate -AND ([System.Management.ManagementDateTimeConverter]::ToDateTime($_.CreationDate).Date -EQ $fecha.Date)} | Select-Object -Property Name, ProcessId, @{Name="Fecha de ejecución";Expression={[System.Management.ManagementDateTimeConverter]::ToDateTime($_.CreationDate)}}
$pd

