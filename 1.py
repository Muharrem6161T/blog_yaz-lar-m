API_URL = f"https://{SERVER_IP}/openapi/authorize/login"
DATA  = {
    "username" : "admin",
    "password" : "Ka29101923."
}
PARAMS = {
    "client_id" : "1d5b36240f024978a7bd60934503f95d",
    "omadac_id" : OMADA_ID
}

HEADERS = {
    "content-type" : "application/json"
}
result = requests.post(url=API_URL, json=DATA, params=PARAMS, headers=HEADERS, verify=False)
    
print(result.json()["result"])

#>> {'csrfToken': 'lakjosnfdfoasndoıasndıoasdn', 'sessionId': 'iam-asmkdaslkmdlasmdasdkolllmkads'}
