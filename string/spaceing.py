########## Program 1
#Get an input string from the user. Add a space at every 3rd char.
#eg input = abcdefg , output = ab cd ef g



inputString = input("enter the string:")
i = 0 #counter to track the chars
newString = ""
#Loop to travers all the letter in the word with its index value
while i < len(inputString):
    newString += inputString[i:i+2] #(assign the from i, i+1 of inputString)
    newString += " " #add space
    i+=2
#check to add the chars at the end

#display the output
print (newString)


'''
enter the string:Wonderful
Wo nd er fu l
'''