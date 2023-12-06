#Calculator
#add
def add(n1, n2):
    return n1 + n2

#subtract
def subtract(n1, n2):
    return n1 - n2

#multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide(n1, n2):
    return n1 / n2

calci = {
    "+" : add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
}

print('''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
''')

def calculator1():
    num_1 = float(input("What is the First Number?: "))

    for symbol in calci:
        print(symbol)

    operation_symbol = input("Pick and Operation from the line above: ")
    num_2 = float(input("What is the Second Number?: "))
    calculation_func = calci[operation_symbol]
    answer = calculation_func(num_1, num_2)
    print(f"{num_1} {operation_symbol} {num_2} = {answer}")

    continue_operation = True
    while continue_operation:
        con = input("Do you wanna continue with result and do another operation or you wanna exit? type y for continue and n for exit\n").lower()
        if con == "y":
            operation_symbol = input("Pick and Operation from the line above: ")
            num_3 = float(input("What is the number?: "))
            calculation1 = calci[operation_symbol]
            answer = calculation1(answer, num_3)
            print(f"{answer} {operation_symbol} {num_3} = {answer}")
        else:
            continue_operation = False
            print("Thank your for using our calculator")
            calculator1()

calculator1()