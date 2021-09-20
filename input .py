print("enter a no.")
a = input()
print("you entred", a)
print(type(a)) # by defalt it will we string type
num1=int(input("Enter 1st no:"))
num2=int(input("Enter 2nd no:"))
num3=int(input("Enter 3rd no:"))
avg=(num1+num2+num3)/3
print ("The average is: " + str(avg))
#format
print("{}, Welcom to AITR"
      .format("Welcom Everyone"))
 

str = "This program is written in {}"
print(str.format("Python"))
 
print("Hello, I am {} years old !".format(19))
#split
text= 'Hello Everyone'

# splits at space
print(text.split())

name= 'Gourav, Rohit, hgjkj'

# splits at ','
print(name.split(', '))
