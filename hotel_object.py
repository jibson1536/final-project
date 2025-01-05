

from abc import ABC, abstractmethod

# Abstract class for Hotel
class Hotel(ABC):
    def _init_(self, name, city_id):
        self.name = name
        self.city_id = city_id

    @abstractmethod
    def get_details(self):
        pass


# Guesthouse class inheriting from Hotel
class Guesthouse(Hotel):
    def _init_(self, name, city_id, guest_capacity):
        super()._init_(name, city_id)
        self.guest_capacity = guest_capacity

    def get_details(self):
        return f"Guesthouse: {self.name}, City ID: {self.city_id}, Capacity: {self.guest_capacity}"


# Apartment class inheriting from Hotel
class Apartment(Hotel):
    def _init_(self, name, city_id, number_of_units):
        super()._init_(name, city_id)
        self.number_of_units = number_of_units

    def get_details(self):
        return f"Apartment: {self.name}, City ID: {self.city_id}, Units: {self.number_of_units}"


# Single Apartment inheriting from Apartment
class SingleApartment(Apartment):
    def _init_(self, name, city_id, unit_size):
        super()._init_(name, city_id, 1)  # Single Apartment has only 1 unit
        self.unit_size = unit_size

    def get_details(self):
        return f"Single Apartment: {self.name}, City ID: {self.city_id}, Size: {self.unit_size} sq ft"


# Double Apartment inheriting from Apartment
class DoubleApartment(Apartment):
    def _init_(self, name, city_id, unit_sizes):
        super()._init_(name, city_id, 2)  # Double Apartment has 2 units
        self.unit_sizes = unit_sizes  # List of sizes for the two units

    def get_details(self):
        return f"Double Apartment: {self.name}, City ID: {self.city_id}, Sizes: {self.unit_sizes}"


# Penthouse class inheriting from Apartment
class Penthouse(Apartment):
    def _init_(self, name, city_id, number_of_units, luxury_amenities, premium_price):
        super()._init_(name, city_id, number_of_units)
        self.luxury_amenities = luxury_amenities  # List of luxury amenities
        self.premium_price = premium_price  # Extra price for the penthouse

    def get_details(self):
        return (
            f"Penthouse: {self.name}, City ID: {self.city_id}, Units: {self.number_of_units}, "
            f"Luxury Amenities: {', '.join(self.luxury_amenities)}, Premium Price: {self.premium_price}"
        )


# Country class
class Country:
    def _init_(self, country_id, name):
        self.country_id = country_id
        self.name = name


# City class
class City:
    def _init_(self, city_id, name, country_id):
        self.city_id = city_id
        self.name = name
        self.country_id = country_id