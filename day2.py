import math

def advanced_calculator():
    print("Advanced Calculator")

    while True:
        expression = input("Enter an expression (or 'exit' to quit): ")

        if expression.lower() == 'exit':
            print("Exiting calculator. Goodbye!")
            break

        try:
            result = eval(expression)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    advanced_calculator()
