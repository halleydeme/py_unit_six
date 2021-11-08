# Halley Deme
# Date Last Edited: 11/03/2021
# This program simulates multiple classes of 23 people to check for duplicate birthdays.
# This is a model of the birthday paradox.
import random
def birthdays():
    list_one = []
    for x in range(23):
        r=random.randint(1,365)
        list_one.append(r)
    print(list_one)

def find_duplicate(listx):
    for x in range(22):
        for y in range(x+1,23):
            if listx[x]== listx[y]:
                return true
    return false
def main():
    num= (int(input("How many times should this program run?")))
    for x in range(num):
        birthdays()
        find_duplicate(birthdays())
main()



