#1. #declaring a string

 s= ‘gourav’

#capitalize
s.capitalize()
Output -: GOURAV

#2. #uppercase then lowercase conversioon
print(s.upper())
print(s.lower())

output -: GOURAV
                 gourav

#3. #find a character in string

x=s.find('v')
print("v is at",x,"place")

Output -:  v is at 5 place

#4. triple quotes string can extend multiple lines

my_string = """Hello, Welcome to my repostiory of
            Python lab files"""
print(my_string)


#5.
var1 = 'Hello World'
var2 = "Hello Everyone welcome"

print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[6:10])

var1 = 'Hello World'
print ("Updated String : ", var1[:6] + 'Python')

print ("this is %s and age is %d kg" % ('Gourav', 19))

