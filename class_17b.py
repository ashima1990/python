# function to check whether
#first and the last character match
def match_words(words):
    ctr = 0
    lst=[]
    for word in words:
       if len(word)>1 and word[0]==word[-1]:
              ctr+=1
              lst.append(word)


    print("list of words which have the samae character in the front and at the back\n",lst)
    return ctr 

count = match_words(['less', 'ice','123451', 'kick','eagle','acacia'])
print("number of word having first and last character same are:", count)
