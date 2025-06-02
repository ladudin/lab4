def print_name1():
    print("Владислав")

def print_name2():
    print("МАКСИМ")

def print_name3():
    print("АНЯ")

def print_name4():
    print("ЕГОР")

n = int(input())
if n not in (1, 2, 3, 4):
    raise ValueError("Номер должен быть от 1 до 4")
if n == 1:
    print_name1()
elif n == 2:
    print_name2()
elif n == 3:
    print_name3()
elif n == 4:
    print_name4()