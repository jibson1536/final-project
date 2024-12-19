class TruthTableEvaluator:
    def evaluate(item, expression):
        try:
            return eval(expression.format(**item))
        except Exception as e:
            print(f"Error evaluating expression: {e}")
            return False

    
    def filter_data(data, expression):
        filtered_data = []
        for item in data:
            if TruthTableEvaluator.evaluate(item, expression):
                filtered_data.append(item)
        return filtered_data

    def format_expression(expression):
        try:
            return expression.replace('and', ' and ').replace('or', ' or ').replace('not', ' not ')
        except Exception as e:
            print(f"Error formatting expression: {e}")
            return expression
