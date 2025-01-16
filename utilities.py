import csv

def format_display(hotels):
    """Display hotel data in a user-friendly format."""
    if not hotels:
        print("No matching hotels found.")
        return
    print("\nMatching Hotels:")
    for hotel in hotels:
        print(f"{hotel['HotelName']} - Price: ${hotel['Price']}, Rating: {hotel['Rating']}/5, Location: {hotel['Location']}")

import os

def save_to_csv(data, file_path):
    try:
        # Ensure the file path exists
        file_exists = os.path.isfile(file_path)

        # Get the headers dynamically from the first item's keys
        headers = data[0].keys() if data else []

        with open(file_path, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=headers)

            # Write the header only if the file doesn't exist
            if not file_exists:
                writer.writeheader()

            # Write all data
            writer.writerows(data)

    except Exception as e:
        print(f"Error saving file: {e}")