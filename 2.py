
# Write a python program in which User will Input 3 ages you have to find the oldest one ?

age_1 = int(input("Enter Your first age: "))
age_2 = int(input("Enter Your second age: "))
age_3 = int(input("Enter Your  third age: "))

max_age = age_1
if age_2 > max_age:
    max_age = age_2
if age_3 > max_age:
    max_age = age_3
print(max_age,"is maximum age")







