# Halley Deme
# Date Last Edited: 11/09/2021
# This program simulates multiple classes of 23 people to check for duplicate birthdays.
# This is a model of the birthday paradox.
import random

def birthdays():
    """

    :return: This function generates a random list of 23 birthdays ( a number between 1 and 365).
    """
    list_one = []
    for x in range(23):
        r=random.randint(1,365)
        list_one.append(r)
    return list_one

def find_duplicate(listx):
    """

    :param listx: This parameter takes a list to check for duplicates.
    :return: This function checks for repeats in a given list aka duplicates. Then, it returns true or false depending on if there is or isn't duplicates.
    """
    for x in range(22):
        for y in range(x+1,23):
            if listx[x] == listx[y]:
                return True
    return False
def main():
    percent = 0
    num = (int(input("How many times should this program run?")))
    for x in range(num):
       if find_duplicate(birthdays()):
           percent += 1
    print("The percent of times duplicates were found is " + str(percent/num) + ".")

main()



