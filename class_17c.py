L = [4,5,6,8,2,10,1]
print("Orignal list:",L)
 # Variable to store the sum of 
 # the list
count = 0

#finding the sum 
for i in L:
    count += i

# dividing the total elements by 
#number of elements
avg = count/len(L)

print("sum is :",count)
print("average is :",avg)

#sorting the elements from list
L.sort()

#printing the first element 
print("smallest element is:", L[0])

#printing the last statement 
print("largest element is:", L[-1])