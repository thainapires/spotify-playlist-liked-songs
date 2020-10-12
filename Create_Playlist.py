from secrets import spotify_user_id, spotify_token
import requests
import json

uris = [] 
query = f'https://api.spotify.com/v1/me/tracks?offset=0&limit=50'

#Requesting and getting response
response = requests.get(query, 
               headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {spotify_token}"})
json_response = response.json()
#print(response.status_code)

#Printing response
for i,j in enumerate(json_response['items']):
    uris.append(j['track']['uri'])
    #print(f"{i+1}) \"{j['track']['name']}\"")

total = json_response['total']
while len(uris) < total:
    query = f'https://api.spotify.com/v1/me/tracks?offset={len(uris)}&limit=50'
    response = requests.get(query, 
               headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {spotify_token}"})
    json_response = response.json()
    for i,j in enumerate(json_response['items']):
        uris.append(j['track']['uri'])
        #print(f"{i+1}) \"{j['track']['name']}\"")


#Creating the playlist 
query2 = f"https://api.spotify.com/v1/users/{spotify_user_id}/playlists"
request_body = json.dumps({
          "name": "All saved songs",
          "description": "All of the songs that I have Saved",
          "public": False
})
response2 = requests.post(url = query2, data = request_body, headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {spotify_token}"})
url = response2.json()['external_urls']['spotify']
#print(response2.status_code)

#Filling the playlist with the songs
playlist_id = response2.json()['id']
query3 = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

finish = False
x= 0
y = 99
totalAdded = 0 

#Because it only adds 100 songs per request, we have to split the list
while(totalAdded != total):
    uris_aux = uris[x:y]
    request_body = json.dumps({
            "uris" : uris_aux
            })
    response3 = requests.post(url = query3, data = request_body, headers={"Content-Type":"application/json", 
                            "Authorization":f"Bearer {spotify_token}"})
    totalAdded = y
    if(totalAdded != total):
        x= y+1
        y = x+99
        if(y > total):
            y = total

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response3.json())
print(f'Your playlist is ready at {url}')