#print a multiplication table like below.
#get user intput for start and end numbers. 
#the following example uses 1 to 5.
'''
     1  2  3  4  5
  ********************
1 |  1  2  3  4  5
2 |  2  4  6  8 10
3 |  3  6  9 12 15
4 |  4  8 12 16 20
5 |  5 10 15 20 25
'''


# Get user input for start and end numbers
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

# Print the header row
print("     ", end="")
for i in range(start, end + 1):
    print(f"{i:4}", end="")
print("\n"+"*" * (25))

# Print the multiplication table
for i in range(start, end + 1):
    print(f"{i:2} |", end="")
    for j in range(start, end + 1):
        print(f"{i * j:4}", end="")
    print()


'''
Output:
Enter the start number: 1
Enter the end number: 5
        1   2   3   4   5
*************************
 1 |   1   2   3   4   5
 2 |   2   4   6   8  10
 3 |   3   6   9  12  15
 4 |   4   8  12  16  20
 5 |   5  10  15  20  25
'''