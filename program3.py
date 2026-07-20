# program to  check whether number is even or odd.
num =int(input("Enter the number: "))
if num%2==0:
    print("The number is even")
else:
    print("The number is odd")


# program to check whether a person is eligible to vote or not.
age=int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


# program to check whether a number is positive, negative or zero.
num=int(input("Enter the number: "))
if num>0:
    print("The number is positive")
elif num<0:
    print("The number is negative")
else:
    print("The number is zero")


#program to check whether ayear is a leap year or not.
year=int(input("Enter the year: "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("The year is a leap year")
else:
    print("The year is not a leap year")


#program to check whether a character is vowel or consonant.
char=input("Enter a character: ")
if char in 'aeiouAEIOU':
    print("The character is a vowel")
else:
    print("The character is a consonant")
