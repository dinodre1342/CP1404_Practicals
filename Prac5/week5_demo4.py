plants = {}

print(plants)
plants ['carrots'] = 'orange' #key=carrot, value=orange
plants ['radish'] = 'white'
plants ['beetroot'] = 'red'
print (plants)


for plant in plants:
    print ("Getting plant: ", plant)

for key, value in plants.items():
    print ("Key:{}, Value:{}".format (key, value))

print (plants['beetroot'])
print ("Finding carrot: ",plants.get("carrot"))
print ("Finding Vege: ",plants.get("Vege", "cannot be found."))

for value in plants.value ():
    print(value)

#dictionary_basic ()

words =['John', 'Amy', 'John', 'Benny']
count_dict = {}

for word in words:
    if word in count_dict:
        count_dict[word] += 1     #+= - increment by 1
    else:
        count_dict[word] = 1
print(count_dict)

