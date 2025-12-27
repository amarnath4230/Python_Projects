
# Use will Input 3 ages you have to find the oldest one :-

age_1 = int(input("Enter your age: ")) # taking age 1 from user
age_2 = int(input("Enter your age: ")) # taking age 2 from user
age_3 = int(input("Enter your age: ")) # taking age 3 from user

# First Way Using Sort() function :------------------------------------
l = [age_1,age_2,age_3]
l.sort(reverse = True)
print(l[0])



# Second Way Using if statement:----------------------------------------------
max = age_1 
if max < age_2:
    max = age_2
if max < age_3:
    max = age_3
print(max)



