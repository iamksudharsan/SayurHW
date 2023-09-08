'''The user just bought a few things in your  shop. Ask the user what he bought.
Cost of one vadai is Rs 30, one soda is Rs20 and one sandwich is Rs 100. Calculate the total cost.
Ask the user to pay the amount. Receive the amount from the user (get money as input). 
Print the change amount you have to give to the user. 
Hint - use float datatype'''

print("Welcome to Snacks Shop")
vadai=int(input("enter no of vadai:"))
vadaicost=vadai*30
soda=int(input("enter no of soda:"))
sodacost=soda*20
sandwich=int(input("enter no of sandwich:"))
sandwichcost=sandwich*100

# to get total cost
total=float(vadaicost+sandwichcost+sodacost)

#bill details
print("*******************************")
print("Items   Qty   price")
print("Vadai   ",vadai, vadaicost)
print("soda    ",soda, sodacost)
print("Sandwich",sandwich, sandwichcost)
print("TOTAL=",total)
print("******************************")

#get the money details from user
money=float(input("enter the given amount:"))

#check the given amount to cashier
if(money<total):
        need=total-money
        print("Money is not sufficient u need to pay Rs.",need)
else:
        need=money-total
        print("Money is excess of Rs.",need)


'''
Output:
Welcome to Snacks Shop
enter no of vadai:3
enter no of soda:2
enter no of sandwich:0
*******************************
Items   Qty   price
Vadai    3 90
soda     2 40
Sandwich 0 0
TOTAL= 130.0
******************************
enter the given amount:150
Money is excess of Rs. 20.0
'''