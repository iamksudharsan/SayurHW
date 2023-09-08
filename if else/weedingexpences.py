'''
Calculate wedding expenses. Cost for lunch per person is Rs200. Cost for Breakfast per
 person is half of lunch cost. Cost of the hall is Rs 200 per person.
  Decoration is 50% of Hall cost. Parking is 10% of the Hall cost. 
  Decide what should be the input and calculate the cost.
  
  Start with the above. The total cost is split equally by bride and groom.
 Bride has saved Rs50000. Determine if the bride has to take a loan or not. 
 If loan, how much?
 '''

# declaration for money in hands by bride
inhand=50000

# input from user to the people are going to attend the wedding
person=int(input("Enter no of person coming to wedding:"))

if(person>=25):
    
    # to caluclate the expens
    lunch=person*200
    breakfast=lunch*(0.5)
    hall=person*200
    decoration=hall*(0.5)
    parking=hall*(0.1)

    # to find the total cost
    total=lunch+breakfast+hall+decoration+parking

    # printing the cost
    print("Lunch cost is ",lunch)
    print("Breakfast cost is",breakfast)
    print("Hall cost is",hall)
    print("Decoration cost is",decoration)
    print("Parking cost is",parking)
    print("Total cost is",total)

    # to know the required amount if it excess
    if(total>50000):
        loan=total-inhand
        print("Loan needed amount is ",loan)
        print("Have happy maried life!")

    # if money is fine
    if(total<50000):
        print("Your have enough money in your hand So don't need to take loan")
        print("Have happy maried life!")

    
else:
    print("Have more members in ur marriage")


'''
Output:

Enter no of person coming to wedding:75 
Lunch cost is  15000
Breakfast cost is 7500.0
Hall cost is 15000
Decoration cost is 7500.0
Parking cost is 1500.0
Total cost is 46500.0
Your have enough money in your hand So don't need to take loan
Have happy maried life!
'''
 