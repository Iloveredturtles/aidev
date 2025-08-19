grocery_list = ['Bread','Cereal','Peanut Butter']
# print(grocery_list)
# print(grocery_list[0]) #Displays the first data
# print(grocery_list[1]) #Displays the second data
# print(grocery_list[-1])
# grocery_list.append('Sausage') #Adding items to the list
# grocery_list.append('Croissant')
# grocery_list.remove('Bread') #Delete items on the list
# print(grocery_list)
# grocery_list[1] = 'Strawberry Jam' #Changing index items to
# print(grocery_list) 
# print(len(grocery_list)) #Displays the number of items in the list


numbers = [' 130','100','140','150', '190', '200', '250','200','230','250'] #Do It Yourself! Try filling it with the weight of the grapes recorded by Jio.
# numbers.sort() #Sorts the items in the list in ascending order
# print(numbers)
# grade_3 = numbers[:4] #Fetch the item before the 4th index
# print(grade_3)
# grade_2 = numbers[4:7] #Sort the items in the list in descending order.
# print(grade_2)
# grade_1 = numbers[7:] #Fetches items after index 7
# print(grade_1)

ages = [14, 15, 8, 10, 17,18, 20, 21, 19, 10, 25, 21, 10,20, 15]
# ages.sort()
# print(ages)
# new_ages = ages[7:]
# print(new_ages)

#2D Lists
temperature = [ #Outer list
    [25, 27, 28, 27], #Inside is another list. 
    [23, 24, 26, 26],
    [24, 24, 27, 27],
    [22, 24, 25, 24]
]

# temperature.append([23,24,24,26])
# print(temperature)
# print(len(temperature))
temperature[1][2] = 27
print(temperature[1])