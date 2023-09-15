'''Input is a sentence. Find the number of times each word appears'''

#Input of sentences
str="happy persons always be happy"
#Print the given sentence
print("The given sentence is",str)
#word to count
b=input("enter the search word:")
#If word in sentence it will count
if b in str:
    print(str.count(b))
#Else expection case
else:
    print("No word in sentence")


'''
Output:
The given sentence is happy persons always be happy
enter the search word:happy
2
'''