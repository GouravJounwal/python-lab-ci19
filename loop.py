#1. Program to find digital sum of a given Number
ex: n=123 Digital sum----->1+2+3=6

x=input("Enter digits ")
sum=0
for i in x:
    sum=sum+int(i)
print(sum)

output-: Enter digits 123
                         6

#2. Program to find the digital product of a given number
ex: n=28 Digital product ----->2*8=16

x=input("Enter digits ")
num=1
for i in x:
    num=num*int(i)
print(num)

output-: Enter digits 28
                16

#3. Find the sum of the series 3 +33 + 333 + 3333 + .. n terms

x= int(input()) #3
n= int(input()) #10
sum=0
z=0
for i in range(n):
    z+=(x*(10**i))
    sum+=z
print(sum)

#4. Print the following pattern

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

for i in range (1,6):
    print('* '*i)
for i in range (4,0,-1):
    print('* '*i)
        
    
#5. .Program to reverse a given Number. ex: n=123 Reversed no is 321

temp=int(input())

x=0
while temp>0:
    x=x*10
    x=x+(temp%10)
    temp=temp//10

print(x)

    

