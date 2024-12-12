import csv  # Ensure you import the csv module

class HotelBookingSystem:
    def __init__(self, data_file):  # Constructor with correct initialization
        self.data_file = data_file
        self.data = []  # Initialize an empty list to store hotel data
        self.load_data()  # Load the data when the class is initialized

    def load_data(self):
        """Load and validate the CSV data."""
        try:
            with open(self.data_file, mode='r') as file:  # Open the file in read mode
                reader = csv.DictReader(file)  # Read the file as a dictionary
                for row in reader:  # Loop through each row in the CSV file
                    if self.validate_row(row):  # Validate the row data
                        self.data.append(row)  # Add valid rows to the data list
                    else:
                        print(f"Invalid data skipped: {row}")  # Print invalid rows
        except FileNotFoundError:
            print("Error: The specified data file does not exist.")
        except Exception as e:
            print(f"Unexpected error while loading data: {e}")

    @staticmethod
    def validate_row(row):
        """Validate a row from the CSV file."""
        required_fields = ["HotelName", "Price", "Rating", "Location"]
        try:
            # Ensure each required field exists and has valid data
            for field in required_fields:
                if field not in row or not row[field].strip():
                    return False  # If any field is missing or empty, return False
            # Ensure Price is a number and Rating is between 1 and 5
            if not row["Price"].isdigit() or not (1 <= int(row["Rating"]) <= 5):
                return False
            return True  # If all validations pass, return True
        except Exception:
            return False  # In case of any other errors, return False
