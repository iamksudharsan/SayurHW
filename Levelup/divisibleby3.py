'''Get a number from the user. Divide it by 3 and print the result. 
Divide again by 3 and print the result. Keep dividing until the number is less than 3. 
Print the number of times the number was divided.'''

#Asking user input
num = int(input("Enter a number: "))
count = 0

print("The number are after division by 3 from ",num,"to")
#Loop to divided the given number
while num >= 3:
    num /= 3
    print(num)
    count += 1

#Print the result
print("The result is ",num)
print("The number was divided ",count,"time(s).")


'''
Output:
Enter a number: 21
The number are after division by 3 from  21 to
7.0
2.3333333333333335
The result is  2.3333333333333335
The number was divided  2 time(s)

'''