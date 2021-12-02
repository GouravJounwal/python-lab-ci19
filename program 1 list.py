odd_square = [x ** 2 for x in range(1, 10) if x % 2 == 1] 
print (odd_square) 
  

odd_square = [] 
for x in range(1, 10): 
    if x % 2 == 1: 
        odd_square.append(x**2) 
print (odd_square) 
  

power_of_2 = [2 ** x for x in range(1, 5)] 
print (power_of_2) 
  

noprimes = [j for i in range(2, 8) for j in range(i*2, 30, i)] 
primes = [x for x in range(2, 30) if x not in noprimes] 
print (primes) 
  
# list for lowering the characters 
print ([x.lower() for x in ["A","B","C","G"]] )
  
# list which extracts number 
string = "my phone number is : 121212 !!"
  
print("\nExtracted digits") 
numbers = [x for x in string if x.isdigit()] 
print (numbers) 
 
  
  1. Python program to insert a number to given position in a list.

x=[1,2,3,4,5,7,8,9]

pos=5

x.insert(pos,6)   #insert 6 after 5th postion
print(x)

output -: [1, 2, 3, 4, 5, 6, 7, 8, 9]

2.  Python program to delete an element from a list by index which is given by the user.
In [18]:
x=[1,2,3,4,5,62,6,7,8,9]

delete=5

del x[delete]    #delete 5th element in list
print(x)

output-: [1, 2, 3, 4, 5, 6, 7, 8, 9]


3. list for lowering the characters 

print ([x.lower() for x in ["A","B","C","G"]] )

output-: ['a', 'b', 'c', 'g']
4.  list which extracts number 

string = "my phone number is : 121212 !!"
  
print("\nExtracted digits") 
numbers = [x for x in string if x.isdigit()] 
print (numbers)

output-: Extracted digits
['1', '2', '1', '2', '1', '2']


5. .Write a Python program to find all the values in a list are greater than a given number.

x=[1,2,3,4,5,6,7,8,9]

x.sort()
num=5

i=x.index(num)

print(x[i+1:])

output-: [6, 7, 8, 9]
 

