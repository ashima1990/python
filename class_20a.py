#Part 1: Create two fruit basket as sets
basket1 = {"apple", "banana", "cherry", "orange", "kiwi", "mango"}
basket2 = {"banana", "mango", "banana", "grape","orange"}
print("Basket 1:", basket1)
print("Basket 2:", basket2)

# add a new fruit to Basket 1 
basket1.add("pear")
print("Basket 1 after adding pear:", basket1)

# find fruits that are common in both baskets
common_fruits = basket1.intersection(basket2)
print("Common fruits:", common_fruits)

# Create an array of fruit counts using array module
import array as arr
fruit_counts = arr.array('i', [3, 4, 1, 0, 9, 2]) 
print("Fruit counts:", fruit_counts)

#Add a a new fruit counts to the array 
fruit_counts.insert(0,1)
fruit_counts.append(5)
print("Fruit counts after modifications:", fruit_counts)

# count how many times number 4 apears in the array
count_of_4 = fruit_counts.count(4)
print("Count of number 4 in fruit counts:", count_of_4)

# reverse the array of fruit counts
fruit_counts.reverse()
print("Reversed fruit counts:", fruit_counts)

# print the final class fruit basket organizer summary
print("")
print("==============Fruit Organizer==================")
print("Basket 1:", basket1)
print("Basket 2:", basket2)
print("Common fruits:", common_fruits)
print("Fruit counts:", fruit_counts)
print("=========================")
