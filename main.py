import os
import csv
from filters import filter_hotels
from sorters import sort_hotels
from utilities import save_to_csv

class HotelBookingSystem:
    def __init__(self, data_file):
        self.data_file = data_file
        self.data = []  # Initialize an empty list to store hotel data
        self.load_data()

    def load_data(self):
        """Load hotel data from CSV."""
        try:
            with open(self.data_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    print(f"Row read: {row}")  # Debugging line
                    if self.validate_row(row):
                        self.data.append(row)
                    else:
                        print(f"Invalid data skipped: {row}")
        except FileNotFoundError:
            print(f"Error: {self.data_file} not found.")
        except Exception as e:
            print(f"Unexpected error while loading data: {e}")

    def validate_row(self, row):
        """Validate a row from the CSV file."""
        required_fields = ["HotelName", "Price", "Rating", "Location"]
        try:
            for field in required_fields:
                if field not in row or not row[field].strip():
                    print(f"Missing or empty field in row: {row}")
                    return False
            if not row["Price"].replace('.', '', 1).isdigit():
                print(f"Invalid Price in row: {row}")
                return False
            if not (1 <= float(row["Rating"]) <= 5):
                print(f"Invalid Rating in row: {row}")
                return False
            return True
        except Exception as e:
            print(f"Error validating row {row}: {e}")
            return False

    def view_hotels(self):
        """Display all hotels."""
        if not self.data:
            print("No hotels available.")
        for hotel in self.data:
            print(f"{hotel['HotelName']} - ${hotel['Price']} - {hotel['Rating']}/5")

    def filter_hotels(self):
        """Filter hotels and display results."""
        filtered_data = filter_hotels(self.data, {"Price": lambda x: float(x) <= 200})
        if not filtered_data:
            print("No matching hotels found.")
        for hotel in filtered_data:
            print(f"{hotel['HotelName']} - ${hotel['Price']} - {hotel['Rating']}/5")

    def sort_hotels(self):
        """Sort hotels and display results."""
        sorted_data = sort_hotels(self.data, "Price")
        if not sorted_data:
            print("No hotels to sort.")
        for hotel in sorted_data:
            print(f"{hotel['HotelName']} - ${hotel['Price']} - {hotel['Rating']}/5")

if __name__ == "__main__":
    try:
        # Load hotel data
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_file = os.path.join(current_dir, "hotels.csv")
        system = HotelBookingSystem(data_file)

        # Console menu for interaction
        while True:
            print("\nHotel Booking System")
            print("1. View Hotels")
            print("2. Filter Hotels")
            print("3. Sort Hotels")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                system.view_hotels()
            elif choice == "2":
                system.filter_hotels()
            elif choice == "3":
                system.sort_hotels()
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
