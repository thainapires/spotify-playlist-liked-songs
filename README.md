# 
<h2 align="center">Last 10 Saved Tracks Spotify</h2>

<p align="center">
  A little while ago, I searched if there was a tool available online that saved all of my saved songs in spotify into a playlist, but I couldn't find it. I decided to explore the
  spotify API and I was able to save the last 10 songs of my spotify saved songs, I can get up to 50 of the last songs and save in a playlist. Now I'm trying to find a way to
  save all of the songs. So, for now my code retrieves the last 10 saved tracks of my spotify and adds to a new playlist called "Last 10 songs saved".
</p>

<p align="center">
   <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/thainapires/last10-SavedTracks-Spotify">
   <img alt="Lines of code" src="https://img.shields.io/tokei/lines/github/thainapires/last10-SavedTracks-Spotify">
</p>

# Requirements

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
