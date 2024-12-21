import csv

def format_display(hotels):
    """Display hotel data in a user-friendly format."""
    if not hotels:
        print("No matching hotels found.")
        return
    print("\nMatching Hotels:")
    for hotel in hotels:
        print(f"{hotel['HotelName']} - Price: ${hotel['Price']}, Rating: {hotel['Rating']}/5, Location: {hotel['Location']}")

def save_to_csv(data, file_name):
    """Save filtered/sorted data to a CSV file."""
    try:
        with open(file_name, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["HotelName", "Price", "Rating", "Location"])
            writer.writeheader()
            writer.writerows(data)
        print(f"Results saved to {file_name}")
    except Exception as e:
        print(f"Error saving file: {e}")
