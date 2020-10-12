# 
<h2 align="center">Playlist with Liked Tracks from Spotify</h2>

<p align="center">
  A little while ago, I really wanted to save all of my liked spotify songs into one single playlist, but doing this by hand would be impossible. I decided to explore the spotify API and this repository contains my code, that retrieves all of the liked songs from a spotify account and adds to a new playlist called "All my liked songs". I'm still working on improving the code.
</p>

<p align="center">
   <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/thainapires/last10-SavedTracks-Spotify">
   <img alt="Lines of code" src="https://img.shields.io/tokei/lines/github/thainapires/last10-SavedTracks-Spotify">
</p>

# Usage

First install the following:

```
pip3 install requests
```

```
pip3 install json
```

Than, create a file called secrets.py with the following code:

```
#Keys
spotify_token = "YOUR-TOKEN-HERE"
spotify_user_id = "YOUR-USER-ID-HERE"
```

You have to change the values of the token and user id according to yours.

Now, you can run the code:

```
python3 Create_Playlist.py
```

*If you want to change the number of songs, you can change the limit up to 50 in the query
