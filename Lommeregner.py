import math

# Chosses how to calculate based on sign, and does the calculation.
def calculate(x, y, sign):
    match sign:
        case "+":
            return float(x) + float(y)
        case "-":
            return float(x) - float(y)
        case "*":
            return float(x) * float(y)
        case "/":
            if y=="0":
                return "no division by 0"
            return float(x) / float(y)
        case "^":
            return float(x) ** float(y)
        case "sqrt" | "//":
            return  math.sqrt(float(x)) 
        case _:
            return "failed"

def main():
    print("------Lommeregner------")
    while(True):
        print("giv input:")
        i = input()
        if i == "q":
            break
        i = i.split()
        print(calculate(i[0], i[2] if len(i) > 2 else i[0], i[1]))
    print("lukker lommeregner")

main()