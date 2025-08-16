# __author__ = "midhun" or "Qyrhal"
# 
#  Simple object representation of a song in order to grab state easily.
#  private access mutator indicated with a _ before the function name 
from utils.logger import Logger

from pathlib import Path



# used for each song
# Usage:
# song = Song("Shake it off", 180, Path("/path/to/shakeitoff.jpg"), Path("/path/to/shakeitoff.mp3"))
class Song: 

    def __init__(self, album_name :str="Untitled", song_duration : int= 0, path_to_song_cover : str = "", path_to_song : str = ""):
        self._logger = Logger(__name__)
        self._song_name : str = album_name
        self._song_duration : int =  self._validate_duration(song_duration) # done in seconds
        self._path_to_song_cover : str = str(path_to_song_cover)
        self._path_to_song : str = str(path_to_song)

    @property
    def song_name(self) -> str: 
        return self._song_name

    @property
    def song_duration(self) -> int: 
        return self._song_duration

    @property
    def path_to_song_cover(self) -> str: 
        return self._path_to_song_cover

    @property
    def path_to_song(self) -> str: 
        return self._path_to_song
    
    # def validation methods to make sure song is processesed correcttly

    def _validate_duration(self, duration: int) -> int:
        if duration < 0: 
            raise ValueError("Duration must be a positive integer, Cannot have a negative integer")
        return duration
    

