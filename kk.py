my_set= {"dumplings", "noodles", "wanton", "soup"}
snack_set= {"chips", "cookies", "candy", "soda", "dumplings", "noodles"}
print("yum snacks:", my_set)
print("little snacks:", snack_set)

added_snack = snack_set.add("popcorn")
print("snack set after adding popcorn:", snack_set)

same_snacks = my_set.intersection(snack_set)
print("same snacks in both sets:", same_snacks)

import array as arr
snack_counts = arr.array('i', [5, 2, 3, 1, 4, 6])
print("snack counts:", snack_counts)    

snack_counts.insert(0, 7)
snack_counts.append(8)
print("snack counts after modifications:", snack_counts)

count_of_3 = snack_counts.count(3)
print("Count of number 3 in snack counts:", count_of_3)

snack_counts.reverse()
print("Reversed snack counts:", snack_counts)

# print the final class snack organizer summary
print("")   
print("==============Snack Organizer==================")
print("My snack set:", my_set)
print("Little snack set:", snack_set)
print("Same snacks in both sets:", same_snacks)
print("Snack counts:", snack_counts)
print("smack your lips with these snacks!")
print("=========================")