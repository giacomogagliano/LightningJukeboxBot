import spotipy
from spotipy.oauth2 import SpotifyOAuth
from MusicPlatform import MusicPlatform
import spotifyhelper


class Spotify(MusicPlatform):
    # from spotipy
    @property
    def OAuth():
        return SpotifyOAuth

    @property
    def OauthError():
        return spotipy.oauth2.SpotifyOauthError

    @property
    def Exception():
        return spotipy.exceptions.SpotifyException

    # from spotify helper

    @property
    def Settings():
        return spotifyhelper.SpotifySettings

    @property
    def CacheHandler():
        return spotifyhelper.CacheJukeboxHandler

    @property
    def mp_is_none(self):
        return spotifyhelper.sp_is_none

    @property
    def oauthErrorText(self):
        return spotifyhelper.spotifyOauthErrorText

    @property
    def exception(self):
        return spotifyhelper.spotifyException

    @property
    def exceptionWarning(self):
        return spotifyhelper.spotifyExceptionWarning

    @property
    def callback_unhandled_exception(self):
        return spotifyhelper.callback_spotify_unhandled_exception

    @property
    def callback_info(self):
        return spotifyhelper.callback_spotify_info

    @property
    def callback_nocode(self):
        return spotifyhelper.callback_spotify_nocode

    @property
    def callback_connected(self):
        return spotifyhelper.callback_spotify_connected

    def add_to_queue(self, sp, uri_list):
        return spotifyhelper.add_to_queue(sp, uri_list)

    def get_track_title(self, item):
        return spotifyhelper.get_track_title(item)

    def apiFactory(self, auth_manager):
        return spotifyhelper.spotifyFactory(auth_manager)

    def get_price(self, chat_id):
        return spotifyhelper.get_price(chat_id)

    def set_price(self, price):
        return spotifyhelper.set_price(price)

    def create_auth_manager(
        self, chat_id, client_id, client_secret
    ):
        return spotifyhelper.create_auth_manager(
            chat_id, client_id, client_secret
        )

    def init_auth_manager(self, chat_id, client_id, client_secret):
        return spotifyhelper.init_auth_manager(
            chat_id, client_id, client_secret
        )

    def get_auth_manager(self, chat_id):
        return spotifyhelper.get_auth_manager(chat_id)

    def delete_auth_manager(self, chat_id):
        return spotifyhelper.delete_auth_manager(chat_id)

    def save_settings(self, sps):
        return spotifyhelper.save_spotify_settings(sps)

    def get_settings(self, userid):
        return spotifyhelper.get_spotify_settings(userid)

    def get_history(self, chat_id, maxlen):
        return spotifyhelper.get_history(chat_id, maxlen)

    def update_history(self, chat_id: int, title: str):
        return spotifyhelper.update_history(chat_id, title)

    def get_donation_fee(self, chat_id: int):
        return spotifyhelper.update_history(chat_id)

    def set_donation_fee(self, chat_id: int, fee: int):
        return spotifyhelper.set_donation_fee(chat_id, fee)

    def makeConnectMessage(self, uri):
        return spotifyhelper.makeConnectMessage(uri)

    def validateSearch(self, searchstr):
        return spotifyhelper.validateSearch(searchstr)

    def validateTrackId(self, track_id):
        return spotifyhelper.validateTrackId(track_id)

    def addSpotifyPrefix(self, track_id):
        return spotifyhelper.addSpotifyPrefix(track_id)

    def make_callback_infoText(self, chatid, userid, code):
        return spotifyhelper.make_callback_spotify_infoText(
            chatid, userid, code
        )

    def addUriListToDict(self, userdata, value):
        return spotifyhelper.addSpotifyPrefix(userdata, value)

    def makeRedirectUri(self, domain):
        return spotifyhelper.makeSpotifyRedirectUri(domain)
