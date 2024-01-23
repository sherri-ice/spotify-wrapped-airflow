import datetime
import os

from airflow.decorators import task, dag
from dotenv import load_dotenv, find_dotenv

from spotify_utils import Spotify

default_args = {
    'owner': 'sherri-ice'
}

load_dotenv(find_dotenv())


@dag(default_args=default_args, schedule=None, start_date=datetime.datetime.now())
def spotify_dag():
    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

    spotify_client: Spotify = None

    @task
    def setup_spotify_client():
        spotify_client = Spotify(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope="playlist-read-private",
            use_redis=True
        )

    @task
    def get_spotify_user():
        print(spotify_client.get_current_user())

    get_spotify_user() >> get_spotify_user()


spotify_dag()
