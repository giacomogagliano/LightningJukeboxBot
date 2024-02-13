from abc import ABC, abstractmethod, abstractproperty

tbi = "to be implemented"
bar = "bar"


class MusicPlatform(ABC):

    @abstractproperty
    def OAuth(self):
        pass

    # from spotipy
    @abstractproperty
    def OauthError(self):
        pass

    @abstractproperty
    def Exception(self):
        pass

    # from spotify helper

    @abstractproperty
    def Settings(self):
        pass

    @abstractproperty
    def CacheHandler(self):
        pass

    @abstractproperty
    def mp_is_none(self):
        pass

    @abstractproperty
    def oauthErrorText(self):
        pass

    @abstractproperty
    def exception(self):
        pass

    @abstractproperty
    def exceptionWarning(self):
        pass

    @abstractproperty
    def callback_unhandled_exception(self):
        pass

    @abstractproperty
    def callback_info(self):
        pass

    @abstractproperty
    def callback_nocode(self):
        pass

    @abstractproperty
    def callback_connected(self):
        pass

    @abstractmethod
    def add_to_queue(self, sp, uri_list):
        print(tbi)

    @abstractmethod
    def get_track_title(self, item):
        print(tbi)

    @abstractmethod
    def apiFactory(self, auth_manager):
        print(tbi)

    @abstractmethod
    def get_price(self, chat_id):
        print(tbi)

    @abstractmethod
    def set_price(self, price):
        print(tbi)

    @abstractmethod
    def create_auth_manager(
        self, chat_id, client_id, client_secret
    ):
        print(tbi)

    @abstractmethod
    def init_auth_manager(self, chat_id, client_id, client_secret):
        print(tbi)

    @abstractmethod
    def get_auth_manager(self, chat_id):
        print(tbi)

    @abstractmethod
    def delete_auth_manager(self, chat_id):
        print(tbi)

    @abstractmethod
    def save_settings(self, sps):
        print(tbi)

    @abstractmethod
    def get_settings(self, userid):
        print(tbi)

    @abstractmethod
    def get_history(self, chat_id, maxlen):
        print(tbi)

    @abstractmethod
    def update_history(self, chat_id: int, title: str):
        print(tbi)

    @abstractmethod
    def get_donation_fee(self, chat_id: int):
        print(tbi)

    @abstractmethod
    def set_donation_fee(self, chat_id: int, fee: int):
        print(tbi)

    @abstractmethod
    def makeConnectMessage(self, uri):
        print(tbi)

    @abstractmethod
    def validateSearch(self, searchstr):
        print(tbi)

    @abstractmethod
    def validateTrackId(self, track_id):
        print(tbi)

    @abstractmethod
    def addPrefix(self, track_id):
        print(tbi)

    @abstractmethod
    def make_callback_infoText(self, chatid, userid, code):
        print(tbi)

    @abstractmethod
    def addUriListToDict(self, userdata, value):
        print(tbi)

    @abstractmethod
    def makeRedirectUri(self, domain):
        print(tbi)
