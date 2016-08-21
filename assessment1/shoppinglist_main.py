"""
Andre Sardino Arno

The program is to load list of saved items from a csv file. The user then can choose either list required items, add new item,
mark completed items, or list of completed items. The program ends with saving added new items to the csv file.
"""

def main():
    print("Shopping List 1.0 - by Andre Sardino Arno")
    print("3 items loaded from items.csv")
    menu()


def list_items ():
    list = open("items.csv", 'r')
    num = 0
    for each in list:
        items = each.strip().split()



def menu():
    print("Menu:")
    print("R - List required items")
    print("A - Add new item")
    print("M - Mark an item as completed")
    print("Q - Quit")
    user_input = input(">>>")
    user_input = user_input.upper()

    while True:

main()
