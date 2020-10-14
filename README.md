# Playlist with Liked Songs from Spotify

A Python Script that gets your liked songs, and generates a new playlist in your account with all of these songs.

<p>
   <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/thainapires/last10-SavedTracks-Spotify">
   <img alt="Lines of code" src="https://img.shields.io/tokei/lines/github/thainapires/last10-SavedTracks-Spotify">
</p>

## English

### Setup

1. Install the following package:

```
pip3 install requests
```

2. Get your spotify user ID and Oath Token:

   - To get your user ID, you have to login to spotify and go to the [Account Overview](https://www.spotify.com/us/account/overview/).
   - To get your Oath Token, visit this url: [click here](https://developer.spotify.com/console/post-playlists/). Click the Get Token button.


3. Create a file called secrets.py with the following code (replacing YOUR-TOKEN-HERE and YOUR-USER-ID-HERE with your token and your user id):

```
#Keys
spotify_token = "YOUR-TOKEN-HERE"
spotify_user_id = "YOUR-USER-ID-HERE"
```

4. Run the File

```
python3 createPlaylist.py
```

After that, you'll get a message with the URL for the playlist created.

## Português

Um Script em Python que pega todas as suas músicas curtidas, e gera uma nova playlist na sua conta com todas essas músicas.

### Setup

1. Instale o seguinte pacote no seu ambiente de desenvolvimento:

```
pip3 install requests
```

2. Pegue seu user ID e seu Token Oath:
   - To get your user ID, you have to login to spotify and go to the [Account Overview](https://www.spotify.com/us/account/overview/).
   - To get your Oath Token, visit this url: [click here](https://developer.spotify.com/console/post-playlists/). Click the Get Token button.


3. Crie um arquivo chamado secrets.py com o seguinte código (substituindo SEU-TOKEN-AQUI e SEU-USER-ID_AQUI com o seu token e seu user ID):

```
#Keys
spotify_token = "SEU-TOKEN-AQUI"
spotify_user_id = "SEU-USER-ID_AQUI"
```

4. Rode o arquivo

```
python3 createPlaylist.py
```

Depois disso, você irá receber uma mensagem com a playlist criada.
