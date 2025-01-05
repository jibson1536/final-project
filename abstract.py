

from abc import ABC, abstractmethod

# Abstract class for Hotel
class Hotel(ABC):
    def __init__(self, name, city_id):
        self.name = name
        self.city_id = city_id

    @abstractmethod
    def get_details(self):
        pass
class Guesthouse(Hotel):
    def __init__(self, name, city_id, guest_capacity):
        super().__init__(name, city_id)
        self.guest_capacity = guest_capacity

    def get_details(self):
        return f"Guesthouse: {self.name}, City ID: {self.city_id}, Capacity: {self.guest_capacity}"