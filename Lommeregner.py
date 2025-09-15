import math

help =  " Skriv et simpelt regnestykke med mellemrum mellem alle dele af det for at udregne de \n " \
        " programmet tager i mod: + for addition, - for substraction, * for multiplication, / for division, ^ for potens, og // eller sqrt for kvadratrod \n " \
        " skriv q eller quit for at lukke progammmet"

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y==0:
        return "no division by 0"
    return x / y

def pot(x, y):
    return x ** y

def sqt(x):
    return math.sqrt(x)

# Chosses how to calculate based on sign, and does the calculation.
def calculate(sign, int):
    match sign:
        case "+":
            return add(float(int[0]), float(int[1]))
        case "-":
            return sub(float(int[0]), float(int[1]))
        case "*":
            return mul(float(int[0]), float(int[1]))
        case "/":
            return div(float(int[0]), float(int[1]))
        case "^":
            return pot(float(int[0]), float(int[1]))
        case "sqrt" | "//":
            return  sqt(float(int[0])) 
        case _:
            return "failed"

def main():
    print("------Lommeregner------")
    while(True):
        print("skriv input eller \"help\":")
        i = input()
        if i == "q" or i == "quit":
            break
        if i == "help":
            print(help)
            continue
        i = i.split()
        sign = i.pop(1)
        print("= " + str(calculate(sign, i)))
    print("lukker lommeregner")

main()