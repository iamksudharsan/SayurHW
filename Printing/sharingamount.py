'''geting the amount in hand of 3 person and dividing it mutualy
'''

a=1300;
b=3000;
c=2500;

#To know total money in hand
total=a+b+c;
print("Total money",+total);

#spend amount
spend=int(input("Enter the spend amount:"));
share=(total-spend)/3;

print("The sharable amount to three member is ",+share);

'''
Output:
Total money 6800
Enter the spend amount:3500
The sharable amount to three member is  1100.0
'''