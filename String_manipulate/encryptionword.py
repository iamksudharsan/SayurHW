'''
2. Input is an encrypted  string where there will be chars followed by number. The way to decrypt is 
to repeat the chars, by the number of times. Print the decrypted word and its length. If there are any special 
chars, all the chars between the number and special char are ignored.
 eg - ac2bd3 means acacbdbdbd. 
 ac2acc#cd3 acaccdcdcd
'''

import re

# Get the encrypted string from the user
encrypted_str = input("Enter the encrypted string: ")

# Define a regular expression pattern to match char followed by number
pattern = r'([a-zA-Z]+)(\d+)([^a-zA-Z]*)'

# Initialize an empty decrypted string
decrypted_str = ""

# Find all matches in the input string
matches = re.findall(pattern, encrypted_str)

#Loop to change the encrypted
for word in matches:
    chars = word[0]
    count = int(word[1])
    decrypted_str += chars * count

# Print decrypted string and its length
print("Decrypted String:", decrypted_str)

'''
Output:
Enter the encrypted string: af2eg1
Decrypted String: afafeg
'''