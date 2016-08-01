import string

MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = False
SPECIALS = "!@#$%^&*()_-=+`~,./o'[]\<>?O{}|"


def main():
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH, "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIALS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your " + str(len(password)) + " character password is valid: " + password)


def is_valid_password(password):
    # TODO: if length is wrong, return False
    print (len(password))
    if len(password) < MIN_LENGTH and len(password) > MAX_LENGTH:
        print("The password is too short/long. It must be 2 to 6 characters.")
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    for char in password:
        if char in string.ascii_lowercase:
            count_lower += 1
        elif char in string.ascii_uppercase:
            count_upper += 1
        elif char in string.digits:
            count_digit += 1
        elif char in string.punctuation:
            count_special += 1

    if count_lower == 0:
        return False
    elif count_upper == 0:
        return False
    elif count_digit == 0:
        return False
    elif count_special == 0:
        return False
    else:
        return True
main ()
    # TODO: count each kind of character
    # TODO: if any of the 'normal' counts are zero, return False
    # TODO: if special characters are required, then check the count of those and return False if it's zero

    # if we get here (without having returned False), then the password must be valid
