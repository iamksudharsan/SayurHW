#Write a program for a bag shop. Shop has 100 red bags (each Rs 1000) and 200 white bags (each Rs 1500)
#Customers can buy one or more bags at a time.
#The program ends when the sales reached Rs10000 or at least 10 bags are sold. 
#Display total sales and total number of bags sold

#initialize variables
redBags,whiteBags = 100, 200
totalSales=totalBagsSold = 0
redcount=whitecount=0

#Loop to check the conditions of sales amount greater than 10k and more than 10 bages
while totalSales < 10000 and totalBagsSold < 10:

    #To know the info of bages in stocks
    print(f"Available bags - Red: {redBags}, White: {whiteBags}")
    #To ask the choice from user
    bagchoice =int(input("Enter 1 for red and 2 for white:"))

    #Expectional cases
    if 0<bagchoice>2:
        print("Invalid bag color. Please enter '1' or '2'.")
        continue

    #To know the number of bages required    
    quantity = int(input("Enter quantity to purchase: "))
    
    #To have the sufficient bages or not checking case
    if bagchoice == 1 and  quantity > redBags:
        print("Not enough red bags available.")
        continue
    #To have the sufficient bages or not checking case
    elif bagchoice == 2 and quantity > whiteBags:
        print("Not enough white bags available.")
        continue
    
    #if choice is Red bags   
    if bagchoice == 1: 
        cost_per_bag = 1000  #cost of red bags
        total_cost = cost_per_bag * quantity
        redBags -= quantity  #To update the bags 
        redcount+=quantity  #To know the count
    
    #if choice is Red bags 
    if bagchoice == 2:
        cost_per_bag = 1500    #cost of red bags
        total_cost = cost_per_bag * quantity
        whiteBags -= quantity   #To update the bags
        whitecount+=quantity     #To know the count
    
    totalSales += total_cost
    totalBagsSold += quantity

#To print The final information of bages sold list
print(f"Total Sales: Rs {totalSales}")
print(f"No of red bags sold:{redcount}")
print(f"No of white bags sold:{whitecount}")
print(f"Total Bags Sold: {totalBagsSold}")


'''
Output:
Available bags - Red: 100, White: 200
Enter 1 for red and 2 for white:1
Enter quantity to purchase: 4

Available bags - Red: 96, White: 200
Enter 1 for red and 2 for white:2
Enter quantity to purchase: 5

Total Sales: Rs 11500
No of red bags sold:4
No of white bags sold:5
Total Bags Sold: 9

'''