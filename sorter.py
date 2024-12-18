def sort_hotels(data, key, reverse=False):
    """Sort hotels based on a given key."""
    try:
        return sorted(data, key=lambda x: x[key], reverse=reverse)
    except KeyError:
        print(f"Error: Cannot sort by {key}. Invalid field.")
        return data
