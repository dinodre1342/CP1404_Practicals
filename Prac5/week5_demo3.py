def subject(subject_code, subject_name):
    """
    This is a function for printing subject code and name.
    :param subject_code: This is the JCU unique code for each subject
    :param subject_name: This is the associated name matching the code
    :return: A string message displaying both code and name
    """
    string_msg = "This subject {} refers to {}".format (subject_code, subject_name)
    print(string_msg)
    return string_msg

def main():
    #print(subject())
    #print (subject("3400", "New Subject"))
    #print (subject("4000"))
    #print (subject(subject_name="abc"))
    print (subject.__name__)
    print (subject.__doc__)
    print (subject.__str__)
    print (subject.__dict__)
    #print(subject("","").__doc__)
    #print subject ("1404", "Intro to programming")

main()