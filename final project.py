
#### Group Member 1: Object-Oriented Design & Data Handling
import csv
from abc import ABC, abstractmethod

# Core DataItem class
class DataItem:
    def __init__(self, hotel_id, name, location, price, rating, availability):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.price = price
        self.rating = rating
        self.availability = availability

    def __str__(self):
        return f"{self.name} ({self.location}) - ${self.price}/night, Rating: {self.rating}, Available: {self.availability}"

# Abstract SortingAlgorithm class
class SortingAlgorithm(ABC):
    @abstractmethod
    def sort(self, data, key, reverse=False):
        pass

# BubbleSort class
class BubbleSort(SortingAlgorithm):
    def sort(self, data, key, reverse=False):
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if (data[j][key] > data[j + 1][key]) != reverse:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data

# MergeSort class
class MergeSort(SortingAlgorithm):
    def sort(self, data, key, reverse=False):
        if len(data) > 1:
            mid = len(data) // 2
            left_half = data[:mid]
            right_half = data[mid:]

            self.sort(left_half, key, reverse)
            self.sort(right_half, key, reverse)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if (left_half[i][key] < right_half[j][key]) != reverse:
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                data[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                data[k] = right_half[j]
                j += 1
                k += 1
        return data

# DataHandler class for loading CSV data
class DataHandler:
    @staticmethod
    def load_data(file_path):
        data = []
        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row['price'] = float(row['price'])
                    row['rating'] = float(row['rating'])
                    row['availability'] = row['availability'].lower() == 'true'
                    data.append(row)
        except Exception as e:
            print(f"Error loading data: {e}")
        return data

### Group Member 2: Truth Table and Logical Complexity
class TruthTableEvaluator:
    @staticmethod
    def evaluate(item, expression):
        try:
            return eval(expression.format(**item))
        except Exception as e:
            print(f"Error evaluating expression: {e}")
            return False

    @staticmethod
    def filter_data(data, expression):
        filtered_data = []
        for item in data:
            if TruthTableEvaluator.evaluate(item, expression):
                filtered_data.append(item)
        return filtered_data

    @staticmethod
    def format_expression(expression):
        # Ensure logical expression formatting for better evaluation
        try:
            formatted_expression = expression.replace('and', ' and ').replace('or', ' or ').replace('not', ' not ')
            return formatted_expression
        except Exception as e:
            print(f"Error formatting expression: {e}")
            return expression

class PerformanceAnalyzer:
    @staticmethod
    def measure_time(func, *args):
        import time
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution Time: {execution_time:.4f} seconds")
        return result

    @staticmethod
    def compare_algorithms(data, sorting_algorithms, key):
        for algorithm in sorting_algorithms:
            print(f"Measuring performance of {algorithm.__class__.__name__}...")
            PerformanceAnalyzer.measure_time(algorithm.sort, data.copy(), key)

### Group Member 3: User Interaction
class UserInterface:
    def __init__(self, data):
        self.data = data

    def display_hotels(self):
        for hotel in self.data:
            print(f"{hotel['name']} ({hotel['location']}): ${hotel['price']}/night, Rating: {hotel['rating']}, Available: {hotel['availability']}")

    def sort_hotels(self):
        print("1. Sort by Price\n2. Sort by Rating\n3. Sort by Availability")
        choice = int(input("Choose a sorting criterion: "))
        key_map = {1: 'price', 2: 'rating', 3: 'availability'}
        key = key_map.get(choice, 'price')
        reverse = input("Sort in descending order? (yes/no): ").lower() == 'yes'

        print("Choose Sorting Algorithm:\n1. Bubble Sort\n2. Merge Sort")
        algorithm_choice = int(input("Enter your choice: "))
        sorting_algorithm = BubbleSort() if algorithm_choice == 1 else MergeSort()

        self.data = PerformanceAnalyzer.measure_time(sorting_algorithm.sort, self.data, key, reverse)
        self.display_hotels()

    def filter_hotels(self):
        expression = input("Enter a truth table condition (e.g., 'price < 150 and rating > 4.0'): ")
        expression = TruthTableEvaluator.format_expression(expression)
        filtered_data = PerformanceAnalyzer.measure_time(TruthTableEvaluator.filter_data, self.data, expression)
        print("Filtered Hotels:")
        for hotel in filtered_data:
            print(f"{hotel['name']} ({hotel['location']}): ${hotel['price']}/night, Rating: {hotel['rating']}, Available: {hotel['availability']}")

if __name__ == "__main__":
    data_file = "hotels.csv"  # Replace with your CSV file path
    data = DataHandler.load_data(data_file)

    if not data:
        print("No data available. Please check the file.")
        exit()

    ui = UserInterface(data)

    while True:
        print("\nHotel Booking System")
        print("1. View Hotels\n2. Sort Hotels\n3. Filter Hotels\n4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            ui.display_hotels()
        elif choice == 2:
            ui.sort_hotels()
        elif choice == 3:
            ui.filter_hotels()
        elif choice == 4:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")