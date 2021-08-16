#!/usr/bin/env python3

import string
from random import sample
import argparse

class password_generator():

    def __init__(self, caracters_range):
        if caracters_range <= 1500000 and caracters_range > 1:
            self.__caracters_range = int(caracters_range)
        else:
            raise Exception("\033[0;31m" + "The size must be greater than 1 and less than 1.500.000." + "\033[0m")
        self.random_caracters()
    
    def random_caracters(self, lowercase = True, uppercase = True, numbers = True, special_characters = True):
        self.__random_characters = ""
        if lowercase:
            self.__random_characters += string.ascii_lowercase
        if uppercase:
            self.__random_characters += string.ascii_uppercase
        if numbers:
            self.__random_characters += string.digits
        if special_characters:
            self.__random_characters += string.punctuation
        if len(self.__random_characters) < 1:
            raise Exception("\033[0;31m" + "Your password must contain at least one character set." + "\033[0m")
        while len(self.__random_characters) < self.__caracters_range:
            self.__random_characters += self.__random_characters

    def generate_password(self):
        password = "".join(sample(self.__random_characters, self.__caracters_range))
        return password
        
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple password generator made by Tynuz. GitHub: https://github.com/Tynuzz")
    default_size = 8
    parser.add_argument('-s', '--size', type=int, default=default_size, help=f'sets the number of characters in the password. (defaut: {default_size})', action="store")
    parser.add_argument('-l', '--lowercase', help='disables the use of lowercase.', action="store_false")
    parser.add_argument('-u', '--uppercase', help='disables the use of uppercase.', action="store_false")
    parser.add_argument('-n', '--numbers', help='disables the use of numbers.', action="store_false")
    parser.add_argument('-p', '--punctuation', help='disables the use of punctuation.', action="store_false")
    
    args = parser.parse_args()

    password_generator = password_generator(args.size)
    password_generator.random_caracters(args.lowercase, args.uppercase, args.numbers, args.punctuation)
    
    password = password_generator.generate_password()
    
    print(password)