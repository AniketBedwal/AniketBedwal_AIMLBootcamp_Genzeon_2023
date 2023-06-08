#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Functions
#User defined function

def greet(name):
    '''this is a function to greet a person'''
    print("Hello \t" +name+" Good Afternoon")
        

greet("aniket")


# In[4]:


#default

def A(a,b=1,c=2):
    return a+b+c


print(A(3))
print(A(4,4,4))
print(A(2,2))


# In[5]:


#Keyword

def A(a,b=1,c=3):
    return a+b+c

print(A(a=2,b=3))
print(A(c=3,b=2,a=10))


# In[6]:


#Positional

def add(a,b,c):
    return a+b+c
print(add(10,20,30))


# In[7]:


#arbitary Keyword
def key_arg(**kwargs):
    return kwargs
my_dic = key_arg(Apple=10,banana=20,chiku=30)
print(my_dic["Apple"])
print(my_dic)


# In[8]:


#aribitary posiitonal

def add_num(*n):
    print(n)
    print(sum(n))
    
add_num(1,2,3,4,5)


# In[10]:


#higher order function

def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()
def explain(func):
    greet=func("Hi I am higher order FuNcTion")
    print(greet)
    
explain(shout)
explain(whisper)


# In[14]:


#lambda function

def inc(x):
    x=x+10
    return x

print(inc(4))

#
print((lambda x:x+10)(4))
#
res = lambda x:x+1
print(res(3))

#
print((lambda x,y:x**y)(2,2))


# In[17]:


li=[1,2,3,4,5]
def inc(num):
    return num+2
ref_list=list(map(inc,li))
print(ref_list)
#print using lambda
print("using lambda")
print(list(map(lambda x:x+2,li)))


# In[22]:


def eor(n):
    if n%2==0:
        print("number {} is even".format(n))
    else:
        print("numer {} is odd".format(n))
        
li=[1,2,3,4,5]
list(map(eor,li))


# In[25]:


#filter
def odd_num(n):
    if n%2!=0:
        return n
lis=[3,5,2,6,5,1,7]
print(list(filter(odd_num,lis)))
    
li=[5,6,43,23,10,50]
temp=list(filter(lambda x:x%2==0,li))
print(temp)


# In[26]:


#modules

import os
os.mkdir("newf")
os.chdir("newf")
os.getcwd()
os.listdir()


# In[27]:


rmdir("newf")


# In[29]:


import sys
print(sys.path)
print(sys.version)
print(sys.maxsize)


# In[31]:


import statistics as st
print(st.mean([10,2,30,50,70]))
print(st.mode([10,2,30,50,70]))
print(st.median([10,2,30,50,70]))


# In[33]:


import random as r 
print(r.randrange(1,20))
print(r.randint(1,100))
print(r.random())


# In[34]:


#class and object

class CO:
    def addn(self,a,b):
        return a+b
    def subn(self,a,b):
        return a-b
    
obj=CO()
print("addition of two number is",obj.addn(5,5))
print("sub of two number is",obj.subn(5,4))


# In[ ]:


#inheritance

#single inheritance
class Animal:
    def animal_sounds(self):
        return "makes sound"
class Cat(Animal):
    def cat_sound(self):
        return self.animal_sounds()+"meoww"
    def __str__(self)


# In[35]:


print(d)


# In[36]:


#exception handeling

try:
    print(d)
except NameError as ne:
    print("exception occurred",ne)


# In[39]:


#File handeling 
f=open("sample1.txt","x")


# In[40]:


import os
os.remove("sample1.txt")


# In[41]:


f=open("file1.txt","x")


# In[42]:


import os
os.remove("file1.txt")


# In[43]:


f=open("file.txt",'x')


# In[44]:


f1=open("file1.txt",'x')


# In[45]:


f1=open("f1.txt",'x')


# In[46]:


f2=open("f2.txt",'x')


# In[47]:


#Pickle

import pickle
myl=['a','b','c','d','e']
f3=open("f4.txt","wb")
pickle.dump(myl,f3)
f3.close()


# In[49]:


print(f3)


# In[ ]:




