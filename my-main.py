import os
import csv
from hotel import DataItem, DataHandler  # Assuming hotel.py contains the DataItem and DataHandler classes
from sorting_algorithms import BubbleSort, MergeSort  # Assuming sorting_algorithms.py contains sorting algorithms

# Main Functionality
def main():
    # Ensure the directory exists
    directory = "/Users/rigers/Desktop/final-project"  # Replace with your actual directory path
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)  # Create directory if it doesn't exist
            print(f"Directory created: {directory}")
        except PermissionError:
            print(f"PermissionError: Unable to create directory at {directory}. Check folder permissions.")
            return
    
    # File path for the CSV file
    file_path = os.path.join(directory, "hotels2.csv")  # Combine the directory path with the file name
    print(f"Attempting to load file from: {file_path}")

    # Load Data
    hotels = DataHandler.load_data(file_path)  # Load the data from the CSV file

    # Check if data was loaded successfully
    if not hotels:
        print("No data loaded. Exiting program.")
        return

    # Ask the user to select sorting algorithm
    print("Choose Sorting Algorithm:")
    print("1) Bubble Sort")
    print("2) Merge Sort")
    choice = input("Enter choice (1 or 2): ")

    # Instantiate the chosen sorting algorithm
    if choice == '1':
        sorter = BubbleSort()  # Use BubbleSort
    elif choice == '2':
        sorter = MergeSort()  # Use MergeSort
    else:
        print("Invalid choice. Exiting program.")
        return

    # Ask the user for the sorting key and order
    key = input("Enter sorting key (price, rating, availability): ").strip()
    if key not in ["price", "rating", "availability"]:
        print("Invalid sorting key. Exiting program.")
        return
    
    # Ask if they want to sort in ascending order
    order = input("Sort in ascending order? (yes/no): ").lower()
    if order not in ['yes', 'no']:
        print("Invalid order choice. Exiting program.")
        return

    ascending = (order == 'yes')

    # Sort the hotels based on the selected options
    sorted_hotels = sorter.sort(hotels, key, ascending)

    # Display sorted hotels
    print("\nSorted Hotels:")
    for hotel in sorted_hotels:
        print(f"{hotel.name} - Price: {hotel.price}, Rating: {hotel.rating}, "
              f"Availability: {hotel.availability}, Location: {hotel.location}")

if __name__ == "__main__":
    main()










