import fileinput
import os
from dotenv import load_dotenv
import errno
import logging
import spotipy
load_dotenv()



logger = logging.getLogger(__name__)


def replace_or_append(file_path, search, new_text):
    with open(file_path, 'a+') as file:
        content = file.read()
        if search not in content:
            print("writing to file")
            file.write("\n"+ new_text)
            return
        else:
            with fileinput.input(file_path, inplace=True) as file2:
                for line in file2:
                    if search in line:
                        line.replace(line, new_text)
                        return

               

class CustomHandler(spotipy.cache_handler.CacheHandler):
    """
    Handles reading and writing cached Spotify authorization tokens
    as json files on disk.
    """

    def __init__(self):
        pass

    def get_cached_token(self):
        token_info = None

        try:
            token_info = os.getenv("SPOTIFY_ACCESS_TOKEN")
            token_info = eval(token_info)

        except Exception:
            logger.debug("cache does not exist or couldnt been read")
           

        return token_info

    def save_token_to_cache(self, token_info):
       
            replace_or_append(".env", "SPOTIFY_ACCESS_TOKEN", f'SPOTIFY_ACCESS_TOKEN="{token_info}"')
       
