from abc import ABC, abstractmethod

# Abstract class for Hotel
class Hotel(ABC):
    def __init__(self, name, city_id):
        self.name = name
        self.city_id = city_id

    @abstractmethod
    def get_details(self):
        """Abstract method to return hotel details."""
        pass


# Guesthouse class inheriting from Hotel
class Guesthouse(Hotel):
    def __init__(self, name, city_id, guest_capacity):
        super().__init__(name, city_id)
        self.guest_capacity = guest_capacity

    def get_details(self):
        return f"Guesthouse: {self.name}, City ID: {self.city_id}, Capacity: {self.guest_capacity}"


# Apartment class inheriting from Hotel
class Apartment(Hotel):
    def __init__(self, name, city_id, number_of_units):
        super().__init__(name, city_id)
        self.number_of_units = number_of_units

    def get_details(self):
        return f"Apartment: {self.name}, City ID: {self.city_id}, Units: {self.number_of_units}"


# Penthouse class inheriting from Apartment
class Penthouse(Apartment):
    def __init__(self, name, city_id, number_of_units, luxury_amenities, premium_price):
        super().__init__(name, city_id, number_of_units)
        self.luxury_amenities = luxury_amenities
        self.premium_price = premium_price

    def get_details(self):
        return (
            f"Penthouse: {self.name}, City ID: {self.city_id}, Units: {self.number_of_units}, "
            f"Luxury Amenities: {', '.join(self.luxury_amenities)}, Premium Price: {self.premium_price}"
        )


# Example of how these classes can be used
if __name__ == "__main__":
    guesthouse = Guesthouse("Cozy Stay", 101, 15)
    apartment = Apartment("Urban Nest", 102, 5)
    penthouse = Penthouse(
        "Skyline View", 103, 1, ["Infinity Pool", "Private Elevator"], 5000
    )

    print(guesthouse.get_details())
    print(apartment.get_details())
    print(penthouse.get_details())
