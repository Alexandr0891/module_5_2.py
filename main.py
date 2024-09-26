# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if 1 <= new_floor <= self.number_of_floors:
                print(i)
            else:
                print('Такого этажа не существует')
                break


h1 = House('ЖК Эльбрус', 30)
h2 = House('магазин', 4)
h1.go_to(7)
h1.go_to(31)
h2.go_to(4)
h2.go_to(5)