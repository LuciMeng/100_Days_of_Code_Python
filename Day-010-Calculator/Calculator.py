import art

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculator():
    print(art.logo)
    n1 = float(input("What is the first number: "))
    while True:
        for symbol in operations:
            print(symbol)
        pick = input("Pick an operation: ")
        n2 = float(input("What's the next number: "))
        result = operations[pick](n1, n2)
        print(f"{n1} {pick} {n2} = {result}")

        response = input(f"Type 'y' to continue calculating with {result}, "
                         f"or type 'n' to start a new calculation: "
                         f"or type 'exit' to exit the calculation: ")

        if response == "y":
            n1 = result
        elif response == "n":
            print("\n" * 20)
            calculator()
            break
        else:
            print("Goodbye!")
            break
calculator()

