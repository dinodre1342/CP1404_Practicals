
user_input = input("Text:")
words =user_input.split()
count_dict = {}

for word in words:
    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict[word] = 1
print(count_dict)

