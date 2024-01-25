from abc import ABC
from datetime import datetime

@ABC.register
class MovieTheaterInterface():
    """
    Interface for theaters to implement
    """
    _location = None


    def __init__(self) -> None:
        pass


class Movie:
    def __init__(self, language: str, genere: str, date: datetime, title: str) -> None:
        self.language = language 
        self.genere = genere 
        self.date = date 
        self.title = title 

class AuditoriumScreen:
    def __init__(self,seats: list, movie: Movie) -> None:
        self. movie = movie
        self.seats = seats


class Theater(MovieTheaterInterface):
    def __init__(self) -> None:
        pass