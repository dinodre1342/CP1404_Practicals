

class LowInventoryException(Exception):
    """
    Creating your own exception
    """
    def __init__(self):
        print("Low inventory alert!!!!")


def test():
    inventory = 6
    if inventory < 10:
        raise LowInventoryException

try:
    test()
except LowInventoryException:
    print("Re-Stock!!")
#
# filename = "data1.txt"
#
# try:
#     file_pointer = open(filename, "r")
# except FileNotFoundError:
#     print("File doesn\'t exist.")
# else: #continuation of try if no except
#     file_pointer.close()
#     print("File opened and closed.")
#     print("In else")
# finally: # Will be executed no matter with exception or without exception.
#     print("print no matter what.")