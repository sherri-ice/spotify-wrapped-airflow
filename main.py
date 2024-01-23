import os

from spotify_utils import Spotify
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

if __name__ == '__main__':
    sp = Spotify(client_id, client_secret, redirect_uri, scope="playlist-read-private", use_redis=True)
    print(sp.get_current_user())
