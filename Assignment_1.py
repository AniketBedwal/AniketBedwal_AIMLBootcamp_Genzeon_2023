#!/usr/bin/env python
# coding: utf-8

# In[31]:


#String

str="My name is Aniket"

for i in str:
    print(i)
    
#
print(len(str))
#
print("name" in str)

#
print("name" not in str)

#slicing
print(str[2:15])

print(str[:6])

print(str[4:])

print(str.upper())
print(str.replace("Aniket", "walter white"))
print(str.split(" "))

#formatting
a="     thomas shelby"
print(f"my name  is {a}")

city="buldana"
state="maharashtra"
str1="I am from {0} in {1}"
print(str1.format(city,state))

#multiline string
str3="""aniket
is 
my 
name"""

print(str3)

print(a.lstrip())
print(a.find("om"))


# In[33]:


#List methods

lst = ['mercedes', 'lambo', 'ferrari', 'porshe', 'hummer']
lst.append("maruti")
print(lst)

print(lst.pop())

lst.reverse()

print(lst)

lst.sort()

print(lst)

lst.remove("lambo")
print(lst)

lst.insert(3,"a")
print(lst)


# In[42]:


#Tuple methods

tup1 = ('lily','rose','banana',90,2,2,2)
print(tup1)

print(tup1.count(2))

print(tup1.index(2))


# In[54]:


#Dictionary

dict={
    "name" : "Aniket",
    "company" : "Genzeon",
    "designation" : "Trainee"
}

print(dict)
print(dict["company"])
dict["location"] = "Pune"
print(dict)

dict.update({"designation" : "Lead"})
print(dict)

dict.pop("location")
print(dict)

print(dict.items())
print(dict.values())


# In[59]:


#set

set0={"bmw", "kawasaki", "yamaha", "Royal Enfield", "Honda"}
set1={"Augusta", "Harley Davidson", "yamaha"}
print(set0)

set0.difference(set1)

set0.add("Suzuki")
print(set0)
set0.intersection(set1)



# In[8]:


#conversion decimal > binary > hex >octal

#decimal to binary
a = int(input("enter"))
bin_a=bin(a)
print(bin_a)

#decimal to hex
b = int(input())
hex_b = hex(b)
print(hex_b)

#decimal to octal
c = int(input())
oct_c = oct(c)
print(c)


# In[12]:


#arithemetic operators

a=int(input())
b=int(input())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)




# In[14]:


#Assignment Operators
c=int(input())
d=int(input())
e=c
print(e)
c+=d
print(c)
c-=d
print(c)
c*=d
print(c)
c/=d
print(c)


# In[15]:


#comparison operators
a=int(input())
b=int(input())
print(a==b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a!=b)


# In[27]:


#logical operators
a= 1
b= 0
if a and b:
    print("both are true")
else:
    print("atlest one is false")
    
if a or b:
    print("atlest one is true")
else:
    print("both are false")

#
print(not b)


# In[36]:


#bitwise

a=4
b=15

c= bin(a)
d=bin(b)

e = c & d
print(e)


# In[39]:


#15
print("aniket is my name"[::-1][4::3])


# In[50]:


#16
str = "was it a car or a cat i saw"
str[::-1]
str.upper()


# In[63]:


#matrix
import numpy as np
mat1=([2,4],[5,6])
mat2 = ([30,20],[1,4])
print(np.add(mat1,mat2)) 
print('\n')
print(np.subtract(mat1,mat2))
print('\n')
print(np.divide(mat1,mat2))

print('\n')
print(np.dot(mat1,mat2))


# In[62]:


#
x=int(input())
print(x*"Z" + (x*2)*"O")


# In[64]:


#membership ops
x="hello world"
y={1:'a',2:'b'}
print(y)

print('H' in x)
print(1 in y)
print('a' in y)


# In[65]:


#identity operators
x1=5
y1=5
x2="Hello"
y2="Hello"
x3=[1,2,3]
y3=[1,2,3]
print(x1 is not y1)
print(x2 is y2)
print(x3 is y3)


# In[ ]:




