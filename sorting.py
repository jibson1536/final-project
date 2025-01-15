def sort_hotels_by_name(hotels, reverse=False):
    return sorted(hotels, key=lambda hotel: hotel.name, reverse=reverse)

def sort_hotels_by_city_id(hotels, reverse=False):
    return sorted(hotels, key=lambda hotel: hotel.city_id, reverse=reverse)

def sort_hotels_by_custom_attribute(hotels, attribute, reverse=False):
    try:
        return sorted(hotels, key=lambda hotel: getattr(hotel, attribute), reverse=reverse)
    except AttributeError:
        print(f"Error: Attribute '{attribute}' does not exist in the hotel objects.")
        return None
