from MusicPlatform import MusicPlatform


class MusicPlatformHandler(MusicPlatform):
    def __init__(self, platform: MusicPlatform) -> None:
        super().__init__()
        self._platorm = platform

    @property
    def platform(self) -> MusicPlatform:
        return self._platorm

    @platform.setter
    def platform(self, platform: MusicPlatform) -> None:
        self._platorm = platform

    # implementations

    @property
    def OAuth(self):
        return self.platform.OAuth

    # from spotipy
    @property
    def OauthError(self):
        return self.platform.OauthError

    @property
    def Exception(self):
        return self.platform.Exception

    def current_user_playing_track(self):
        return self.platform.current_user_playing_track()

    def queue(self):
        return self._platorm.queue()

    def playlist_items(self, playlistid, offset, limit):
        return self.platform.playlist_items(
            playlistid, offset, limit
        )

    def playlist(self, playlistid, fields):
        return self.platform.playlist(playlistid, fields)

    def search(self, string):
        return self.platform.search(string)

    def track(self, uri):
        self.platform.track(uri)

    # from spotify helper

    @property
    def Settings(self):
        return self.platform.Settings

    @property
    def CacheHandler(self):
        return self.platform.CacheHandler

    @property
    def mp_is_none(self):
        return self.platform.mp_is_none

    @property
    def oauthErrorText(self):
        return self.platform.oauthErrorText

    @property
    def spotifyException(self):
        return self.platform.exception

    @property
    def spotifyExceptionWarning(self):
        return self.platform.exceptionWarning

    @property
    def callback_unhandled_exception(self):
        return self.platform.callback_unhandled_exception

    @property
    def callback_info(self):
        return self.platform.callback_info

    @property
    def callback_nocode(self):
        return self.platform.callback_nocode

    @property
    def callback_connected(self):
        return self.platform.callback_connected

    def add_to_queue(self, sp, uri_list):
        return self.platform.add_to_queue(sp, uri_list)

    def get_track_title(self, item):
        return self.platform.get_track_title(item)

    def apiFactory(self, auth_manager):
        return self.platform.apiFactory(auth_manager)

    def get_price(self, chat_id):
        return self.platform.get_price(chat_id)

    def set_price(self, price):
        return self.platform.set_price(price)

    def create_auth_manager(
        self, chat_id, client_id, client_secret
    ):
        return self.platform.create_auth_manager(
            chat_id, client_id, client_secret
        )

    def init_auth_manager(self, chat_id, client_id, client_secret):
        return self.platform.init_auth_manager(
            chat_id, client_id, client_secret
        )

    def get_auth_manager(self, chat_id):
        return self.platform.get_auth_manager(chat_id)

    def delete_auth_manager(self, chat_id):
        return self.platform.delete_auth_manager(chat_id)

    def save_settings(self, sps):
        return self.platform.save_settings(sps)

    def get_settings(self, userid):
        return self.get_settings(userid)

    def get_history(self, chat_id, maxlen):
        return self.platform.get_history(chat_id, maxlen)

    def update_history(self, chat_id: int, title: str):
        return self.platform.update_history(chat_id, title)

    def get_donation_fee(self, chat_id: int):
        return self.platform.get_donation_fee(chat_id)

    def set_donation_fee(self, chat_id: int, fee: int):
        return self.platform.set_donation_fee(chat_id, fee)

    def makeConnectMessage(self, uri):
        return self.platform.makeConnectMessage(self, uri)

    def validateSearch(self, searchstr):
        return self.platform.validateSearch(searchstr)

    def validateTrackId(self, track_id):
        return self.platform.validateTrackId(track_id)

    def addPrefix(self, track_id):
        return self.platform.addPrefix(track_id)

    def make_callback_infoText(self, chatid, userid, code):
        return self.platform.make_callback_infoText(
            chatid, userid, code
        )

    def addUriListToDict(self, userdata, value):
        return self.platform.addUriListToDict(userdata, value)

    def makeRedirectUri(self, domain):
        return self.platform.makeRedirectUri(domain)
