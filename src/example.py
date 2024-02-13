# costruire un adapter
# costruire una strategia per il x


# Da simulare
class Spotify:
    def add_to_queue(self) -> None:
        return "spotify added"


# Da adattare
class Audius:
    def audiusadd(self):
        return "audius added"


# Adattatore
class MusicPlatform(Spotify, Audius):
    """
    this class adapts the class to be adapted to the Target
    """

    def add_to_queue(self) -> str:
        return self.audiusadd()


class MusicPlatformHandler:
    def __init__(self, platform: MusicPlatform) -> None:
        self._platform = platform

    @property
    def platform(self) -> MusicPlatform:
        return self._platform

    @platform.setter
    def platform(self, platform: MusicPlatform) -> None:
        self._platform = platform

    def add_to_queue(self):
        return self._platform.add_to_queue()


if __name__ == "__main__":
    musicplatformhandler = MusicPlatformHandler(Spotify())
    print(musicplatformhandler.add_to_queue())
    musicplatformhandler.platform = MusicPlatform()
    print(musicplatformhandler.add_to_queue())
