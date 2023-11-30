import sys, json, math

f = open("settings.json")
settings = json.load(f)

prec = settings["precision_answer"]
max_num = settings["max_input_num"]
min_num = settings["min_input_num"]

f.close()

class OutOfLimits(Exception):
    pass


def start_speaking():
    command = input("Type command or 'help' to see what you can do: ").strip()

    if command == "help":
        print("")
        print("'+' - finding the sum of two numbers")
        print("'-' - finding the difference of two numbers")
        print("'*' - finding the product of two numbers")
        print("'/' - finding the quotient of two numbers")
        print("'**' - exponentiation")
        print("'%' - remainder from division")
        print("'sin' - finding the sine")
        print("'cos' - finding the cosine")
        print("'q' - stoping the script")
        print("")
        start_speaking()

    elif command in ["+", "-", "/", "*", "**", "%", "sin", "cos"]:
        try:
            num1_str = input("\nEnter the first number\n").strip()
            num1 = float(num1_str)
            if num1 > max_num: raise OutOfLimits
            if num1 < min_num: raise OutOfLimits
            num2 = ""
            if command != "sin" and command != "cos":
                num2_str = input("\nEnter the second number\n").strip()
                num2 = float(num2_str)
                if num2 > max_num: raise OutOfLimits
                if num2 < min_num: raise OutOfLimits
        except OutOfLimits:
            print(f"Numbers should be larger than {min_num} and less than {max_num}\n")
        except:
            print("Wrong value\n")
        else:
            if command == "+":
                print(f"{num1} + {num2} = {round(num1 + num2, prec)}")
            if command == "-":
                print(f"{num1} - {num2} = {round(num1 - num2, prec)}")
            if command == "*":
                print(f"{num1} * {num2} = {round(num1 * num2, prec)}")
            if command == "**":
                print(f"{num1} ** {num2} = {round(num1 ** num2, prec)}")
            if command == "%":
                print(f"{num1} % {num2} = {round(num1 % num2, prec)}")
            if command == "sin":
                print(f"sin({num1}) = {round(math.sin(num1), prec)}")
            if command == "cos":
                print(f"cos({num1}) = {round(math.cos(num1), prec)}")
            if command == "/" and num2 != 0:
                print(f"{num1} / {num2} = {round(num1 / num2, prec)}")
            elif command == "/":
                print("You can`t divide by 0")
    
    elif command == "q":
        sys.exit()

    else:
        print("Wrong command or value\n")
        start_speaking()

    start_speaking()


start_speaking()
