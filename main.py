import random

def print_name1():
    print("Владислав")

def print_name2():
    print("МАКСИМ")

def print_name3():
    print("АНЯ")

def print_name4():
    print("ЕГОР")

def print_random_name():
    n = random.randint(1, 4)
    if n == 1:
        print_name1()
    if n == 2:
        print_name2()
    if n == 3:
        print_name3()
    if n == 4:
        print_name4()