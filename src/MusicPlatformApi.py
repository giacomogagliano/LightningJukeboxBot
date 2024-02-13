from abc import ABC, abstractmethod, abstractproperty

tbi = "to be implemented"


class MusicPlatformApi(ABC):
    @abstractmethod
    def current_user_playing_track(self):
        print(tbi)

    @abstractmethod
    def queue(self):
        print(tbi)

    @abstractmethod
    def playlist_items(self, playlistid, offset, limit):
        print(tbi)

    @abstractmethod
    def playlist(self, playlistid, fields):
        print(tbi)

    @abstractmethod
    def search(self, string):
        print(tbi)

    @abstractmethod
    def track(self, uri):
        print(tbi)
