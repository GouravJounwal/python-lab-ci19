add = lambda x, y: x + y
print (add (50, 8))
x="some kind of a lambda"
(lambda x : print(x))(x)


#filter 
list1= [1,2,3,4,5,6,7,8,9,10]
result=list(filter (lambda x:x%2==1,list1))
print(result)

#map 
list2=[1,3,5,7,9,11]
re=list((map(lambda x:x*2, list2)))
print(list(re))

#reduce
#import reduce from the functools module
from functools import reduce
list3= [1,2,3,4,5]
R= reduce (lambda x, y: x*y, list3)
print(R)
