'''
3. Write the function mostFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated the same), returns a lowercase string containing the letters of s in most frequently used order. (In the event of a tie between two letters, follow alphabetic order.)
Eg - "We Attack at Dawn" is input. Output should be 'atwcdekn'
Do not use dictionaries. Try to use string built in functions.
'''

input=input("Enter the string:")
a=input.lower()
a=a.replace(" ", "")
res=''.join(sorted(a))
print(res)

sorted_word = ''.join(sorted(set(res)))
print(sorted_word)
#print(a)

#atwcedkn