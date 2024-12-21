import csv
import os
import sys
from data_loader import load_data, validate_row
from filters import filter_hotels, search_hotels
from sorters import sort_hotels
from utilities import format_display, save_to_csv

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
                    if validate_row(row):  # Validate the row data
                        self.data.append(row)  # Add valid rows to the data list
                    else:
                        print(f"Invalid data skipped: {row}")  # Print invalid rows
        except FileNotFoundError:
            print("Error: The specified data file does not exist.")
        except Exception as e:
            print(f"Unexpected error while loading data: {e}")

    def menu(self):
        """Interactive menu for users."""
        while True:
            print("\nHotel Booking System Menu:")
            print("1. View all hotels")
            print("2. Search hotels")
            print("3. Filter hotels")
            print("4. Sort hotels")
            print("5. Save results to CSV")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                format_display(self.data)

            elif choice == "2":
                search_term = input("Enter hotel name or location to search: ")
                results = search_hotels(self.data, search_term)
                format_display(results)

            elif choice == "3":
                conditions = {}
                price_filter = input("Enter max price (or press Enter to skip): ")
                if price_filter:
                    conditions["Price"] = lambda x: int(x) <= int(price_filter)

                rating_filter = input("Enter minimum rating (1-5, or press Enter to skip): ")
                if rating_filter:
                    conditions["Rating"] = lambda x: int(x) >= int(rating_filter)

                location_filter = input("Enter location (or press Enter to skip): ")
                if location_filter:
                    conditions["Location"] = lambda x: location_filter.lower() in x.lower()

                filtered_hotels = filter_hotels(self.data, conditions)
                format_display(filtered_hotels)

            elif choice == "4":
                keys = input("Enter sorting keys (e.g., Price, Rating): ").split(',')
                order = input("Sort in descending order? (yes/no): ").lower() == "yes"
                sorted_data = sort_hotels(self.data, keys, reverse=order)
                format_display(sorted_data)

            elif choice == "5":
                file_name = input("Enter file name to save results (e.g., results.csv): ")
                save_to_csv(self.data, file_name)

            elif choice == "6":
                print("Exiting the system. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    try:
        # Ensure that the directory containing the module files is in sys.path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        sys.path.append(current_dir)

        data_file = input("Enter the path to the hotel dataset CSV file: ")
        system = HotelBookingSystem(data_file)
        system.menu()
    except ModuleNotFoundError as e:
        print(f"ModuleNotFoundError: {e}. Ensure all required modules are in the same directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
