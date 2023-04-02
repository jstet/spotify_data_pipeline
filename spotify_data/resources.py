from dagster import resource,StringSource
from spotify_data.cache_handler import CustomHandler
import spotipy
from spotipy.oauth2 import SpotifyOAuth

@resource(config_schema={"client_secret": StringSource, "client_id": StringSource, "redirect_uri": StringSource})
def spotify_resource(init_context):
    scope = "user-top-read"

    auth_manager = SpotifyOAuth(scope=scope,
                                open_browser=False,
                                client_secret=init_context.resource_config["client_secret"],
                                client_id=init_context.resource_config["client_id"],
                                redirect_uri=init_context.resource_config["redirect_uri"],
                                cache_handler=CustomHandler())


    sp = spotipy.Spotify(auth_manager=auth_manager)

    return sp