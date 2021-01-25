# Ken

"""
Problem 1
Pretend you have a flip phone that uses multiple button presses to get a character.
Here's a table mapping the button to the characters:
Key   Character
1     .,?!:
2     ABC
3     DEF
4     GHI
5     JKL
6     MNO
7     PQRS
8     TUV
9     WXYZ
0     Space
For instance, pressing 4 twice gets 'H'.
Implement the function to use a dictionary to turn a string into a string of button presses. 'Hello, World!' becomes
4433555555666110966677755531111. Account for both uppercase and lowercase letters. The button's don't differentiate
for capitalization, you can adjust the input for the table. You can ignore every other that's not shown in the table.
"""


def flip_phone(message):
    text = list(message.lower())
    dict = {
        #this is absolutely garbage code, but i don't know how to shorten it
        '.': '1',
        ',': '11',
        '?': '111',
        '!': '1111',
        ':': '11111',
        'a': '2',
        'b': '22',
        'c': '222',
        'd': '3',
        'e': '33',
        'f': '333',
        'g': '4',
        'h': '44',
        'i': '444',
        'j': '5',
        'k': '55',
        'l': '555',
        'm': '6',
        'n': '66',
        'o': '666',
        'p': '7',
        'q': '77',
        'r': '777',
        's': '7777',
        't': '8',
        'u': '88',
        'v': '888',
        'w': '9',
        'x': '99',
        'y': '999',
        'z': '9999',
        ' ': '0'
    }
    for i in text:
        for t,v in dict.items():
            if i in v:
                for y in range(v.index(i)):
                    return t


"""
Problem 2
Use one or more dictionaries to see how many unique characters are in a string.
For instance, 'zzz' has one unique character while 'Hello, World!' has 10. 
"""


def unique_characters(string):
    uniquecharacters = dict()
    for character in string:
        uniquecharacters[character] = True
    return len(uniquecharacters)


"""
Problem 3
Create a Car class with the attributes brand, max_speed, and current_speed. Initialize all those attributes in its
constructor in that order. Add two methods, accelerate and decelerate, which take no parameters, 
and add 10 to current_speed in accelerate and subtract 5 in decelerate. Check if accelerating will go past max_speed 
and if decelerating will make it go past 0. If either situation happens, don't change the speed.
"""


class Car:

    def __init__(self,brand, max_speed, current_speed):
        self.brand = brand
        self.max_speed = max_speed
        self.current_speed = current_speed

    def accelerate(self):
        if self.current_speed + 10 > self.max_speed:
            return self.current_speed
        else:
            self.current_speed += 10

    def decelerate(self):
        if self.current_speed - 5 <= 0:
            return self.current_speed
        else:
            self.current_speed -= 5