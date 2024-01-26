from abc import ABC
from datetime import datetime


class Movie:
    def __init__(self, language: str, genere: str, date: datetime, title: str) -> None:
        self.language = language
        self.genere = genere
        self.date = date
        self.title = title

# class AuditoriumScreen:
#     def __init__(self, sessions: list) -> None:
#         _session = self.get_session()
#         possible_time_slices = []


# class SeatingArrangementHandler:
#     """Create sitting arrangement for the people"""
#     def __init__(self, occupancy) -> None:
#         self.seats = [None for x in occupancy]
    
#     def fill_seats(self, seatsNums: list):
#         fill_possible = True
#         for each in seatsNums:
#             if each is not None:
#                 return False
#         return True


class MovieSession:
    def __init__(self, start_time: datetime, end_time: datetime, movie: Movie) -> None:
        self.start_time = start_time
        self.end_time = end_time
        self.movie = movie

class Theater:
    def __init__(self) -> None:
        self.locaiton = 0, 0
        self.auditoriums = []

    def addAuditorium(self, auditorium: AuditoriumScreen):
        self.auditoriums.append(auditorium)

    



