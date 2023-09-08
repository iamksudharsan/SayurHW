'''Get two names. If the length of the two names is not equal, add 'a' at the end of the short name
    until the length is equal. 
    Eg - input - cat, arrow. (legnth is not equal) 
    Output - cataa, arrow (length is equal by adding a)'''

# get the  string from user
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Make the names equal in length
name1 += 'a' * (len(name2) - len(name1))
name2 += 'a' * (len(name1) - len(name2))

# Print the result
print("Output ",name1, name2)



'''Output:
Enter the first name: ram
Enter the second name: deepan
Output  ramaaa deepan
'''