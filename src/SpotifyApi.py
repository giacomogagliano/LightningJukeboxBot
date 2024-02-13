import spotipy
from MusicPlatformApi import MusicPlatformApi


class SpotifyApi(MusicPlatformApi):
    def __init__(self, auth_manager) -> None:
        self._api = spotipy.Spotify(auth_manager)
        super().__init__()

    def current_user_playing_track(self):
        return self._api.current_user_playing_track()

    def queue(self):
        return self._api.queue()

    def playlist_items(self, playlistid, offset, limit):
        return self._api.playlist_items(playlistid, offset, limit)

    def playlist(self, playlistid, fields):
        return self._api.playlist(playlistid, fields)

    def search(self, string):
        return self._api.search(string)

    def track(self, uri):
        return self._api.search(uri)
