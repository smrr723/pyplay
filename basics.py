# def say_hello(name):
#     if(name == "Scott"):
#         print("Hello " + name)
#     else:
#         print("Uh, I don't know you.. Do I?")
# # Won't work without indentation
#
# say_hello("Scott")
# say_hello("Sian")
#
# # Python List - same as array in Ruby
# my_list = ["spam", "ham", "eggs", "parrot"]
# my_list.reverse()
# print(my_list)
#
# my_stuff = [1, 2, "spam", "parrot"]
# print(my_stuff)
#

# my_list = ["spam", "ham", "eggs"]
#
# for food in my_list:
#     print(food)
#
# print("The loop has finished")

# list1 = [2, 4, 6]
# list2 = [1, 3, 5]
#
# print(list1 * list2)
#
# import numpy as np
# array1 = np.array([1, 2, 3])
#
# array2 = np.array([1, 2, 3])
# print(array1 + array2)
person = {
    "name": "Alan",
    "age": 30,
    "favourite_foods": ["Pizza", "Bacon", "Parrot"]
}

# print(person["name"])
#
# for food in person["favourite_foods"]:
#     print(food)

for attribute in person:
    print(person[attribute])
