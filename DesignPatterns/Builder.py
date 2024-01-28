from abc import ABC, abstractmethod

"""
Use / Motivation -->
    1.  To get rid of Telescopic contructor
    2. To build objects step by step

class Pizza {
    Pizza(int size) { ... }
    Pizza(int size, boolean cheese) { ... }
    Pizza(int size, boolean cheese, boolean pepperoni) { ... }
    // ...
"""
class Car:
    def __init__(self) -> None:
        pass


class BuilderInterface(ABC):
    def set_seats(self, *args, **kwargs):
        pass

    def set_engine(self, *args, **kwargs):
        pass

    def set_chassey(self, *args, **kwargs):
        pass

    def set_Infotainment(self, *args, **kwargs):
        pass


class CarBuilder(BuilderInterface):
    def set_chassey(self, chassey_details):
        pass

    def set_seats(self,seats):
        pass

    def set_ending(self, ending):
        pass
    
    def set_Infotainment(self, *args, **kwargs):
        pass

class ManualCarBuilder(BuilderInterface):
    _maual = 'Mauanl'
    def set_chassey(self, chassey_details):
        pass

    def set_seats(self,seats):
        pass

    def set_ending(self, ending):
        pass
    
    def set_Infotainment(self, *args, **kwargs):
        pass



class CarDirector:

    def construct_sports_car(self, builder: BuilderInterface):
        print('Constructing sport car..')
        
    def construct_SUV(self, builder: BuilderInterface):
        print('Constructing SUV..')