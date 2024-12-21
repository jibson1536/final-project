def sort_hotels(data, keys, reverse=False):
    """Sort hotels by multiple keys."""
    try:
        for key in reversed(keys):  # Apply sorting for each key in reverse order
            data = sorted(data, key=lambda x: x[key], reverse=reverse)
        return data
    except KeyError as e:
        print(f"Error: Cannot sort by {e}. Invalid field.")
        return data
