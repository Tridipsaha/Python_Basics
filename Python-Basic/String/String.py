#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = 'You can write here any thing' #in python charaters are not exist

print(a)


# In[13]:


a ='g'
ord(a)# it gives the ASCII value of the character 

chr(103)# it gives the character of that the value

print(ord('4'))


# In[ ]:





# In[16]:


a=4
b=3
print(str(a),str(b))#convert it into string

firstname='Tridip'
lastname='Saha'
print(f"{lastname},{firstname}")#format my our own way


a = "             this is use to remove space.        "
print(a.strip())#remove the extra space


# In[18]:


a = input()# use for taking input
print(a)


# In[19]:


a = "5 8 2 0 64 53"
a.split(" ")# it breakes whever it match with parameter that you have pass


# In[21]:


a = "Tridip"
a.replace('Tr', 's') #it replace the string with the right one's


# In[22]:


a.count('i') # count how many times it repeat the character

