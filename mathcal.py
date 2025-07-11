from math import tan, sin, cos, radians

class MathCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            print("Error: Division by zero is not allowed.")
            return a
        return a / b

    def tan(self, a):
        return tan(radians(a))

    def sin(self, a):
        return sin(radians(a))

    def cos(self, a):
        return cos(radians(a))


def main():
    calculator = MathCalculator()
    print("Welcome to the Math Calculator!")

    while True:
        try:
            result = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    while True:
        print("\nChoose an operation:")
        print("+ : Add")
        print("- : Subtract")
        print("* : Multiply")
        print("/ : Divide")
        print("sin : Sine")
       
        print("Clear : Clear")
        print("Exit : Exit")

        op = input("Enter operation: ").strip().lower()

        if op == 'e':
            print("Exiting the calculator. Goodbye!")
            break

        elif op == 'c':
            try:
                result = float(input("Enter new starting number: "))
                print("Calculator reset.")
            except ValueError:
                print("Invalid number. Reset skipped.")
            continue

        elif op in ['+', '-', '*', '/']:
            try:
                b = float(input("Enter second number: "))
                if op == '+':
                    result = calculator.add(result, b)
                elif op == '-':
                    result = calculator.subtract(result, b)
                elif op == '*':
                    result = calculator.multiply(result, b)
                elif op == '/':
                    result = calculator.divide(result, b)

                print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif op in ['sin', 'cos', 'tan']:
            if op == 'sin':
                result = calculator.sin(result)
            elif op == 'cos':
                result = calculator.cos(result)
            elif op == 'tan':
                result = calculator.tan(result)
            print(f"Result: {result}")

        else:
            print("Invalid operation. Please choose from +, -, *, /, sin, cos, tan, c, e.")


if __name__ == "__main__":
    main()
