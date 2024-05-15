# 1) Write a Python function that takes a name as an argument and prints that name
def print_name(name):
    print(name)

# 2) Write a Python function that takes a string as an argument and prints whether it is upper or lower case
def print_case(input):
    if input.islower():
        print("lowercase")
    elif input.isupper():
        print("uppercase")
    else:
        print("other")

# 3) Write a list comprehension that results in a list of every letter in the word smog-tether capitalized
def comprehension():
    word = "smog-tether"
    capitalized_list = [i.upper() for i in word]
    return capitalized_list

# 4) Write a generator that alternates between returning Even and Odd
def generator():
    n = 0
    while True:
        if n % 2 == 0:
            yield "Even"
        else:
            yield "Odd"
        n += 1

# Testing
print_name("Eric Iamarino")

print_case("ERIC")
print_case("eric")
print_case("Eric")

print(comprehension())

gen = generator()
for i in range(0, 4):
    print(next(gen))