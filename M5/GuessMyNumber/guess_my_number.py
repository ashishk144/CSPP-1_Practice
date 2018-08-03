"""Guess My Number Exercise"""

def main():
    """defining main"""
    l_o = 0
    h_i = 100
    an_s = (l_o+h_i)/2
    for _ in range(0, 100):
        print("Is your secret number " + str(an_s))
        in_p = input("Enter c for correct, l for low, h for high ")
        if in_p == 'c':
            break
        elif in_p == 'l':
            l_o = an_s
        elif in_p == 'h':
            h_i = an_s
        else:
            print("Invalid")
        an_s = (l_o+h_i)//2
if __name__ == "__main__":
    main()
