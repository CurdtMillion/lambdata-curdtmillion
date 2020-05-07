# my_mod.py


def enlarge(n):
    return n * 100

def decimate(n):
    return n - (n * .1)

# def splitdate():


if __name__ == "__main__":
    
    x = 5
    print(enlarge(x))

    y = int(input("Please choose a number (e.g. 5): "))
    print(enlarge(y))
