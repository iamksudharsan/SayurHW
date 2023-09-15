'''
Use For loop, break and continue as needed.
You need Rs 1000 to go to movie. you are asking your parents for money. your parents give you a
some money. Ask your parents for money until you get Rs1000 or a maximum of 5 times.
Each time they give you some money, you need to print how much money you got so far and print "Thank you.".
Print "Thank you " only if the money is > Rs 10. If money is less than or = Rs 10, don't add it
towards the Rs1000 that you need. Use Continue stmt as needed.
Print how many times you had to ask your parents to get this money.
'''

#initial variable
money=0
count = 0

#Loop for amount geting from user 
for amount in range(5):
    given_amount = int(input("Enter the amount of money your parents gave you: "))
    
    #If amount is less than 10
    if given_amount <= 10:
        print("Thank you, but this amount won't help towards reaching Rs 1000.")
        continue
    
    #Else amount will be add to total amount
    money += given_amount
    count += 1
    print(f"Thank you. Total money collected so far: {money}")
    
    if money >= 1000:
        print("Congratulations! You have collected enough money.")
        break

else:
#if total_money < 1000:
    print("Unfortunately, you were unable to collect enough money after asking 5 times.")

print(f"Total times asked:{count}")


'''
Output:
Enter the amount of money your parents gave you: 150
Thank you. Total money collected so far: 150
Enter the amount of money your parents gave you: 260
Thank you. Total money collected so far: 410
Enter the amount of money your parents gave you: 5
Thank you, but this amount won't help towards reaching Rs
1000.
Enter the amount of money your parents gave you: 350
Thank you. Total money collected so far: 760
Enter the amount of money your parents gave you: 450
Thank you. Total money collected so far: 1210
Congratulations! You have collected enough money.
Total times asked:4

'''