import time

# Sorting Algorithms
class BubbleSort:
    def sort(self, data, key, reverse=False):
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if (data[j][key] > data[j + 1][key]) != reverse:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data

class MergeSort:
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

# Truth Table Evaluator
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

# Performance Analyzer
class PerformanceAnalyzer:
    @staticmethod
    def measure_execution_time(sort_function, data, key, reverse):
        start_time = time.time()
        sorted_data = sort_function(data, key, reverse)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution Time: {execution_time:.4f} seconds")
        return sorted_data, execution_time

    @staticmethod
    def compare_algorithms(bubble_sort, merge_sort, data, key):
        print("Comparing Performance of Bubble Sort and Merge Sort...")
        print("Running Bubble Sort...")
        bubble_sorted, bubble_time = PerformanceAnalyzer.measure_execution_time(bubble_sort.sort, data.copy(), key, False)
        print("Running Merge Sort...")
        merge_sorted, merge_time = PerformanceAnalyzer.measure_execution_time(merge_sort.sort, data.copy(), key, False)
        if bubble_time < merge_time:
            print(f"Bubble Sort is faster by {merge_time - bubble_time:.4f} seconds")
        else:
            print(f"Merge Sort is faster by {bubble_time - merge_time:.4f} seconds")
        return bubble_sorted, merge_sorted

# User Interface
class UserInterface:
    def __init__(self, data):
        # Ensure data is a list of dictionaries with proper keys
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

        # Measure execution time
        start_time = time.time()
        self.data = sorting_algorithm.sort(self.data, key, reverse)
        end_time = time.time()

        print(f"Sorting completed in {end_time - start_time:.4f} seconds")
        self.display_hotels()

    def filter_hotels(self):
        expression = input("Enter a truth table condition (e.g., 'price < 150 and rating > 4.0'): ")
        filtered_data = TruthTableEvaluator.filter_data(self.data, expression)
        print("Filtered Hotels:")
        for hotel in filtered_data:
            print(f"{hotel['name']} ({hotel['location']}): ${hotel['price']}/night, Rating: {hotel['rating']}, Available: {hotel['availability']}")

    def compare_sorting_algorithms(self):
        key = input("Enter sorting criterion (price/rating/availability): ")
        bubble_sort = BubbleSort()
        merge_sort = MergeSort()
        PerformanceAnalyzer.compare_algorithms(bubble_sort, merge_sort, self.data, key)

if __name__ == "__main__":
    # Sample data for testing
    data = [
        {'name': 'Hotel A', 'location': 'City X', 'price': 120, 'rating': 4.5, 'availability': True},
        {'name': 'Hotel B', 'location': 'City Y', 'price': 100, 'rating': 4.0, 'availability': False},
        {'name': 'Hotel C', 'location': 'City Z', 'price': 200, 'rating': 5.0, 'availability': True}
    ]

    ui = UserInterface(data)

    while True:
        print("\nHotel Booking System")
        print("1. View Hotels\n2. Sort Hotels\n3. Filter Hotels\n4. Compare Sorting Algorithms\n5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            ui.display_hotels()
        elif choice == 2:
            ui.sort_hotels()
        elif choice == 3:
            ui.filter_hotels()
        elif choice == 4:
            ui.compare_sorting_algorithms()
        elif choice == 5:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
