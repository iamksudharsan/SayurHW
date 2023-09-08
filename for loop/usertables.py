'''6)Challlenge program'''


#Get the multiplier from user
number=int(input("Enter the multiper number:"))
#Get the choice from user
choice=int(input("Enter 1 for basic/n2 for advance /n 3 for both"))
print("My Tables",number)
if(choice>0):   # to check that the give choice is number
# if choice is 1 or 3 it will executed the basic multiplication
    if(choice==1 or choice==3):  
        print("Basic numbers")
        for num in range(1,11):
            print(number,"*",num,"=",number*num)
  # if choice is 1 or 3 it will executed the basic multiplication
    if(choice==2 or choice==3):
        print("Advanced numbers")
        for num in range(11,21):
            print(number,"*",num,"=",number*num)
        print(f'{format*10}')
else:
    print("Invalid choice")
print("End of table")



'''
Output:
Enter the multiper number:1
Enter 1 for basic/n2 for advance /n 3 for both:3
My Tables 1
Basic numbers
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
1 * 7 = 7
1 * 8 = 8
1 * 9 = 9
1 * 10 = 10
Advanced numbers
1 * 11 = 11
1 * 12 = 12
1 * 13 = 13
1 * 14 = 14
1 * 15 = 15
1 * 16 = 16
1 * 17 = 17
1 * 18 = 18
1 * 19 = 19
1 * 20 = 20
**********
End of table

'''