from dagster import asset, get_dagster_logger, Output, MetadataValue
import json
from datetime import datetime




@asset(required_resource_keys={"spotify"}) # add the asset decorator to tell Dagster this is an asset
def top_tracks(context):
    logger = get_dagster_logger()
    tracks = context.resources.spotify.current_user_top_tracks(time_range="short_term",limit="1")
    logger.info(f"Got {len(tracks)} items.")
    now = datetime.now() # current date and time
    
    return Output(  
        value=json.dumps(tracks),   
        metadata={
            "owner": "jstet",
            "num_records": len(tracks), 
            "time": now.strftime("%m/%d/%Y, %H:%M:%S"),
        }
    )



