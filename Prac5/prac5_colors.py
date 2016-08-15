colors = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2" :"eedfcc", "AntiqueWhite3":"#cdc0b0", "AntiqueWhite4": "8b8378", "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "aquamarine4": "#458b74", "azure1": "f0ffff"}

input_color = input("Please Enter color:")
while colors != "":
    if input_color in colors:
        print(input_color, "is", colors[input_color])
    else:
        print("Invalid color input!")
    input_color = input("Please Enter color:")