import requests
apikey="e91328a52e454203e996f806aa803356bd725d7e35fce8424c9a0439c853fa4c94ec4c0d26c33b22" #CLAVE API

#FUNCIÓN PARA ANALIZAR UNA API DE IP ABUSE DATABASE. 
def analyzeIP(ipaddress):
    url= f"https://api.abuseipdb.com/api/v2/check?ipAddress={ipaddress}" #URL DE LA API
    headers={
         'Key': apikey,
         }
    response=requests.get(url, headers=headers)
    if response.status_code==200:
        data= response.json()
        if data['data']['abuseConfidenceScore']>50:
            return["Esta es una IP sospechosa", data['data']['domain']]
        else:
            return["Esta no es una IP sospechosa", data['data']['domain']]
    else:
            return



