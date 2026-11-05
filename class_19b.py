# initialize the dictionary
test_dict= {"Codingal":2, "is":2, "best":2, "for":2, "coding":2}

# print the original dictionary
print("The original dictionary is:", str(test_dict))

# initialize the value
K=2

# Using loop
#Selective key values in dictionary
res = 0
for key in test_dict.items():
    if test_dict[key] == K:
        res = res + 1

# printing result
print("The frequency of K in dictionary is:", str(res))