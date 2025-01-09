import os
from Data_handling import DataHandler, DataItem
from accounts import AccountManager
from sorting_algorithms import sort_hotels
from utilities import save_to_csv
from truth_tables import TruthTableEvaluator  # Re-added truth tables

class HotelBookingSystem:
    def __init__(self, data_file):
        self.data_file = data_file
        self.hotels = self.load_hotels()
        self.bookings = []
        self.logged_in_user = None  # Track the logged-in user

    def load_hotels(self):
        """Load hotels using DataHandler."""
        data = DataHandler.load_data(self.data_file)  # Ensure this returns dictionaries
        if data and all(isinstance(row, dict) for row in data):
            hotels = [DataItem(**row) for row in data]  # Convert dictionaries to DataItem objects
            return hotels
        else:
            raise TypeError("DataHandler.load_data() must return a list of dictionaries.")

    def view_hotels(self):
        """Display all hotels."""
        if not self.hotels:
            print("No hotels available. Debug info: self.hotels is empty.")  # Debugging
            return
        for hotel in self.hotels:
            print(hotel)

    def filter_hotels(self):
        """Filter hotels based on various criteria, including city and country."""
        print("\nFilter Options:")
        print("1. By City")
        print("2. By Country")
        print("3. By Price Range")
        print("4. By Rating")
        print("5. By Logical Expression")  # Added logical expression filtering
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                city_name = input("Enter city name: ").strip().lower()
                results = [hotel for hotel in self.hotels if city_name in hotel.city.lower()]
            elif choice == "2":
                country_name = input("Enter country name: ").strip().lower()
                results = [hotel for hotel in self.hotels if country_name in hotel.country.lower()]
            elif choice == "3":
                min_price = float(input("Enter minimum price: ").strip())
                max_price = float(input("Enter maximum price: ").strip())
                results = [hotel for hotel in self.hotels if min_price <= hotel.price <= max_price]
            elif choice == "4":
                min_rating = float(input("Enter minimum rating (1-5): ").strip())
                results = [hotel for hotel in self.hotels if hotel.rating >= min_rating]
            elif choice == "5":
                expression = input("Enter logical expression (e.g., price < 100 and rating > 4.5): ").strip()
                formatted_expression = TruthTableEvaluator.format_expression(expression)
                results = TruthTableEvaluator.filter_data([hotel.__dict__ for hotel in self.hotels], formatted_expression)
                results = [DataItem(**hotel) for hotel in results]  # Convert back to DataItem objects
            else:
                print("Invalid choice.")
                return

            if results:
                print("\nFiltered Hotels:")
                for hotel in results:
                    print(hotel)
            else:
                print("No hotels found matching the filter.")
        except ValueError:
            print("Invalid input. Please try again.")
        except Exception as e:
            print(f"Error filtering hotels: {e}")

    def register_account(self):
        """Register a new account."""
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        AccountManager.register_account(username, password)

    def login(self):
        """Log in to an existing account."""
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        if AccountManager.authenticate(username, password):
            self.logged_in_user = username

    def view_bookings(self):
        """View bookings for the logged-in user."""
        if not self.logged_in_user:
            print("Please log in to view your bookings.")
            return

        print(f"Bookings for {self.logged_in_user}:")
        for booking in self.bookings:
            if booking["username"] == self.logged_in_user:
                print(booking)

    def book_hotel(self):
        """Book a hotel."""
        if not self.logged_in_user:
            print("Please log in to book a hotel.")
            return

        hotel_name = input("Enter the name of the hotel to book: ").strip()
        for hotel in self.hotels:
            if hotel.name.lower() == hotel_name.lower():
                booking = {
                    "username": self.logged_in_user,
                    "hotel_name": hotel.name,
                }
                self.bookings.append(booking)
                save_to_csv(self.bookings, "bookings.csv")
                print(f"Hotel '{hotel.name}' booked successfully!")
                return
        print("Hotel not found.")

if __name__ == "__main__":
    data_file = "hotels.csv"
    system = HotelBookingSystem(data_file)

    while True:
        print("\nHotel Booking System")
        print("1. Register Account")
        print("2. Login")
        print("3. View Hotels")
        print("4. Search Hotels")
        print("5. Filter Hotels")
        print("6. Sort Hotels")  # Added sorting option
        print("7. Book a Hotel")
        print("8. View Bookings")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            system.register_account()
        elif choice == "2":
            system.login()
        elif choice == "3":
            system.view_hotels()
        elif choice == "4":
            system.filter_hotels()
        elif choice == "5":
            system.filter_hotels()
        elif choice == "6":  # Sorting logic
            print("\nSort Options: name, price, rating, location")
            key = input("Enter sorting key: ").strip()
            reverse = input("Sort in descending order? (yes/no): ").strip().lower() == "yes"
            try:
                system.hotels = sort_hotels(system.hotels, key, reverse=reverse)
                print("\nHotels sorted successfully!")
                system.view_hotels()  # Display sorted hotels
            except Exception as e:
                print(f"Error sorting hotels: {e}")
        elif choice == "7":
            system.book_hotel()
        elif choice == "8":
            system.view_bookings()
        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
