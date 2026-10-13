# define the function to calculate cube
def cube(num):
    return num*num*num
# define a function which will execute cube number if the user entered a number divisible by 3 
def by_three(num):
    if num%3==0:
        return cube(num)
    else:
        return False
# display result
print(by_three(9))
print(by_three(4))