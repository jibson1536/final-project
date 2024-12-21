import csv

def load_data(data_file):
    """Load and validate the CSV data."""
    data = []
    try:
        with open(data_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if validate_row(row):
                    data.append(row)
                else:
                    print(f"Invalid data skipped: {row}")
    except FileNotFoundError:
        print("Error: The specified data file does not exist.")
    except Exception as e:
        print(f"Unexpected error while loading data: {e}")
    return data

def validate_row(row):
    """Validate a row from the CSV file."""
    required_fields = ["HotelName", "Price", "Rating", "Location"]
    try:
        for field in required_fields:
            if field not in row or not row[field].strip():
                return False
        if not row["Price"].isdigit() or int(row["Price"]) < 0:
            return False
        if not (1 <= int(row["Rating"]) <= 5):
            return False
        return True
    except Exception:
        return False

