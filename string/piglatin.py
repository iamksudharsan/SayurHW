########## Program 4
#PigLatin - From the input string, for each word, remove the first chars until a vowek, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay nPythoay (in Python 'o' is the first vowel)


inputSentence = input("Enter a sentence: ") # Get input sentence from the user
#To ad ay in end 
pigLatinKey = 'ay'
#Vowel check list
vowels = ['a', 'e', 'i', 'o', 'u']

# Split the input sentence into words
for word in inputSentence.split(): 
    #To find the index value of the first vowel in it
    first_vowel_index = 0
    # Iterate through the characters in the word
    for index, char in enumerate(word): 
        if char in vowels:
            first_vowel_index = index
            break # Break the loop when the first vowel is found

    word = word[first_vowel_index] + word[:first_vowel_index] +word[first_vowel_index+1:]+ pigLatinKey
    print(word,end=" ")


'''

'''