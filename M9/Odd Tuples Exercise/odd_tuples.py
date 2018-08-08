"""Exercise : Odd Tuples
Write a python function oddTuples(aTup) that takes a some numbers in the tuple
as input and returns a tuple in which contains odd index values in the input tuple"""  



def oddTuples(a_tup):
    '''
    a_tup: a tuple
    
    returns: tuple, every other element of a_tup. 
    '''
    # Your Code Here
    btup = ()
    for [i, j] in enumerate(a_tup):
        if not i%2:
            btup = btup + (j, )
    return btup
def main():
    '''defining main'''
    data = input()
    data = data.split()
    a_tup = ()
    for [_, j] in enumerate(data):
        a_tup += (j, )
    print(oddTuples(a_tup))
        

if __name__ == "__main__":
    main()
