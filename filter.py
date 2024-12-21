def filter_hotels(data, conditions):
    """Filter hotels based on conditions."""
    filtered = []
    for hotel in data:
        if all(conditions.get(key, lambda x: True)(hotel[key]) for key in conditions):
            filtered.append(hotel)
    return filtered

def search_hotels(data, search_term):
    """Search hotels by name or location."""
    return [hotel for hotel in data if search_term.lower() in hotel['HotelName'].lower() or search_term.lower() in hotel['Location'].lower()]
