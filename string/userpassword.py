'''
Check if the username and password is correct. 
     Username should contain the char @  and '.com' or '.edu' or '.tech' or 'org' at the end.
     passward is the first, third, and last 3 letters of the username followed by the first three letters of the 
     name of the company mentioned in the username, followed by any 3 numbers.
     eg username : myname@sayur.com. password - mnamesay123 
'''


# Input username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if the username meets the criteria
if username.endswith(('.com', '.edu', '.tech', '.org')) and '@' in username:
    # Extract the first, third, and last 3 letters of the username
    username_parts = username.split('@')[0]
    #Totake the 0th index letter in username
    first_three = username_parts[0]
    #To take the 2nd index letter in username 
    third_letter = username_parts[2]
    #To take the last 3 index letters in username
    last_three = username_parts[-3:]
    
    # Extract the first three letters of the company name with first three letter in company name 
    company_name = username.split('@')[1][:3]

    # Check if the password matches the criteria
    #The password in the format of first_letter+third_letter+last_three_letter+company_name+123 for the given op
    expected_password = first_three + third_letter + last_three + company_name 
    #If user entered password is equal to program genterated espected password format 
    if password[0:8] == expected_password:
        #To check the last three digits is added in the password  
        if password[-3:-1].isdigit():
            print("Username and password are correct.")
        #To give info that the password need to add only the three digits numbers    
        else:
            print("Enter the three digits number in password!")
    #If the password in enterly wrong case scenirio
    else:
        print("Password is incorrect.")

#IF user name is wrong
else:
    print("Username does not meet the criteria.")


'''
Output:
Enter your username: myname@sayur.com
Enter your password: mnamesay456
Username and password are correct.

Enter your username: iamknownas@sudharsan.edu
Enter your password: imknassudh234
Password is incorrect.

Enter your username: iamironman@sudharsan
Enter your password: immansud456
Username does not meet the criteria.

'''