#!/usr/bin/env python
# coding: utf-8

# In[13]:


lst = ['mercedes', 'lambo', 'ferrari', 'porshe', 'hummer']
print(lst)
lst.reverse()
print(lst)

lst.insert(2,'pagani')
print(lst)
lst[4] = 'fortuner'
print(lst)

lst[1:4]=['bently']
print(lst)
lst[1:] = ['maruti']
print(lst)


# In[23]:


#tupple
tup0=(1,2,3,4)
tup1=('hi',1.3,2)
tup2=("hello",tup0,tup1)

#indexing
print(tup2[2][0])
print(tup2[-1][2])

#slicing
print(tup2[0][0:2])

#tupple methods
print(max(tup0))


# In[29]:


#sets
s1={1,2,3,4,5}
s3={4,6,7}
s2={1,2,3,'hi',(1,2,3)}
lst = [12,23,4,3]
s3= set(lst)
print(s3)
s1.add(45)
print(s1)

##
print(s1.union(s2))


# In[30]:


#dictionary
dic={'name':'aniket'
    ,'phone':'4309430943',
    'add':'pune'}
print(dic)


# In[36]:


#string formats

name='genzeon'
language='python'
c='trainee'

print(c,"are learning", language,"programming at", name)

#format
print("{} are learning {} programming at {}".format(c,language,name))
print("{1} are learning {0} programming at {2}".format(c,language,name))
print("{a} are learning {b} programming at {d}".format(a=c,b=language,d=name))

#rawstring
print(f"{c} are learning {language} at {name}")


# In[37]:


#decision making in python

#if statement
var=20
if var>0:
    print('true')
    print(var)


# In[ ]:


#if else

var1=2
if var>1:
    print('true')
else:
    print("false")


# In[ ]:


age=10
if age<0:
if age<5:
    print("free")
elif age>5 and age<=10:
    print("half ticket")
elif age>10 and age<=60:
    print("full ticket")
else:
    print("30% off")


# In[ ]:




