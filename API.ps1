#Código para extraer información de una IP sospechosa
#Analizar una api de abuse database
param(
[parameter(mandatory)] [string]$ipAddress)
$apikey = "e91328a52e454203e996f806aa803356bd725d7e35fce8424c9a0439c853fa4c94ec4c0d26c33b22" #clave API
$url =  "https://api.abuseipdb.com/api/v2/check?ipAddress=$ipAddress" #URL de la api
 # Dirección IP del servidor

#Solicitud para verificar si la IP es maliciosa o no
$headers = @{
    Key = $apiKey
    Accept = "application/json"
}

$response = Invoke-RestMethod -Uri $url -Method Get -Headers $headers

 # Analizar la respuesta
if ($response.data.abuseConfidenceScore -gt 50) {
    Write-Host "La IP es sospechosa"
} else {
    Write-Host "La Ip no es sospechosa"
}

Write-Host "Dominio: $($response.data.domain)"

#Generar archivo txt

# Crear un archivo nuevo con contenido
"Esto es el contenido del archivo" | Out-File -FilePath "salida.txt"

# Añadir contenido a un archivo existente
"Más contenido" | Out-File -FilePath "salida.txt" -Append

# Sobrescribir un archivo si existe
"Nuevo contenido" | Out-File -FilePath "salida.txt" -Force

#  El cmdlet `Out-File` tiene otros parámetros para controlar la codificación, el ancho de la salida, etc.
 