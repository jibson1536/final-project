# sorting.py
def sort_hotels_by_city_id(hotels):
    """Sort a list of hotels by their city_id."""
    return sorted(hotels, key=lambda h: h.city_id)

def sort_hotels_by_name(hotels):
    """Sort a list of hotels by their name."""
    return sorted(hotels, key=lambda h: h.name)
