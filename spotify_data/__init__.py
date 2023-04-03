from dagster import Definitions, load_assets_from_modules
from spotify_data.resources import spotify_resource
from dagster_aws.s3 import s3_pickle_io_manager, s3_resource
from . import assets

all_assets = load_assets_from_modules([assets])


defs = Definitions(
    assets=all_assets,
    resources={
        "spotify": spotify_resource.configured(
            {"client_secret": {"env": "SPOTIFY_CLIENT_SECRET"}, "client_id": {"env": "SPOTIFY_CLIENT_ID"}, "redirect_uri": {"env": "SPOTIFY_REDIRECT_URI"}}
        ), "io_manager": s3_pickle_io_manager.configured({"s3_bucket": {"env": "MINIO_BUCKET"}}), "s3": s3_resource.configured({
            "endpoint_url": {"env": "MINIO_ENDPOINT_URL"}})
    },
)
