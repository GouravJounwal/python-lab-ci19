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
 #A list comprehension generally consist of these parts :

#1.Output expression,
#2.Input sequence,
#3.A variable representing a member of the input sequence and
#4.An optional predicate part. 
#A list of list for multiplication table 
a = 7
table = [[a, b, a * b] for b in range(1, 11)] 
  
print("\nMultiplication Table") 

    print (i) 
