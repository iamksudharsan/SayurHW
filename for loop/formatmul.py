'''
3)print the following using two loop
My Table
Tabel  1
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
**********
Tabel  2
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
**********
End of table
'''

format='*'    # to formate in neat way to present
print("My Table")
for multipler in range(1,4): #Outer loop changes the multiplier
    print("Tabel ",multipler)  # to give info about the table no.
    for num in range(1,6):    #Inner loop changes number to mul
        print(multipler,"*",num,"=",multipler*num)
    print(f'{format*10}')   #format the string
print("End of table")

# Output:
# My Table
# Tabel  1
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 1 * 4 = 4
# 1 * 5 = 5
# **********
# Tabel  2
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# 2 * 4 = 8
# 2 * 5 = 10
# **********
# Tabel  3
# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9
# 3 * 4 = 12
# 3 * 5 = 15
# **********
# End of table
