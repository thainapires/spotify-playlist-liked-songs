from secrets import spotify_user_id, spotify_token
import requests
import json

class Playlist:

    uris = []
    url = ''
    playlist_id = ''
    total = ''

    def __init__(self):
        pass

    def get_total(self):
        query = 'https://api.spotify.com/v1/me/tracks?offset=0&limit=1'

        response = requests.get(query, 
               headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {spotify_token}"})
        
        json_response = response.json()
        total = json_response['total']
        return total

    def get_all_songs(self):
        
        self.total = self.get_total()            
        total_retrieved = 0

        while total_retrieved < self.total:
            query = f'https://api.spotify.com/v1/me/tracks?offset={total_retrieved}&limit=50'
            response = requests.get(query, 
                    headers={"Content-Type":"application/json", 
                                "Authorization":f"Bearer {spotify_token}"})
            json_response = response.json()

            urisAux = []
            for i,j in enumerate(json_response['items']):
                urisAux.append(j['track']['uri'])
                total_retrieved += 1

            self.uris.append(urisAux) 

    def create_playlist(self):
        query = "https://api.spotify.com/v1/users/{}/playlists".format(spotify_user_id)
        
        request_body = json.dumps({
                "name": "All my liked songs",
                "description": "A Playlist with all of the songs that I Liked!",
                "public": False
        })
        
        response = requests.post(url = query, data = request_body, headers={"Content-Type":"application/json", 
                                "Authorization": "Bearer {}".format(spotify_token)})
        
        json_response = response.json()

        self.url = json_response['external_urls']['spotify']
        self.playlist_id = json_response['id']

    def populate_playlist(self):
        
        query = f"https://api.spotify.com/v1/playlists/{self.playlist_id}/tracks"

        for uri in self.uris:
        
            request_body = json.dumps({
                    "uris" : uri
                    })
            response = requests.post(url = query, data = request_body, headers={"Content-Type":"application/json", 
                                    "Authorization":f"Bearer {spotify_token}"})
        
        print('Your playlist is ready at {}'.format(self.url))
        
if __name__ == '__main__':
    #Creating the Playlist Object
    playlist = Playlist()
    #Getting all of the songs
    playlist.get_all_songs()
    #Creating the empty playlist in spotify
    playlist.create_playlist()
    #Populating the playlist
    playlist.populate_playlist()