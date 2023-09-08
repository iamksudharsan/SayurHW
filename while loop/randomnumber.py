'''######## Problem 2 ###############
# Computer will guess a random number. 
# user has to guess that number. for each guess, print 'High' or 'Low'
# eg - computer number - 189
# user guess 56 - print low
# user guess 678 - print high
# Get user input and print 'high' or 'low' until the user guesses the number correctly 
# https://www.w3schools.com/python/ref_random_randint.asp - read this to learn how to create a random number
'''
#Import random module or package
import random
#Randomly numeber will be generated
computerNo=random.randint(1,10)

#inititalize variable to count the attempt
attemt=0

#Loop to continue the both have the correct number guesses
while(True):
    #Asking the input guess from user
    userNo=int(input("Enter the numbers:"))
    #If guess is low
    if(userNo<computerNo):
        print("Your guess is low")
    #if guess is correct
    elif(userNo==computerNo):
        print("Your guess is correct")
        break
    #if guess is high
    else:
        print("Your guess is high")
    attemt+=1   

#Final output display
print(f"User guess the number in {attemt} chance and the random number is {computerNo}")


'''
Output:
Enter the numbers:5
Your guess is low
Enter the numbers:7
Your guess is low
Enter the numbers:9
Your guess is high
Enter the numbers:8
Your guess is correct
User guess the number in 3 chance and the random number is 8

'''