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
        self.bookings = []  # Store bookings in memory

    def load_data(self):
        """Load hotel data from CSV."""
        try:
            with open(self.data_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
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
                    return False
            if not row["Price"].replace('.', '', 1).isdigit() or not (1 <= float(row["Rating"]) <= 5):
                return False
            return True
        except Exception:
            return False

    def view_hotels(self):
        """Display all hotels in a formatted table."""
        if not self.data:
            print("No hotels available.")
            return
        print(f"{'Hotel Name':<25}{'Price':<10}{'Rating':<10}{'Location':<15}")
        print("-" * 60)
        for hotel in self.data:
            print(f"{hotel['HotelName']:<25}${hotel['Price']:<10}{hotel['Rating']:<10}{hotel['Location']:<15}")

    def filter_hotels(self):
        """Filter hotels based on user input."""
        try:
            max_price = input("Enter maximum price (or press Enter to skip): ")
            min_rating = input("Enter minimum rating (1-5, or press Enter to skip): ")
            location = input("Enter location (or press Enter to skip): ")

            # Clean the inputs
            max_price = ''.join(c for c in max_price if c.isdigit() or c == '.') if max_price else None
            min_rating = ''.join(c for c in min_rating if c.isdigit() or c == '.') if min_rating else None

            # Validate rating range
            if min_rating and (float(min_rating) < 1 or float(min_rating) > 5):
                print("Error: Rating must be between 1 and 5.")
                return

            conditions = {}
            if max_price:
                conditions["Price"] = lambda x: float(x) <= float(max_price)
            if min_rating:
                conditions["Rating"] = lambda x: float(x) >= float(min_rating)
            if location:
                conditions["Location"] = lambda x: location.lower() in x.lower()

            filtered_data = filter_hotels(self.data, conditions)
            if not filtered_data:
                print("No matching hotels found.")
            else:
                print(f"{'Hotel Name':<25}{'Price':<10}{'Rating':<10}{'Location':<15}")
                print("-" * 60)
                for hotel in filtered_data:
                    print(f"{hotel['HotelName']:<25}${hotel['Price']:<10}{hotel['Rating']:<10}{hotel['Location']:<15}")
        except ValueError as e:
            print(f"Error in input: {e}")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")

    def sort_hotels(self):
        """Sort hotels based on user choice."""
        key = input("Enter sorting key (Price, Rating, Location): ").strip()
        order = input("Sort in descending order? (yes/no): ").strip().lower() == "yes"
        sorted_data = sort_hotels(self.data, key, reverse=order)
        if not sorted_data:
            print("No hotels to sort.")
        else:
            print(f"{'Hotel Name':<25}{'Price':<10}{'Rating':<10}{'Location':<15}")
            print("-" * 60)
            for hotel in sorted_data:
                print(f"{hotel['HotelName']:<25}${hotel['Price']:<10}{hotel['Rating']:<10}{hotel['Location']:<15}")

    def book_hotel(self):
        """Book a hotel and save it."""
        hotel_name = input("Enter the name of the hotel to book: ").strip()
        for hotel in self.data:
            if hotel["HotelName"].lower() == hotel_name.lower():
                self.bookings.append(hotel)
                save_to_csv(self.bookings, "bookings.csv")
                print(f"Hotel '{hotel_name}' booked successfully!")
                return
        print(f"Hotel '{hotel_name}' not found.")

if __name__ == "__main__":
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_file = os.path.join(current_dir, "hotels.csv")
        system = HotelBookingSystem(data_file)

        # Console menu for interaction
        while True:
            print("\nHotel Booking System")
            print("1. View Hotels")
            print("2. Filter Hotels")
            print("3. Sort Hotels")
            print("4. Book a Hotel")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                system.view_hotels()
            elif choice == "2":
                system.filter_hotels()
            elif choice == "3":
                system.sort_hotels()
            elif choice == "4":
                system.book_hotel()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
