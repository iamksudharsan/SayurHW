'''Calcualte and print users age - Write a program to ask the user for his/her name and print 'Hello', user's name.
Ask what year they were born.  get the year from the user. Print 'You are <age> years old'.
'''
# Getting user name and printing it
name=input("Enter your name:")
print("Hello "+name)

#getting the year of born 
year=int(input("Enter the year of born:"))

# to check the year in between years
if(year>1900 and year<2023):
    age=2023-year
    print("Your age is ",age)
# for expecton case of mismatch numbers
else:
    print("Enter a vaild year")

'''
Output:
Enter your name:sudharsan
Hello sudharsan
Enter the year of born:2003
Your age is  20
'''

