# program to compute sum of n natural numbers and find average of that numbers using  while loop.
n = int(input("enter a number:"))
i =1
sum =0
while (i<n):
    sum = sum +i
    i = i + 1

avg =sum/n;
print("The sum of n natural number is :",(n,sum))
print("The average of n natural numbers is :",(n,avg))


# program to compute sum of n natural numbers and find average of that numbers using  for loop.
n = int(input("enter a number:"))
sum =0
for i in range(1,n):
    sum = sum +i        

avg =sum/n;
print("The sum of n natural number is :",(n,sum))       
print("The average of n natural numbers is :",(n,avg))

# program to compute square of n natural numbers using  while loop.
n = int(input("enter a number:"))
i =1
while (i<=n):
    sum = i*i
    i = i + 1
    print("The square of n natural number is :",sum)

