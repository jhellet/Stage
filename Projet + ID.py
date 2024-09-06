import requests

API_Key = ''  
WORKSPACE_RDR_IT_ID = '5f7ecb9f2bcbc7438ea54100'

headers = {
    'X-API-KEY' : API_Key
}

response = requests.get(f'https://api.clockify.me/api/v1/workspaces/{WORKSPACE_RDR_IT_ID}/projects', headers=headers, params={
    'page': 1,  
    'page-size': 200,  
    'archived': 'false' 
})

# Vérification du statut de la réponse
if response.status_code == 200:
    print("Requête réussie ! Voici la liste des projets :")
    projects = response.json()
    for project in projects:
        print(f"Projet : {project['name']}, ID : {project['id']}")
else:
    print(f"Échec de la requête : {response.status_code} - {response.text}")
