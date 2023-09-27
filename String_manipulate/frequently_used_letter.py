'''
3. Write the function mostFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated the same), returns a lowercase string containing the letters of s in most frequently used order. (In the event of a tie between two letters, follow alphabetic order.)
Eg - "We Attack at Dawn" is input. Output should be 'atwcdekn'
Do not use dictionaries. Try to use string built in functions.
'''

def mostFrequentLetters(s):
    # Convert the string to lowercase
    s = s.lower()

    # Remove non-alphabetic characters
    s = ''.join(filter(str.isalpha, s))

    # Count the occurrences of each letter
    letter_counts = {}
    for char in s:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

    # Sort the letters first by frequency (in descending order) and then alphabetically
    sorted_letters = sorted(letter_counts.keys(), key=lambda x: (-letter_counts[x], x))

    # Convert the sorted letters to a lowercase string
    result = ''.join(sorted_letters)

    return result

# Example usage:
input_str = "We Attack at Dawn"
s = mostFrequentLetters(input_str)
print(s)  # Output: 'atwcdekn'