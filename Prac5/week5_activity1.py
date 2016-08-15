"""
Create a python file that can get 3 words from user, seperated by whitespace.
Once the inputs are received, split it into 3 variables called word1, word2, word3
Use Exception to capture any error in user input.
"""

input_flag = False

while not input_flag:
    try:
        user_input = input("Enter three words seperated by space: ")
        data1, data2, data3 = user_input.split()
        print ("data1: {}\ndata2: {}\ndata3: {}".format(data1, data2, data3))
        input_flag = True
    except ValueError:
        print ("Bad input.")

#data1: {} =
#\n: New line





