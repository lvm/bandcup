from bandcamp_dl.bandcamp import Bandcamp
from bandcamp_dl.bandcampdownloader import (
    BandcampDownloader as BandcampDownloaderBase
)
from os import environ as env
from worker import celery


class BandcampDownloader(BandcampDownloaderBase):
    def start(self, album: dict):
        """
        Note: The original class asks for user input
        when an album has 'private' songs, which prevents
        automatic downloads.
        This way will download an album in any way
        (with incomplete tracklists, though).
        """
        self.download_album(album)


download_dir = env.get("DOWNLOAD_DIR", "/download/").rstrip("/")
bandcamp = Bandcamp()

@celery.task(name='tasks.download')
def download(album_url: str) -> str:
    album = bandcamp.parse(album_url, True, False, False)
    bc_dl = BandcampDownloader(
        template="%{artist}/%{album}/%{track} - %{title}",
        directory=download_dir,
        overwrite=False,
        embed_lyrics=False,
        grouping=False,
        embed_art=False,
        no_slugify=False,
        debugging=False,
        urls=album_url
    )
    bc_dl.start(album)

    return "ok"
