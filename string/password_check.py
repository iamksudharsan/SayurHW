'''
1. Print the level of the password security and if the password is acceptable
    Weak - only alphabets or only numbers or only special chars
    Ok - at least one alphabet, one number and one special char
    strong - at least three alphabets, two numbers and one special char
    Very strong - same as strong, but at least 16 count

    All passwords must be at least 8 chars long. You can use RegEx if you want.

'''


#To import RedEx modules (RegularExpression)
import re

# Input password to check
password = input("Enter your password: ")

# Check if the password is at least 8 characters long
if len(password) < 8:
    print("Weak - Password must be at least 8 characters long")
else:
    # Count the number of alphabets, numbers, and special characters using regex
    #It counts only number of alphabets in password
    alphabets_count = len(re.findall(r'[a-zA-Z]', password))
    #It counts only no.of numbers in password
    numbers_count = len(re.findall(r'[0-9]', password))
    #It counts only number of special symbols in password
    special_chars_count = len(re.findall(r'[^a-zA-Z0-9]', password))

    # Check the criteria for different password strength levels
    if alphabets_count == 0 or numbers_count == 0 and special_chars_count == 0:
        print("It is at Weak-Level")
    #if the password is ok level
    if alphabets_count > 1 and numbers_count > 1 and special_chars_count == 0:
        print("It is at Ok-Level")    
    #To check whethere the password is strong or very strong 
    if alphabets_count >= 3 and numbers_count >= 2 and special_chars_count >= 1:
        if len(password) >= 16:
            print("It is at Very strong Level")
        else:
            print("It is at Strong - Level")

'''
Output:
Enter your password: sudharsan
It is at Weak-Level

Enter your password: $udhar$an21092003
It is at Very strong Level

Enter your password: Sudharsan21
It is at Ok-Level

Enter your password: $udharsan21
It is at Strong - Level

'''   
    