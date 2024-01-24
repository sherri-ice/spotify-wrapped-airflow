import os

from dotenv import load_dotenv

from spotify_utils import Spotify

load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")


if __name__ == '__main__':
    sp = Spotify(client_id, client_secret, redirect_uri, use_redis=True).spotify_client
    print(sp.current_user())
