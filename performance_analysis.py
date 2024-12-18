import time

class PerformanceAnalyzer:
    
    def measure_execution_time(sort_function, data, key, reverse):
        start_time = time.time()
        sorted_data = sort_function(data, key, reverse)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution Time: {execution_time:.4f} seconds")
        return sorted_data, execution_time

    
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


