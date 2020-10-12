from secrets import spotify_user_id, spotify_token
import requests
import json

uris = [] 
query = f'https://api.spotify.com/v1/me/tracks?offset=0&limit=10' #Returns last 10 songs in the saved playlist

#Requesting and getting response
response = requests.get(query, 
               headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {spotify_token}"})
json_response = response.json()

#print(response.status_code)

#Printing response
#print("Last 10 songs in the saved playlist:")
for i,j in enumerate(json_response['items']):
    uris.append(j['track']['uri'])
#    print(f"{i+1}) \"{j['track']['name']}\"")

#Creating the playlist 

query2 = f"https://api.spotify.com/v1/users/{spotify_user_id}/playlists"
request_body = json.dumps({
          "name": "Last 10 songs saved",
          "description": "The last 10 songs that I've saved",
          "public": False
})
response2 = requests.post(url = query2, data = request_body, headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {spotify_token}"})
url = response2.json()['external_urls']['spotify']
#print(response2.status_code)

#Filling the playlist with the songs

playlist_id = response2.json()['id']
query3 = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
request_body = json.dumps({
          "uris" : uris
        })
response3 = requests.post(url = query3, data = request_body, headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {spotify_token}"})
#print(response3.status_code)

print(f'Your playlist is ready at {url}')