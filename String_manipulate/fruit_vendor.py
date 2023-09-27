'''
1. Write an app for the fruit vendor. Fruit vendor has a list of fruits (apple, Orange, banana etc).
When the customer comes in, vendor asks "What do you want to buy?" .
The customer can say "I want apple", or "Apple" or "three apple" or something like that.
Your program will find out what fruit the customer is asking. 
Your program will also find, if the customer already asked for the quantity of the fruit (one apple or 5 orange etc).
Print the quantity if the customer says the quantity. If not, ask him how much he wants.
Hint : Use string manipulation and lists. https://www.w3schools.com/python/python_ref_string.asp 
You can limit the quantity to single digit number.
'''

# List of available fruits
fruits = ["apple", "orange", "banana"]

# Main program loop
while True:
    customer_input = input("What do you want to buy? ").strip().lower()
    if customer_input == "exit":
        break  # Exit the program if the customer enters "exit"

    # Initialize variables to store fruit and quantity
    selected_fruit = None
    selected_quantity = 1  # Default quantity is 1 if not specified by the customer

    # Split customer input into words
    words = customer_input.split()

    # Iterate through words to find the fruit and quantity
    for word in words:
        if word in fruits:
            selected_fruit = word
        elif word.isdigit():
            selected_quantity = min(int(word), 9)  # Limit quantity to single digit

    if selected_fruit:
        print(f"You want {selected_quantity} {selected_fruit}.")
    else:
        print("Sorry, I couldn't understand your request. Please try again.TO close enter 'exit'")
    

# End of the program
print("Thank you for shopping with us!")