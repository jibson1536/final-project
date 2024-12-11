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

