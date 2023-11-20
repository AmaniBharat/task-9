#1) EXPECTED OUTPPUT OF THE FOLLOWING CODE
data=[10,501,22,37,100,999,87,351]
result=filter(lambda x:x>4,data)#if we not use list 
print("the expected output is ")
print(result)
#OUTPUT:
the expected output is 
<filter object at 0x000001A67BD77A30>




#2)PYTHON CODE USING LAMBDA FUNCTION CHECK WHETHER EVERY ELEMENT IS INTEGER OR STRING
l=[1,2,3,4,5,6,7,'amani']
integers=list(map(lambda x: type(x),l))
print("the data type is\n ",integers)

#OUTPUT:
data type is
  [<class 'int'>, <class 'int'>, <class 'int'>, <class 'int'>, <class 'int'>, <class 'int'>, <class 'int'>, <class 'str'>]


#3)uSING LAMBDA FUNCTION CREATE FIBNOCCI SERIES 1-50
from functools import reduce
 
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
                                range(n-2), [1, 1]) 
print("Fibonacci series from 1 to 50:")
print(fib(50))

#OUTPUT:
Fibonacci series from 1 to 50:
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025]


4)#PYTHON FUNCTION TO VALIDATE THE REGULAR EXPRESSIION OF THE FOLLOWING
import re
#regex= r'\b[A-Za-z0-9]+@[a-z]+\.[a-z]{2,7}\b'
regex= r'\b[A-Za-z0-9]+@[a-z]+\.[a-z]{2,7}\b'
def emailvalidation(email):
    if re.fullmatch(regex,email):
        print("email is in correct format",email)
    else:
        print("email is not in correct format",email)
emailvalidation("amanidesu333@gmail.com")
emailvalidation("amanidesu333$@gmail.com")
regex1=r'\b[0-9]{10}\b'
def mobilenumber(mobile):
    if re.fullmatch(regex1,mobile):
        print("number is in correct format",mobile)
    else:
        print("the number is not in correct format",mobile)
mobilenumber('1234567890')
mobilenumber('126734567890')
regex2=r'^\([0-9]{3}\)\s[0-9]{3}\-[0-9]{4}$'# we can use space or \s for the white space
#regex2=r"\(\d{3}\) \d{3}-\d{4}"
def telephonenumber(number):
    if re.fullmatch(regex2,number):
        print("number in correct format",number)
    else:
        print("number is not in correct format",number)
telephonenumber("(555) 555-1234")
telephonenumber("6555 555-1234")
#regex3=r'\b[a-zA-Z0-9^#@!_*%$]{16}\b'#we cant write in ths format
regex3="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{16}$"
#regex3="^(?=.+[a-z])(?=.+[A-Z])(?=.+\d)(?=.+[@$!%*#?&])[A-Za-z\d@$!#%*?&]{16}$"#using + or * not showing much difference
def pass_word(password):
    if re.fullmatch(regex3,password):
        print("password is in correct format ",password)
    else:
        print(" PASSWORD not in correct format")
pass_word("AmaniGnanvika@58")
pass_word("amanignanvika@in")

#OUTPUT:
email is in correct format amanidesu333@gmail.com
email is not in correct format amanidesu333$@gmail.com
number is in correct format 1234567890
the number is not in correct format 126734567890
number in correct format (555) 555-1234
number is not in correct format 6555 555-1234
password is in correct format  AmaniGnanvika@58
PASSWORD not in correct format