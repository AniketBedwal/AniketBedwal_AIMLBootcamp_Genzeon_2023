#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Q.6

 

statelist=["Delhi","Bihar","UP","Goa","Gujarat","Assam","AP"]
str=""
for item in statelist:
    a=item[len(item)-2]
    if(a=='a'or a=='e'or a=='i'or a=='o' or a=='u'or a=='A'or a=='E'or a=='I'or a=='O' or a=='U'):
           str+=a.upper()
print(str[::-1])    


# In[ ]:


#4
#approach 1

import math
statelist=["Delhi","Bihar","Goa","Gujarat","Assam"]

for i in statelist:
    keng = (math.floor(len(i)/2))
    char = i[keng]
    #print(char)
    if char in ['a','e','i','o','u']:
        print(char,end="")
  


# In[ ]:


#5
#approach 1

statelist=["Delhi","Bihar","UP","Goa","Gujarat","Assam","AP"]
list=[]
for i in statelist:
    char = i[1]
    if char in ['a','e','i','o','u']:
        list.append(char)
        
list.sort()
list.reverse()
print(list)




# In[ ]:


#question 3(1)

statelist=["Delhi","Telangana","Goa","AP","Kerala"]
for i in statelist:

    for j in i:

        print(i[0].lower()+i[-1].upper(),end="")

        break



# In[ ]:


#question 3(2)

statelist=["Delhi","Telangana","Goa","AP","Kerala"]

output_string = ''.join([state[0].lower() + state[-1].upper() for state in statelist])

print(output_string)


# In[ ]:


#Q.2 using function and without using fucntion

def replace_spaces_with_hyphens(input_string):
    output_string = input_string.replace(" ", "-")
    return output_string

# Example usage
input_string = "This program converts spaces into hyphen"
output_string = replace_spaces_with_hyphens(input_string)
print(output_string)
# without function
output_string2=""
for iter in input_string:
    if iter==" ":
        output_string2+="-"
    else:
        output_string2+=iter

print(output_string2)


# In[ ]:


#Q.8 --------

from functools import reduce
import operator

#input_list = [25, 12, 33, 12, 8, 10]
input_list = input("Enter numbers, separated by spaces: ").split()

# Convert the input elements to integers
input_list = [int(element) for element in input_list]
result = reduce(operator.add, input_list)

print(result)


# In[ ]:


#Q.7 approach(1)



#without using filter()
countries = ["Finland", "Germany", "Sweden", "Ireland", "Turkey"]
filtered_countries = []

for country in countries:
    if "and" in country:
        filtered_countries.append(country)
        print(filtered_countries)


# In[ ]:


#7 approach(2)
countries = ["Finland", "Germany", "Sweden", "Ireland", "Turkey"]

filtered_countries = list(filter(lambda country: "and" in country, countries))
print(filtered_countries)


# In[ ]:


#Q.1
a= list(input("Enter a sentence").split(","))
st=set(a)
li=list(st)
li.sort()
print(li)


# In[ ]:


#Q8.
import functools
Input=[25,12,33,12,8,10]

 

print(functools.reduce(lambda a,b:a+b,Input))


# In[ ]:


#Q10
num=int(input("Enter a number"))
temp=num
count=0
while(temp>0):
    temp=int(temp/10)
    count+=1
with open("countdigit8.txt","w") as f:   
    f.write(str(count))


# In[ ]:


#Q10.

def count_digits(number):

    count = len(str(number))

    with open("countdigit10.txt", "w") as file:

        file.write(str(count))

    return count

 

number = 12345

digit_count = count_digits(number)

print("Number of digits:", digit_count)


# In[ ]:


#Question 7 : 

Countries=['Finland','Germany','Swedan','Ireland', 'Turkey']

 

def func(country):

  return "and" in country

 

ans=list(filter(func, Countries))

print(ans)


# In[ ]:


#11

def calculate_sum(n):
    return (n * (n + 1)) // 2  # Sum of natural numbers formula

# Write the number to a file
def write_number_to_file(number, filename):
    with open(filename, 'w') as file:
        file.write(str(number))

# Read the number from the file, calculate the sum, and write it to another file
def calculate_sum_and_write_to_file(input_file, output_file):
    with open(input_file, 'r') as file:
        number = int(file.read())

    result = calculate_sum(number)

    with open(output_file, 'w') as file:
        file.write(str(result))

# Usage example
input_file = 'input.txt'
output_file = 'output.txt'
number = int(input())

write_number_to_file(number, input_file)
calculate_sum_and_write_to_file(input_file, output_file)


# In[ ]:


#Q.11


num=int(input("enter a number"))
summ=int((num*(num+1))/2)
with open("sumresult.txt","w") as f:
    f.write(str(summ))   


# In[ ]:


#12

lit=["a",'b','c']
lst=[]
for i in lit:
    lst.append(i.capitalize())
    
f1=open("listupper.txt","w")
f1.write(str(lst))
f1.close()


# In[ ]:


#12 (2) using func

ls=[]
def caps(list1):
    for i in list1:
        ls.append(i.capitalize())   

lis=["abc","fd","sdf"]
caps(lis)
        
f1=open("listupper.txt","w")
f1.write(str(ls))
f1.close( )


# In[ ]:


#13(1)

#func to reverse a string

def rev(file1, str):
    f1 = open("file1.txt","w")
    f2 = open("file2.txt", "w")
    f1.write(str)
    f1 = open("file1.txt","r")
    str1=f1.read()
    f2.write(str1[::-1])
    f1.close()
    f2.close()
    

rev("stringinput.txt","aniket")


# In[ ]:


#Question 14: 

Countries=['Finland','Germany','Swedan','Ireland', 'Turkey']
def func(country):
  return "and" in country


ans=list(filter(func, Countries))
print(ans)


# In[ ]:


#Q15.
num=str(input("enter 3 numbers with space separation"))
with open("input.txt","w") as f:
    f.write(str(num))
with open("input.txt","r") as f:
    temp=f.read()
temp=temp.split(" ")
for x in temp:
    max1=0
    if int(x) > max1:
        max1=x
with open("largest.txt","w") as f:
    f.write(max1)
        
    
    
    


# In[4]:


#9
class InvalidProductBillException(Exception):
    pass 
with open("Bill.txt","w") as f:
    pass
with open("Bill.txt" , "r") as f: 
    ans = f.read() 
try:
    if(ans < '0'): 
        raise InvalidProductBillException 
    else: 
        print("You need to pay amount",ans)
except InvalidProductBillException as ie: 
    print("Exception Occured", ie)
f.close()

