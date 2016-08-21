def main():
    print("Shopping List 1.0 - by Andre Sardino Arno")
    print("3 items loaded from items.csv")
    print("Menu:")
    print("R - List required items")
    print("A - Add new item")
    print("M - Mark an item as completed")
    print("Q - Quit")
    user_input = input("Please select one:")

    while user_input == "":
        user_input = input("Please select one:")


main()