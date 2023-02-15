my_list = [1,1,2]
for index, item in enumerate(my_list):
    print(index)
    if item == 1:
        my_list.append(2)
print(my_list)
