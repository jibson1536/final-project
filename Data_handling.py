import csv

class DataItem:
    def __init__(self, hotel_id, name, location, price, rating, availability):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.price = price
        self.rating = rating
        self.availability = availability

    def __str__(self):
        return f"{self.name} ({self.location}) - ${self.price}/night, Rating: {self.rating}, Available: {self.availability}"

class DataHandler:
    @staticmethod
    def load_data(file_path):
        data = []
        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row['price'] = float(row['price'])
                    row['rating'] = float(row['rating'])
                    row['availability'] = row['availability'].lower() == 'true'
                    data.append(row)
        except Exception as e:
            print(f"Error loading data: {e}")
        return data
