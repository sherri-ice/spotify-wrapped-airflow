import os
from typing import Union

import redis
import spotipy
from spotipy.cache_handler import RedisCacheHandler
from spotipy.oauth2 import SpotifyOAuth


class Spotify:
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, scope: Union[str, list[str]],
                 use_redis: bool):
        kwargs = {}
        if use_redis:
            host = os.getenv("REDIS_HOST")
            port = int(os.getenv("REDIS_PORT"))
            redis_instance = redis.Redis(
                host=host,
                port=port
            )
            kwargs["cache_handler"] = RedisCacheHandler(redis_instance)
        auth_manager = SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope,
            **kwargs
        )
        self.__spotify_client__ = spotipy.Spotify(auth_manager=auth_manager)

    def get_current_user(self):
        return self.__spotify_client__.current_user()
