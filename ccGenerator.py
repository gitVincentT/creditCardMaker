import string
import random
from random import choice 

"""
CC generator: core functionality
    1. 16 digit number 
    2. Expiration date - 4 digits
    3. Security code - 3 digits 
    
    BONUS:
    4. Generate random first and last name 
    5. Generate random address in the US 
       Ex. 99 Maple Street, Brighton MA 02135 
        Mailing address, City, State, Zip Code 
    6. Add JS front-end 

Scratch Notes: 
    Create a function (FOUR_DIGIT) that generates a 4 digit number randomly 
    Create a function (three_DIGIT) that generates a 3 digit number randomly 
    Use other functions to parse it
        1. CC number uses "CC Number: " + function FOUR_DIGIT x4 and spaces its out 
        2. Exp date uses "Exp Date: " + function FOUR_DIGIT x1 and adds a / in between it 
        3. Security code uses three_DIGIT x1 

"""
def month():
    #Has to between these numbers: 01 - 12 
    #If 1-9, it should have 0 in front of it 
    #If 10+, 2nd digit should be 0, 1, or 2
    m = (random.randint (1,12))
    if m < 10: #
        return (str(0) + str(m)) 
    else : 
        return m


def year():
    #Has to be 21-30 
    y = random.randrange (21,30)
    return y 
    
def three_DIGIT():
    chars = string.digits
    random = ''.join(choice(chars) for _ in range(3))
    return random

def four_DIGIT():
    chars = string.digits
    random = ''.join(choice(chars) for _ in range(4))
    return random



def ccNumber():
    a = str(four_DIGIT())
    b = str(four_DIGIT())
    c = str(four_DIGIT())
    d = str(four_DIGIT())
    
    print("CC Number: " + a + " " + b + " " + c + " " + d)

def expDate():
    a = str(month())
    b = str(year())
    print("Exp Date: " + a + "/" + b)

def cvCode():
    a = three_DIGIT()
    print("CV Code: " + str(a))
    
ccNumber()
expDate()
cvCode()
