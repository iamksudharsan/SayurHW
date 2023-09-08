'''
Ask the user to input 3 numbers. Ask the user if they want to find the max of these numbers or minimum.
'''


#To find max of three number or min of these number

# function to find maximum value
def max(num1,num2,num3):
    if(num1>num2 and num1>num3):
        return num1
    elif(num2>num1 and num2>num3):
        return num2
    else:
        return num3

# function to find minimum value
def min(num1,num2,num3):
    if(num1<num2 and num1<num3):
        return num1
    elif(num2<num1 and num2<num3):
        return num2
    else:
        return num3

# To get the three number from user
first=int(input("Enter the first number:"))
second=int(input("Enter the second number:"))
third=int(input("Enter the third number:"))

# To know the user need to find min or max 
choice=int(input("Enter 1 to find minimum or else 2 to find maximum:"))

# To call the function of there choice
if(choice==1 or choice==2):
    if(choice==1):
        print("Minimum value is ",min(first,second,third))
    else:
        print("Maximum value is ",max(first,second,third))
else:
    print("Enter vaild option!")

'''
Output:
Enter the first number:34
Enter the second number:43
Enter the third number:23
Enter 1 to find minimum or else 2 to find maximum:2
Maximum value is  43

'''