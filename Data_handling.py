import csv

class DataItem:
    def __init__(self, hotel_id, name, location, price, rating, city, country, availability):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.price = price
        self.rating = rating
        self.city = city
        self.country = country
        self.availability = availability  # New field

    def __str__(self):
        return (
            f"{self.name} ({self.location}, {self.city}, {self.country}) - "
            f"${self.price}/night, Rating: {self.rating}, Available: {self.availability}"
        )

class DataHandler:
    @staticmethod
    def load_data(file_path):
        data = []
        try:
            with open(file_path, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Convert fields to appropriate types
                    row["price"] = float(row["price"])
                    row["rating"] = float(row["rating"])
                    row["availability"] = row["availability"].lower() == "true"  # Convert to boolean
                    data.append(row)  # Keep as dictionaries
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
        except Exception as e:
            print(f"Error loading data: {e}")
        return data
