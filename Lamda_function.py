#1.	Add by lambda
add = lambda x, y: x + y
print (add (50, 8))

#output-:58

#2.	simple funtion to multiply 2 numbers

x= (lambda a,b:a*b)(6,5)
print(x)

#output-:30

#3.	simple function to cube a number

x=(lambda a:a*a*a)(5)
print(x)

#output-: 125

#4.add 2 list

x=[2,3,4,5,6]
y=[5,4,3,2,1]
z=list(map(lambda a,b:a+b,x,y))
print(z)

#output-: [7,7,7,7,7]


#5. print table of 5 using lambda functions
   # j is equal to x where x is 5 times j and x is in range 1 to 10

table=[lambda j=x:5*j for x in range(1,11)]

#print(table)

for i in table:
    print(i())

#output -: 
#5
#10
#15
#20
#25
#30
#35
#40
#45
#50
