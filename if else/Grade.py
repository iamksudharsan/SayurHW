'''We have 3 colleges - each college has a different cut off mark for engineering college admission.
Get the 5 marks from the student. Calculate the average. Find out which colleges the student is eligible to get admission.
For eg, College 1 cut off - 93%, College 2 - 89% and college 3 - 97%. If the student's avg is, 94%, the student is eligible
 for admission in College 1 and College 2.'''

#To get marks from user
matmark=int(input("Enter your maths mark:"))
phymark=int(input("Enter your physics mark:"))
chemark=int(input("Enter your chemistry mark:"))
langmark=int(input("Enter your language mark:"))
engmark=int(input("Enter your english mark:"))

#to get cutoff mark
cutoff=(matmark+phymark+chemark+langmark+engmark)/5

print("Your cutoff is",cutoff)

if(cutoff<=100):   # to check that the mark is less than 100
    if(cutoff>=97 and cutoff<=100):
        print("You are eligible in college 3 ,college 2 and also in college 1")
    elif(cutoff>=93 and cutoff<97):
        print("You are eligible in college 1 and also in colllege 2")
    elif(cutoff>=89 and cutoff<93):
        print("You are eligible in college 2")
    else:
        print("Sry u are marks is low to enter the college!")
else:  # expection cases
    print("Invalid cutoff")


'''
Output:
Enter your maths mark:97
Enter your physics mark:80
Enter your chemistry mark:96
Enter your language mark:90
Enter your english mark:97
Your cutoff is 92.0
You are eligible in college 2
'''