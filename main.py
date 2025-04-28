from calculator import Calculator
from scientific import ScientificCalculator
from user import User

def menu():
    print("\nWelcome to the Enhanced Python Calculator!")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root (Scientific Mode)")
    print("6. Exponentiate (Scientific Mode)")
    print("7. Logarithm (Scientific Mode)")
    print("8. View Calculation History")
    print("0. Exit")

def get_inputs():
    a = float(input("Enter input A: "))
    b = float(input("Enter input B: "))
    return a, b

def main():
    name = input("Enter your name: ")
    user = User(name)
    calculator = Calculator()
    sci_calc = ScientificCalculator()

    while True:
        menu()
        choice = input("Choice: ")

        if choice == '0':
            print(f"Goodbye, {user.name}!")
            break
        elif choice in ['1', '2', '3', '4']:
            a, b = get_inputs()
            calculator.set_inputs(a, b)
        elif choice in ['6']:
            a = float(input("Enter base: "))
            b = float(input("Enter exponent: "))
            sci_calc.set_inputs(a, b)
        elif choice in ['5', '7']:
            a = float(input("Enter input A: "))
            sci_calc.set_inputs(a, 0)

        if choice == '1':
            result = calculator.add()
            print("Result:", result)
            user.add_to_history("Addition", result)
        elif choice == '2':
            result = calculator.subtract()
            print("Result:", result)
            user.add_to_history("Subtraction", result)
        elif choice == '3':
            result = calculator.multiply()
            print("Result:", result)
            user.add_to_history("Multiplication", result)
        elif choice == '4':
            result = calculator.divide()
            print("Result:", result)
            user.add_to_history("Division", result)
        elif choice == '5':
            result = sci_calc.square_root(sci_calc.inputA)
            print("Result:", result)
            user.add_to_history("Square Root", result)
        elif choice == '6':
            result = sci_calc.exponentiate(sci_calc.inputA, sci_calc.inputB)
            print("Result:", result)
            user.add_to_history("Exponentiation", result)
        elif choice == '7':
            result = sci_calc.logarithm(sci_calc.inputA)
            print("Result:", result)
            user.add_to_history("Logarithm", result)
        elif choice == '8':
            print("\nCalculation History:")
            for op, res in user.get_history():
                print(f"{op}: {res}")
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
