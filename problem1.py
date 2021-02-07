#Gavin Lesher
#2/6/2021

def volume(a):
    if a <= 0:
        raise ValueError
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError
    return a*a*a