import requests

API_Key = ''  # Ta clé API
WORKSPACE_RDR_IT_ID = '5f7ecb9f2bcbc7438ea54100'

headers = {
    'X-API-KEY': API_Key
}

# Récupérer la liste des utilisateurs (collaborateurs) du workspace
response = requests.get(f'https://api.clockify.me/api/v1/workspaces/{WORKSPACE_RDR_IT_ID}/users', headers=headers,params={
    'page' : 1,
    'page-size' : 200,
    'archived' : 'False'
})

if response.status_code == 200:
    users = response.json()
    for user in users:
        print(f"Utilisateur : {user['name']}, ID : {user['id']}")
else:
    print(f"Échec de la requête : {response.status_code} - {response.text}")
