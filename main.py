from calculator import Calculator
from user import User

def menu():
    print("\nWelcome to the Enhanced Python Calculator!")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Exponentiate")
    print("7. Logarithm")
    print("0. Exit")

def get_inputs():
    a = float(input("Enter input A: "))
    b = float(input("Enter input B: "))
    return a, b

def main():
    name = input("Enter your name: ")
    user = User(name)
    calculator = Calculator()

    while True:
        menu()
        choice = input("Choice: ")

        if choice == '0':
            print(f"Goodbye, {user.name}!")
            break
        elif choice in ['1', '2', '3', '4', '6']:
            a, b = get_inputs()
            calculator.set_inputs(a, b)
        elif choice in ['5', '7']:
            a = float(input("Enter input A: "))
            calculator.set_inputs(a, 0)

        if choice == '1':
            print("Result:", calculator.add())
        elif choice == '2':
            print("Result:", calculator.subtract())
        elif choice == '3':
            print("Result:", calculator.multiply())
        elif choice == '4':
            print("Result:", calculator.divide())
        elif choice == '5':
            print("Result:", calculator.square_root())
        elif choice == '6':
            print("Result:", calculator.exponentiate())
        elif choice == '7':
            print("Result:", calculator.logarithm())
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
