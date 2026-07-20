
# Program to check if the first number is greater than or equal to the second number
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

if a>=b:
    print("True")
else:
    print("False")


#python program to calculate area of square
side=input("Enter the side of square:")
area=int(side)**2
print("Area of square is:",area)


# Program to check whether the greater number among three numbers.
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))

if a>b and a>c:
    print("a is greater than b and c")
elif b>a and b>c:
    print("b is greater than a and c")
elif c>a and c>b:
    print("c is greater than a and b")
else:
    print("All numbers are equal")
