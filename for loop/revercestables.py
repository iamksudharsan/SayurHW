'''
4)
print the following
My Tables
Table  10
10 * 1 = 10
10 * 2 = 20
10 * 3 = 30
10 * 4 = 40
10 * 5 = 50
************
Table  8
...
....
Table  2
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
**********
End of table
'''

print("My Tables")
#Outer loop will have the inital value as 10 then its starts decr of -2
for multiplyer in range(10,0,-2): 
    print("Table ",multiplyer)
    #Inner loop will multiply with outer loop 
    for num in range(1,6): 
        print(multiplyer,"*",num,"=",multiplyer*num)
    print(f'{format*10}')
print("End of table")





# Output:
# My Tables
# Table  10
# 10 * 1 = 10
# 10 * 2 = 20
# 10 * 3 = 30
# 10 * 4 = 40
# 10 * 5 = 50
# **********
# Table  8
# 8 * 1 = 8
# 8 * 2 = 16
# 8 * 3 = 24
# 8 * 4 = 32
# 8 * 5 = 40
# **********
# Table  6
# 6 * 1 = 6
# 6 * 2 = 12
# 6 * 3 = 18
# 6 * 4 = 24
# 6 * 5 = 30
# **********
# Table  4
# 4 * 1 = 4
# 4 * 2 = 8
# 4 * 3 = 12
# 4 * 4 = 16
# 4 * 5 = 20
# **********
# Table  2
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# 2 * 4 = 8
# 2 * 5 = 10
# **********
# End of table
