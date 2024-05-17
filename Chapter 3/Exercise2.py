#!/usr/bin/env python

# 2) Use click to create a command-line tool that takes a name as an argument and
#    prints it if it does not begin with a p.

import click

@click.command(help="Prints the user inputted name, unless it starts with a 'p'")  # Function should be exposed to command line access
@click.argument('name')  # Define name as a positional argument
def greet(name):
    if not name.lower().startswith('p'):
        print(name)

if __name__ == '__main__':
    greet()  # Call the greet function

