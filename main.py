class Hotel:
    def __init__(self, name, city, country, price, rating, is_available):
        self.name = name
        self.city = city
        self.country = country
        self.price = price
        self.rating = rating
        self.is_available = is_available

    def __repr__(self):
        return f"{self.name} ({self.city}, {self.country}) - ${self.price}, Rating: {self.rating}, Available: {self.is_available}"

def filter_hotels(hotels, min_rating=1, available_only=False):
    """Filter hotels by minimum rating and availability."""
    filtered_hotels = []
    for hotel in hotels:
        if hotel.rating >= min_rating:
            if not available_only or hotel.is_available:
                filtered_hotels.append(hotel)
    return filtered_hotels

def sort_hotels(hotels, key, descending=False):
    """Sort hotels based on the specified key."""
    try:
        return sorted(hotels, key=lambda x: getattr(x, key), reverse=descending)
    except AttributeError:
        print(f"Error: Invalid sorting key '{key}'")
        return hotels

def display_menu():
    """Display the main menu."""
    print("Hotel Booking System")
    print("1. Register Account")
    print("2. Login")
    print("3. View Hotels")
    print("4. Search Hotels")
    print("5. Filter Hotels")
    print("6. Sort Hotels")
    print("7. Book a Hotel")
    print("8. View Bookings")
    print("9. Exit")

if __name__ == "__main__":
    # Example Hotel Data
    hotels = [
        Hotel("Hotel A", "City X", "Country Y", 150, 4.5, True),
        Hotel("Hotel B", "City Y", "Country Z", 200, 4.0, False),
        Hotel("Hotel C", "City X", "Country Y", 120, 4.7, True),
        Hotel("Hotel D", "City Z", "Country Z", 300, 4.8, True),
    ]

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "4":  # Filter Hotels
            print("\nFilter Options:")
            print("1. By City")
            print("2. By Country")
            print("3. By Price Range")
            print("4. By Rating")
            print("5. By Logical Expression")

            filter_choice = input("Enter your choice: ")

            if filter_choice == "4":  # Filter by Rating
                min_rating = float(input("Enter minimum rating (1-5): "))
                available_only = input("Do you want to view only available hotels? (yes/no): ").strip().lower() == "yes"

                # Filter Hotels
                filtered_hotels = filter_hotels(hotels, min_rating, available_only)

                sort_choice = input("Do you want to sort the results? (yes/no): ").strip().lower()
                if sort_choice == "yes":
                    print("\nSort Options: name, price, rating, location")
                    sort_key = input("Enter sorting key: ").strip()
                    descending = input("Sort in descending order? (yes/no): ").strip().lower() == "yes"

                    # Sort Hotels
                    filtered_hotels = sort_hotels(filtered_hotels, sort_key, descending)

                # Display Results
                print("\nFiltered and Sorted Hotels:")
                for hotel in filtered_hotels:
                    print(hotel)

        elif choice == "9":  # Exit
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Option not implemented yet. Please choose another.")
