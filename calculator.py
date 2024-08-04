import math

def evaluate_expression(expression):
    try:
        expression = expression.replace('^', '**')
        expression = expression.replace('sin', 'math.sin')
        expression = expression.replace('cos', 'math.cos')
        expression = expression.replace('tan', 'math.tan')
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Welcome to the CLI Calculator!")
    print("You can perform basic arithmetic operations, use parentheses,")
    print("exponentiation (^), and trigonometric functions (sin, cos, tan).")
    print("Type 'exit' to quit the calculator.")
    
    while True:
        expression = input("Enter an expression: ")
        if expression.lower() == 'exit':
            print("Goodbye!")
            break
        
        result = evaluate_expression(expression)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
