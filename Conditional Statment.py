#1. Given two integer numbers return their sum. If the sum is greater than 100, then return their product.

x=int(input())
y=int(input())

s=x+y

if s>100:
    print("Product is",x*y)
else:
    print("Sum is",s)

#2. Write a Python program to calculate the sum of three given numbers, if the values are not - equal then return four times of their sum

x=int(input())
y=int(input())
z=int(input())

if x==y and y==z and z==x:
    print(x+y+z)
else:
    print(4*(x+y+z))

#3. To check whether a number is divisible by 8 and 12 or not.

x=int(input())

if (x%8)==0 and (x%12)==0:
    print("Divisible by 8 and 12")
else:
    print("Not-divisible")

#4. To check whether a given number is even or odd.

x=int(input())

if x%2==0:
    print("even")
else:
    print("odd")

#5. A student will not be allowed to sit in exam if his/her attendence is less than 80%.
#Take following input from user Total Number of classes held Total Number of classes attended. And print percentage of class attended. Is student is allowed to sit in exam or not.

a=int(input("Number of classes held:"))

b=int(input("Number of classes attended:"))

percentage=b/a*100

if percentage>=75:
    print("The student is allowed to sit in the exam hall")
else:
    print("The student is not allowed to sit in the exam hall")

