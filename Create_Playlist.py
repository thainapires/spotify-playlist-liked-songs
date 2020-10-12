from secrets import spotify_user_id, spotify_token
import requests
import json

#Helps to print json response
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


query = f'https://api.spotify.com/v1/me/tracks?offset=0&limit=10' #Returns last 10 songs in the saved playlist

#Requesting and getting response
response = requests.get(query, 
               headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})
json_response = response.json()

#Printing response
print("Last 10 songs in the saved playlist:")
for i,j in enumerate(json_response['items']):
    print(f"{i+1}) \"{j['track']['name']}\"")