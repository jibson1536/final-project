

from abc import ABC, abstractmethod

# Abstract class for Hotel
class Hotel(ABC):
    def __init__(self, name, city_id):
        self.name = name
        self.city_id = city_id

    @abstractmethod
    def get_details(self):
        pass
