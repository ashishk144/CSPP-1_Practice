""" Variable Evaluation"""

def datatype(parameter):
    """returs type of the inputted parameter"""
    return type(parameter)

VARA = 12
VARB = "12"
STR = datatype("abc")

if datatype(VARA) == STR or datatype(VARB) == STR:
    print("string involved")
elif VARA > VARB:
    print("Bigger")
elif VARA == VARB:
    print("Equal")
else:
    print("Smaller")
