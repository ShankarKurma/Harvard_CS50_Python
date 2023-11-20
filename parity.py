def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("Even")
    else:
        print("odd")


def is_even(n):
    return n%2 ==0

    #Idea 2:
    #return True if n % 2 == 0 else False
    
    """ Idea 1 : 
    if n % 2 ==0:
        return True
    else:
        return False"""

main()