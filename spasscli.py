#!/usr/bin/env python3

'''
███████ ███    ██  █████  ███████ ███████ ██    ██     ██████   █████  ███████ ███████ 
██      ████   ██ ██   ██    ███     ███   ██  ██      ██   ██ ██   ██ ██      ██      
███████ ██ ██  ██ ███████   ███     ███     ████       ██████  ███████ ███████ ███████ 
     ██ ██  ██ ██ ██   ██  ███     ███       ██        ██      ██   ██      ██      ██ 
███████ ██   ████ ██   ██ ███████ ███████    ██        ██      ██   ██ ███████ ███████ 
                                                                                       
                                                                                       
A random password generator with a CLI.
-
Author:
sorzkode
sorzkode@proton.me
https://github.com/sorzkode

MIT License
Copyright (c) 2022 sorzkode

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

#Importing required libraries / modules
import random
import string
import click
import pyfiglet

#ASCII art banner
spbanner = pyfiglet.figlet_format("Spazzy Pass")

#characters to generate password from
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")

#decorators used for CLI commands
@click.command()
@click.option('-l', '--length', default=10, type=int, help='Set your overall password length.')
@click.option('-s', '--special', default=2, type=int, help='Set the number of special characters.')
@click.option('-n', '--numbers', default=2, type=int, help='How many numbers to include.')
def main(length, special, numbers):
    #a little password math
    total_chars = special + numbers
    final_count = length - total_chars
    
    #storing the password as a list for manipulation below
    password = []
    
    #randomizing password pieces
    for i in range(final_count):
        password.append(random.choice(alphabets))

    for i in range(numbers):
        password.append(random.choice(digits))

    for i in range(special):
        password.append(random.choice(special_characters))

	#shuffling pw 
    random.shuffle(password)

    #randomized password
    randopass = ''.join(password)

	#final pw output
    print(spbanner)
    print("\nGenerating a randomized password with the following requirements:\n")
    print(f"Overall length: {length} (default is 10).")
    print(f"Special characters: {special} (default is 2).")
    print(f"Numbers: {numbers} (default is 2).\n")
    print(f"Your password: {randopass}\n")
    print(f"Be sure to play around with the options to change PW length, special characters, and numbers.\n")
    print(f"You can type: python spasscli.py --help for more information.\n")

if __name__ == "__main__":
    main()