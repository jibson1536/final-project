def filter_hotels(data, conditions):
    """Filter hotels based on conditions."""
    filtered = []
    for hotel in data:
        if all(conditions.get(key, lambda x: True)(hotel[key]) for key in conditions):
            filtered.append(hotel)
    return filtered
