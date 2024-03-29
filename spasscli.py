#!/usr/bin/env python3
#%%
'''
███████ ███    ██  █████  ███████ ███████ ██    ██     ██████   █████  ███████ ███████ 
██      ████   ██ ██   ██    ███     ███   ██  ██      ██   ██ ██   ██ ██      ██      
███████ ██ ██  ██ ███████   ███     ███     ████       ██████  ███████ ███████ ███████ 
     ██ ██  ██ ██ ██   ██  ███     ███       ██        ██      ██   ██      ██      ██ 
███████ ██   ████ ██   ██ ███████ ███████    ██        ██      ██   ██ ███████ ███████ 
                                                                                       
                                                                                       
A random password generator with a CLI.
-
Author:
Mister Riley
sorzkode@proton.me
https://github.com/sorzkode

MIT License
Copyright (c) 2024 Mister Riley
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

# Importing required libraries / modules
import random
import string
import click
import pyfiglet

class SnazzyPass:
    def __init__(self, length=10, special=2, numbers=2):
        self.length = length
        self.special = special
        self.numbers = numbers

    def generate_password(self):
        """
        Generate a random password based on specified requirements.

        Returns:
            str: Generated random password.
        """
        # Characters to generate password from
        alphabets = list(string.ascii_letters)
        digits = list(string.digits)
        special_characters = list("!@#$%^&*()")

        if self.length <= 0:
            raise ValueError("Password length must be greater than zero.")
        if self.special + self.numbers > self.length:
            raise ValueError("Sum of special characters and numbers exceeds password length.")

        password = []

        for _ in range(self.length - self.special - self.numbers):
            password.append(random.choice(alphabets))

        for _ in range(self.numbers):
            password.append(random.choice(digits))

        for _ in range(self.special):
            password.append(random.choice(special_characters))

        random.shuffle(password)
        randopass = ''.join(password)

        return randopass

    def main(self):
        """
        Main function to generate and print a random password.
        """
        try:
            password = self.generate_password()

            spbanner = pyfiglet.figlet_format("Spazzy Pass")

            print(spbanner)
            print("\nGenerating a randomized password with the following requirements:\n")
            print(f"Overall length: {self.length} (default is 10).")
            print(f"Special characters: {self.special} (default is 2).")
            print(f"Numbers: {self.numbers} (default is 2).\n")
            print(f"Your password: {password}\n")
            print(f"Be sure to play around with the options to change PW length, special characters, and numbers.\n")
            print(f"You can type: python spasscli.py --help for more information.\n")

        except ValueError as e:
            print(f"Error: {str(e)}")

@click.command()
@click.option('-l', '--length', default=10, type=int, help='Set your overall password length.')
@click.option('-s', '--special', default=2, type=int, help='Set the number of special characters.')
@click.option('-n', '--numbers', default=2, type=int, help='How many numbers to include.')
def cli(length, special, numbers):
    """
    CLI command to generate a random password based on specified requirements.

    Args:
        length (int): Overall password length.
        special (int): Number of special characters.
        numbers (int): Number of numbers to include.
    """
    generator = SnazzyPass(length, special, numbers)
    generator.main()

if __name__ == "__main__":
    try:
        cli()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
