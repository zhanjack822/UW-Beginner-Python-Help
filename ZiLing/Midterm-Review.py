"""
Midterm review for cs 114

Instructor: Cameron Morland - cjmorland@uwaterloo.ca

This review will cover materials from module 1 to 6, from all the slides 
and the textbook materials

"""

"""
Let's start with the very basic

Types         name                        examples 

int          Interger                  3,4,-1,2325289524294
float   Float-Point Numbers            4.5,0.0,-4305.2458532
str          String                   'hello', "world", " ",''
bool         Boolean                   True,False, 1 == 1, 1 != 1
list          List                     [], [12,3.0432,'hello'],['a','b','v']
tuple         tuple                    (True,True,False),(),(23,43.2,"Tuple")
dict        Dictionary                 {2:4},{454:'ok','ok':'No'}
range         Range                    range(4),range(1,4302,45)
callable     Callable                  print(),count_To_Four(), f()
None         NoneType                          None
Further explination for each will be explained further later, now just note that 
these are all the types we are working with  
"""

# You can always use type() to check of the type of certain variable 
x = 3.23546548432741
print(type(x))

"""
Variables

Variable is "something" that has a value inside 
for example: 

x = 4 
regdhtweawf__ewgf43 = True 
name = "value"
are all variables 

be aware that the variable name cannot contain any special character 
other than '_' and it cannot start with a number
"""
n = 234
print(n)
"""
Function 

a sample function would be print()

All the def balabala(this:that) -> whocares: things you wrote are functions
function are composed in a few parts 

There are two types of function

Fruitful functions: returns something 
Void function: returns nothing 


here is some function for converting types 

int()     34.2 -> 34
float()    0 -> 0.0
str()      23.5 -> "23.5"
"""
# Here is a sample function with the name of their different parts 
# This function WILL NOT ACTUALLY RUN make sure to turn this off when you try to 
# Run other parts 
x = 0
def FunctionName (parameter:type) -> returnType:
    """
    Docstring that describes what is the return of this type 
    
    Restritoin: restrictions for this function
    """
    # Note, innerVariable only exists inside this function
    # if you call innerVariable outside of the function, error will show 
    # That this variable does not exist
    innerVariable = 'something'
    # But the function can access variables outside of itself
    x = 1 
    return 'this is the output of the function'

#when you call a function, you are typing its name and input the parameter
FunctionName("input")

# You can do math or print multiple things in a single line of print()
x = 9.81
print(3.53+5, "hello"+" world",x," m/s^2")

"""
While we are on the topic of function, lets talk about check 

import check 

check.expect("name of this test",function(parameter),expect Output)
check.within("the name",function(parameter),expect output, error range)

I hate it too much, that's all I want to say about it 
"""

"""
Comment 

#this thing is a comment
"""

#Comment will not be read by the computer
v = "aer" #You can put comment anywhere 
##Its awesome

"""
Algrebratical Expressions

+ - addition
- - subtraction 
* - multiplication
/ - division 
% - Modules
** - Exponentiation
// = Floor Division

Remember that there are two types of numbers 
int: Intergers, whole numbers 
float: Decimal numbers 

if you want more math, you have to use the math library 

import math 

then you can do all your wacky math.cos(),math.sine(),math.sqrt() stuff 

Down there are the example of some 
"""
# Module is the remain after division
# for example, 2/2 is 1, there is no remainder
# 3/2 can also be see as 2+1/2, the remainder will be 1 
print(2%2)
print(3%2)

# be aware of the difference in decimal places
print(2//3)
print(2/3)

# you can also use + and * on string 
word = "hello" + " world"
hohoho = 'ho'*3

"""
Assignment Operators (in-place operators)
You dont have to use them, but just know what they are 

= -> x = 5 
+= -> x += 3 is the same sa x = x + 3 
-= -> x -= 3 is the same as x = x - 3 
*= -> x *= 3 is the same sa x = x * 3 
/= -> x /= 3 is the same sa x = x / 3 
%= -> x %= 3 is the same sa x = x % 3 
**= -> x **= 3 is the same sa x = x ** 3 

there are more than these, but just know the onces above should be enough 
for you to go through this course

"""

# You cannot use two assignment operators on the same variable at the same line 
# But you can mix it with other algebretical operators 
x += 435+493/2302567

"""
Everything below will return a boolean value(True or False)

Comparison Oprators 

Operator   Name           Example
==         Equal          x == y, 2 == 1 
!=       Not Equal       x != 7, y != y
>      Greater than       3 > 2, 4 > 5
<       Less than         1 < 2, 5 < 5 
>=   Greater or Equal to   1 >= 1, 1 >= 4
<=   less or equal to      x <= 3 , 4 <= 4 

You usually use them with if statement or while statement
"""

# You can use more than one comparison operators in the same line 
for i in range (356,9,-3): 
    if 325 < i > 35:
        print (i)

"""
Logical Oprator 

operator    Returns True if          Example
and     both statements are true     x < 5 and x > 1 
or      either statement is true     x < 5 or x > 1 
not     the statement is false       not(x > 5)

Identity Operator 

operator    Returns True if          Example
is      both variables are the same   5 is 5, x is 5
is not  variables are not the same    x is not 4 

Membership Operator 

operator    Returns True if                 Example
in       object is element in smt        i in mydict
not in      object not in smth           i not in mydict     

All the operators above return a boolean type value (True or False)
"""

# You can mix mash all the operators together as long as it makes sense
for i in range (1,101):
    if not(x%2 == 0 and x > 5 ): 
        print (i)

"""
Conditional statements 

Statement      name   
if              if      
elif         else if
else           else
while          while 
"""

"""
Range

range is a type that gives a range of intergers, like how 
string is a sequence of characters, range is a sequence 
of integers

range(start,end,number between each)
"""
# This will not print out every value in range
print(range(4))

# This will
for i in range(4):
    print(i)

#After talking about math and boolean, lets talk a little about string 

"""
String 

String is a sequence of characters, or rather, a list of characters,
meaning all functions that works with list will work with string 
in the same way, for example 
"""
x = 'hello'
e = x[1] 

# len() function is used if you want the length of a list, in this case 
# a string

print(len('sorrynotsorry'))

# slice is used to get par of the string 

string = "string"
rin = string[2:5]
stri = string[:4]
ing = string[3:]
wholeString = string[:]
# you can also just do
st = 'string'[:2]

# you will get an empty string if the range is 0 
empty = "empty"[3:3]

"""
STRING IS IMMUTABLE

meaning you cannot change any single character inside a string 

Teaversals: ways to loop through the entire string, here are two traverals
"""

for letter in "string": 
    print(letter)

x = 0 
while x < len('string'):
    print('string'[x])
    x += 1

"""
str.format{}

This is a way used to format a string by inputting
different types into a string, for example

"this is a {} statement since the {}th value is {}".format(True,1,3.4)

you can use e to decide how many decimal places you want the number to be 
ex. {:.3e} will give three digit after the decimal 
"""
# your {} always have to be less than the parameter of format
print("{}{}".format(1,2,3,4,5))
# But print("{}{}".format(1)) will give an error 

# L I S T 
"""
List 

Lists are sequences of objects, it can be a list of anythinig 

when you write the type list, you have to CAPITALIZE the L

so List[Any] is correct, list[any] is not 

you can traversing the list the same way you traversing a string 
"""

L = [1,2,3,4]
for elements in L:
    print(elements)

#or you can use in range, in this case, i is the INDEX of each element
for i in range (len(L)):
    print(L[i])

x = 0
while x < len(L):
    print(L[x])
    x += 1

"""
YOU CANNOT USE OPERTAOR ON LIST TO MUTATE A LIST

you have to use list.append(smth)

list.extend(smth) takes in a list and add to the list being mutated

list.copy() can create a copy of the list 

list .pop(index) can pop out the speicific element of that index in the list

list.pop() just pops out the last 

list(string) makes a list to all the characters in a string

string.split() makes a list of all the words in a string seperated by empty space

string.split(string) make a list of all the characters, seperated by that string

list.joint(string) make a string out of the list, using the parameter string as a joint
"""

a = [2,3,4,5]
a.append(6)

#a will be [2,3,4,5,6]

# use + on list 
b = [6]
c = a + b 

a.extend(b)
#c = [2,3,4,5,6]

# use * on list 

c = b*4
#c = [6,6,6,6]

c = a.copy()
# c will become a shallow copy of a 
"""
List can be sliced just like string
"""

slice = ['a',2,'b',3]
a2 = slice[:2]

"""
sort() and sorted()

list.sort(key,reverse)

You can write your own function as key, these are called helper functions
"""
#This is how you mutate a list, key is a function
[2,3,4,5].sort(key = len, reverse = False)

#This is how you create a new list from the mutated list
list = sorted([2,3,4,5],key = len, reverse = False)

"""
Tuple 

Tuples are just lists that are immutable, tuple uses () instead of []

tuple(list) can turn a list in to a tuple 

"""
tuple = ('one',)
string = ('one')

"""
Dictionary 

Restriction: 
1. DOUBLICATE KEYS ARE NOT ALLOWED
2. KEY MUST BE IMMUTABLE

meaning that only INT, STR, FLOAT and TUPLE can be keys
"""

# the object before the semicolon is the KEY
# The object after the semicolon is the VALUE
d = {'d':1,'i':2,'c':3,'t':4}

"""
Range

a sequence

range(start , end, pattern)
"""

#for example, this r repersents a sequence starting from 203, -2 each time
#until it is smaller than 4
r = range(203,4,-2)

# you can turn a range into a list
mylist = list(r)

"""
Files

How to inport a file into the program and manipulate it

\n is the newline character, remember to end each line with a \n

the one below is the most basic .txt file
"""

#The r means to read the file, w is to write a file
with open("filename.txt","r") as myfile:
    print("do shits\n")
    # this line is an object, to print it, use repr(line)
    for line in myfile: 
        print(repr(line))
        #The split() method will turn a line into words seperated by space
        #split("p") will seperated a line into words by p
        for word in line.split(): 
            print(str(word))


with open("filename.txt","w") as f: 
    f.write("some shit\n")
    #Write can only take strings, so remember to convert everything to string
    f.write(str(2)+"\n")


"""
CSV files

comma seperated values

"""
import csv

with open("somefile.csv",'r') as csvfile:
    #Use a reader to seperate the csv file intoa reader format
    reader = csv.reader(csvfile)
    for line in reader:
        print(line)

    #or you can turn it into a list
    listcsv = list(csv.reader(csvfile))
        