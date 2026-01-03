
# Write a python program to swap to numbers ? i.e if x = 2 , y = 4 then interchange value of x with y and value of y with x .

x = int(input("Enter Number 1: "))
y = int(input("Enter Number 2: "))

print("Value of X and Y before swapping")
print("X = ",x)
print("Y = ",y)

x , y = y , x

print("Value of X and Y after swapping")
print("X = ",x)
print("Y = ",y)




