#define the simple_divide function here
def simple_divide(item, denom):
    # start a try-except block
    try:
        for i, _ in enumerate(item):
            item[i] /= denom
    except ZeroDivisionError:
        item = [0]*len(item)
    finally:
        return item

def fancy_divide(list_of_numbers, index):

    return simple_divide(list_of_numbers, denom = list_of_numbers[index])

def main():
    data = input()
    l = data.split()
    l1 = []
    for j in l:
        l1.append(float(j))
    s = input()
    index = int(s)
    print(fancy_divide(l1,index))
    

if __name__== "__main__":
    main()
