import time


def Programm0():
    print("Hello world")


def Programm1():
    Value = input("Enter a word or Number -- ")
    try:
        float(Value)
        try:
            int(Value)
            print("That is an integer")
        except ValueError:
            print("That is a decimal")
    except ValueError:
        print("That is a string")


def Programm2():
    print("Calculator")
    Num = input("First number -- ")
    Num2 = input("Second number -- ")
    Opr = input("Operator -- ")
    try:
        print(eval(Num+Opr+Num2))
    except SyntaxError:
        print("Please input a valid equation.")


__version__ = "0.0.0.0.30"
ProgrammNumber = 2
programmList = {1: Programm1, 2: Programm2}


def Showcase():
    print(f"HubBase Utility v{__version__} programm showcase - {ProgrammNumber} programms")
    ProgrammCycle(ProgrammNumber, programmList, time.sleep, [1])


def ProgrammCycle(ProgrammNumber: int, programmList: dict, TransitionMethod, TransitionMethodargs: list):
    for programm in range(1, ProgrammNumber + 1):
        print(f"Programm №{programm} launching")
        try:
            programmList[programm]()
            TransitionMethod(*TransitionMethodargs)
        except KeyError:
            print(f"KeyError: Key {programm} is out of reach")
            break
