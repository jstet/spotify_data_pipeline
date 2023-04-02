import spotipy
from spotify_data.cache_handler import CustomHandler
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
load_dotenv()

scope = "user-top-read"

auth_manager = SpotifyOAuth(scope=scope,
                            open_browser=False,
                            client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
                            client_id=os.getenv("SPOTIFY_CLIENT_ID"),
                            redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
                            cache_handler=CustomHandler())


sp = spotipy.Spotify(auth_manager=auth_manager)

results = sp.current_user_top_tracks()

print(results)
