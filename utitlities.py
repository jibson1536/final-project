def format_display(hotels):
    """Display hotel data in a user-friendly format."""
    if not hotels:
        print("No matching hotels found.")
        return
    print("\nMatching Hotels:")
    for hotel in hotels:
        print(f"{hotel['HotelName']} - Price: ${hotel['Price']}, Rating: {hotel['Rating']}/5, Location: {hotel['Location']}")
