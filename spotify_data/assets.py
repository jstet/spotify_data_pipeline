from dagster import asset
import json


@asset(required_resource_keys={"spotify"}) # add the asset decorator to tell Dagster this is an asset
def top_tracks(context):
    test = context.resources.spotify.current_user_top_tracks()
    return json.dumps(test)



