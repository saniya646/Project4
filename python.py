print("hello world!")

# comment in python  (single line comment)
""" 
mutiline comment
"""

#variable
number=5
number1=7
first_name_of_person=6

#camelcase
# means we write the code in this form thePersonIsGood

number=5
number1=7
print(number) # op is 5
print("number") # op number

number1=5
number1=7
#we get th op as 7

text="saniya" #we can give the text for var but we need to use ""

Name="saniya"
age=19
print(Name,age)

x,y,z=23,24,25
print(z)#op is 25
print(x,y,z)#op is 23,24,25

#datatypes
##################
number1=56   #integer
number2=9.5  #float(decimal point)
number3="sani" #string
number4=True or False  #boolean

#type()
print(type(number1)) #op is <class 'int'>
#it declare the type of given data
print(type(number2))#po is <class 'float'>

#Converstions
#################
demo1=24
print(float(demo1)) #it conert 24 into float value op is 24.0


result=float(demo1) #integer
print(result) #op is 24.0
print(type(result))#op is <class 'float'>

demo1=24.4
print(int(demo1))#op is 24

demo1=23
result=str(demo1)
print(result) #op 21
print(type(result)) #op is <class 'str'>

#String
############

text="sani"
print(text) #op sani
print(text[0]) #op is s
text="Hello World!"
print(text[6])# op is space

text="helloworld"
print(len(text)) # op is 10
print(text[0:5]) #op is hello
#all other - index no
#count - len
print(text[5:11]) # op is world

#uppercase and lowercase
###############################

text="helloworld"
print(text.upper()) #op HELLOWORLD
print(text.lower()) #op helloworld

#INDENTATION is must in python

x=1
y=1.2
z="sani"
a=True #boolean  1
b=False # 0
print(a) #op is True

number=5
print(number==10)# op is False
print(number==5) # op is True

#Operators :used to perform the operations
##################
"""
Arithemetic op
assignment op
comparision op
logical op
identify op
membership op
bitwise op
"""

#Arithemetic op
#############################

# +.-.*,%,/,**

print(7%2) #op is 1 (module)
print(2**3) #op is 8 (exponentional)

#Assignment op
######################

#-=,==,+==,<,>,<=,>=,!=,*=,%=,/=

number=5
print(number==3) #op is False

print(number<10) #op is True
print(number<=5) #op is True
print(number!=20) #op is True
number=5
number=+5 #number=number+5
print(number) #op is 10



