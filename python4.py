# program to check  number is 10, 50,100 or not.

num= int(input("Enter a number: "))
if num==10:
    print("The number is 10")
elif num==50:
    print("The number is 50")
elif num==100:
    print("The number is 100")
else:
    print("The number is not 10, 50 or 100")


#program to take marks and displya grades

marks= int(input("Enter your Marks:"))
if marks>=80 and marks<=100:
    print("Your Grade is A")
elif marks>=70 and marks<=80:
    print("Your Grade is B")
elif marks>=60 and marks<70:
    print("Your Grade is C")
elif marks>=50 and marks<=60:
    print("Your Grade is D")
elif marks>=40 and marks<=50:
    print("Your Grade is E")
elif marks>35 and marks<=40:
    print("Your Grade is F")
else:
    print("You are Fail")


# program to check number is positive, negative or zero.

num = int(input("Enter a number: "))
if num >= 0:
    if num ==0:
        print("The number is zero")
    else:
        print("The number is positive")
else:
    print("The number is negative")     


# program to check whether a number is divisible by 5 and 11 or not.

num = int(input("Enter a number: "))
if num % 5 == 0 and num % 11 == 0:
    print("The number is divisible by both 5 and 11")
else:
    print("The number is not divisible by both 5 and 11")


# program to check whether a number is divisible by 5 or 11 or not.

num = int(input("Enter a number: "))
if num % 5 == 0 or num % 11 == 0:
    print("The number is divisible by either 5 or 11")
else:
    print("The number is not divisible by either 5 or 11")

