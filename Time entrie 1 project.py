import requests

API_Key = '' 
WORKSPACE_RDR_IT_ID = '5f7ecb9f2bcbc7438ea54100'
USER_ID = '6638e6ad4d9c8438ec7785bc'  
PROJECT_ID = '665ed4e4472314478c691025' 

headers = {
    'X-API-KEY': API_Key
}


response = requests.get(f'https://api.clockify.me/api/v1/workspaces/{WORKSPACE_RDR_IT_ID}/user/{USER_ID}/time-entries', headers=headers, params={
    'project': PROJECT_ID
})

if response.status_code == 200:
    time_entries = response.json()
    for entry in time_entries:
        print(f"Temps : {entry['timeInterval']['duration']}, Date : {entry['timeInterval']['start']}")
else:
    print(f"Échec de la requête : {response.status_code} - {response.text}")
