#Gavin Lesher
#2/6/2021

def first_and_last(firstName, lastName):
    if(not isinstance(firstName, str) or not isinstance(lastName, str)):
        raise TypeError
    if(firstName == "" or lastName == ""):
        raise ValueError
    return firstName + " " + lastName