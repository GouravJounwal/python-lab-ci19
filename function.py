#1. Write a Python function that takes a list of words and returns the length of the longest one.

def maxLength(n):
    
    max=-1
    word="null"
    for i in n:
        if len(i)>max:
            max=len(i)
            word=i
    return word,max

lis=["hello","my","name","is","Gourav"]

print(maxLength(lis))

#output-: ('Gourav', 6)


#2. Write a function x(n) for computing an element in the sequence xn=n^2+1. Call the function for n=4 and write out the result.

def x(n):
    return (n**2 + 1)

print(x(4))

#output-: 17


#3. Take the following Python code that stores a string: ‘str = 'Y-tatata-acropolis: 0.8475'. Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.

str = 'Y-tatata-acropolis: 0.8475'

x=str.find(':')
y=str[x+1:]

print(float(y))

#output-: 0.8475


#4. Write a function that returns the middle value among three integers. (Hint: make use of min() and max()). Write code to test this function with different inputs.

x=list(map(int,input().strip().split()))
x.sort()
print(x[1])

#output-: 12 47 32
#32


#5. Write a Python function to display all the multiples of 7 & 9 within the range 100 to 500.
In [4]:
def fun(x):
    if(x%7==0):
        print(x,end=" ")
    elif x%9==0:
        print(x,end=" ")
    
    if x>500:
        return 
    else:
        fun(x+1)
        
fun(100)
