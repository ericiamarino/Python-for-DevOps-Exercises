#!/usr/bin/env python

# 3) Use fire to access methods in an existing Python script from the command line.
import fire

# Method 1 to be accessed from the command line
def say_first_name(firstName='Eric'):
    message = f'Your first name is {firstName}'
    print(message)

# Method 2 to be accessed from the command line
def say_last_name(lastName='Iamarino'):
    message = f'Your last name is {lastName}'
    print(message)

# Define a class to act as top group. Add our functions to the attributes of this class
class Cli():
    def first_name(self, firstName='Eric'):
        """
        Prints the first name inputted by the user: ./Exercise3 first_name --firstName <here>
        """
        say_first_name(firstName)
    def last_name(self, lastName='Iamarino'):
        """
        Prints the last name inputted by the user: ./Exercise3 last_name --lastName <here>
        """
        say_last_name(lastName)

if __name__ == '__main__':
    fire.Fire(Cli)