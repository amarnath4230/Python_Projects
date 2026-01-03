# Write  a program that will tell whether the given number is divisible by 6 or not ?

num = int(input("enter a number: "))

if num % 2 == 0 and num % 3 == 0:
    print(num,"is divisible by 6")

else:
    print(num,"is not divisible by 6")
    
        