'''Calcualte and print which standard the student is studying - Write a program to ask the user for his/her name 
and print 'Hello', user's name. 
Ask what year they were born.  
eg Hello Chitra, what year were you born?
get the year from the user. 
Calculate if the user is going to elementary school, middle school, highschool or college, based on users age.'''

# Getting user name and printing it
name=input("Enter your name:")

#getting the year of born 
year=int(input("Hello "+name+" ""what year were you born?:"))

# to check the year in between years
if(year>1000 and year<2023):
    age=2023-year
    print("Your age is ",age)
# for expecton case of mismatch numbers
else:
    print("Enter a vaild year")

#to find their group of studies by their age
if (age<5):
    print("Your are too young for school")
elif(age>5 and age<=11):
    print("You are studying elementary school")
elif(age>11 and age<=14):
    print("You are studying middle school")
elif(age>14 and age<=17):
    print("You are studying High school")
elif(age>17 and age<23):
    print("You are studying college ")
else:
    print("You have complete your clg life!")


'''
Output:
Enter your name:nivetha
Hello nivetha what year were you born?:2006
Your age is  17
You are studying High school
'''