#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('hello')


# In[3]:


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


# In[23]:


#table using nested for

for var in range(1,11):
    var=var
    print("\n")
    for i in range(1,11):
        
        v=i*var
        print(f"{var} * {i} = {v}")


# In[26]:


var=10
while var>0:
    print(var)
    var =var-2
    if(var==4):
        break


# In[ ]:




