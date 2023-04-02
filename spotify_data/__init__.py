from dagster import Definitions, load_assets_from_modules
from spotify_data.resources import spotify_resource
from . import assets

all_assets = load_assets_from_modules([assets])


defs = Definitions(
    assets=all_assets,
    resources={
        "spotify": spotify_resource.configured(
            {"client_secret": {"env": "SPOTIFY_CLIENT_SECRET"}, "client_id": {"env": "SPOTIFY_CLIENT_ID"}, "redirect_uri": {"env": "SPOTIFY_REDIRECT_URI"}}
        )
    },
)
