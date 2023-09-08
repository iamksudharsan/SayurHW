'''you have three coin ,value1,3 and 5 give a number ,you need to find the minimum coins required
'''


#initalize the countof each rupee in each variable is starting at zero
countof5=0
countof3=0
countof1=0

# To get the amount from user
amount = int(input("Enter the amount:"))
# to check the give amount is greater than 0
if(amount>0):
# temp to store the amount and to process 
    money=amount
# Loop to reduce the money value by each conditions
    while money > 0:
    # to check the it can be reduced by Rs.5 coins
        if money >= 5:
            # by reducing 5 rupee in money and also count value increase by 1 
            countof5+=1   
            money-= 5
    # to check the it can be reduced by Rs.3 coins
        elif money >= 3:
            # by reducing 3 rupee in money and also count value increase by 1 
            countof3=+1    
            money-= 3
    # to check the it can be reduced by Rs.1 coins
        else:
            # by reducing 1 rupee in money and also count value increase by 1
            countof1+=1    
            money-= 1

#expection case            
else:
    print("Invalid amount")


# to print the output
print("For amount of",amount,"minimum coins required: ",countof1+countof5+countof3)
if(countof5!=0):
    print("Rs.5 x",countof5)
if(countof3!=0):
    print("Rs.3 x",countof3)
if(countof1!=0):
    print("Rs.1 x",countof1)


'''
Output:
Enter the amount:34
For amount of 34 minimum coins required:  8
Rs.5 x 6
Rs.3 x 1
Rs.1 x 1
'''