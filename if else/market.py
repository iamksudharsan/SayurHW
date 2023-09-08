'''
Program to find out how many Kg of onion or tomato we can buy. One Kg of Onion is 20rs, Tomato is 10.5rs.  Input is the budget. 
7.1 Same as above, but the price of Onion is different based on the city. Chennai - Rs30, Trichy Rs27, Madurai Rs 34. Input is budget and city.
7.2 Same as above, but add 3% of the budget for petrol expenses
'''

# function to have different city price calculation
def shop(budget,city):
    # for chennai
    if(city=='CHENNAI'):
        onion=30
        petrolexp=budget-(0.03*budget)  # to find the petrol expens
        return(petrolexp//onion)
    # for trichy 
    elif(city=='TRICHY' ):
        onion=27
        petrolexp=budget-(0.03*budget)
        return(petrolexp//onion)
    # For madurai 
    elif(city=='Madurai'):
        onion=34
        petrolexp=budget-(0.03*budget)
        return(petrolexp//onion)
    # for expection cases
    else:
        return("Enter a vaild city")

# input from user
budget=int(input("Enter your budget:"))
incity=input("Enter the city (Chennai,Trichy,Madurai):")
city=incity.upper()

# to check the min budget is ok or not 
if(budget>9):

    # to call the function for city
    print("No of onion kg",shop(budget,city))
    tomato=10.5
    notomato=budget//tomato
    print("No of tomato kg",notomato)

#for expection cases
else:
    print("Budget is low")



'''
Output:
Enter your budget:200
Enter the city (Chennai,Trichy,Madurai):chennai
No of onion kg 6.0
No of tomato kg 19.0
'''