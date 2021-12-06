#1.
print("enter a no.")
a = input()
print("you entred", a)
 
#2.
num1=int(input("Enter 1st no:"))
num2=int(input("Enter 2nd no:"))
num3=int(input("Enter 3rd no:"))
avg=(num1+num2+num3)/3
print ("The average is: " + str(avg))

#3.  Display float number with 2 decimal places using print()
I
x=10.4996
print("%.2f"%x)

#4. Takes two integer numbers and return their product.

x= int(input()) 
y= int(input()) 

print("product is",x*y)

#5. Write a Python program to get the volume of a sphere with radius 10.
r=int(input("Enter radius "))
print("Volume of sphere is ",(4/3)*3.14*r*r*r)

#6. Write a Python program that accepts an integer (a) and computes the value of a+aa+aaa.

a= int(input("Enter the number"))

print("a+aa+aaa=",a+(a+10*a)+(a+10*a+100*a))

