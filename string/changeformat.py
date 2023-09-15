########## Program 3
#PigLatin - From the input string, for each word, remove the first, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay ythonPay



inputSentence = input("Enter a sentence: ") # Get input sentence from the user
pigLatinKey = 'ay'

for word in inputSentence.split():# Split the input sentence into words
    #If split word length is greater than 1 means the first letter will go end of the string
    if len(word) > 1:
        #To store the first letter of string
        firstChar = word[0]
        #To arrange the word format as 1 index posti letter to first and 0 index to end of the string
        word = word[1:] + firstChar + pigLatinKey
    
    #If the word contains only single letter as string then this case works
    if len(word)==1:
        firstChar=word[0]
        word=firstChar+pigLatinKey
    #To print the output
    print(word,end=" ")
    

'''
Output:
Enter a sentence: I am sudharsan
I maay udharsansay
'''