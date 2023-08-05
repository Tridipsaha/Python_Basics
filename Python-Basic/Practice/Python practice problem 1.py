#!/usr/bin/env python
# coding: utf-8

# ### Write a Function to calculate length of a list and sort in in reverse order

# In[39]:


list = [8,2,9,0,3]

def rever(rows):
    rows.sort()
    size=len(rows)
    for i in range(size-1,0,-1):
        print(rows[i],end=" ")
    
rever(list)


# ###Implement QuickSort on List (using fewer lines of code).

# In[ ]:





# # let a list be s = [1, 3, 2, 1, 5, 3, 9] . use min(s) , max(s) ,sum(s) also calculate the average of the list 

# In[32]:


s = [1,3,2,1,5,3,9]
print(min(s))
print(max(s))
print(sum(s))

print("Average of s is= ", sum(s)/len(s))


# # use import random and call random.shuffle(some_list) to shuffle the contents of the list some_list 

# In[36]:


import random
random.shuffle(s)
print(s)


# # print the last 3 elements of a list without using for loops

# In[48]:


lists = [6,3,89,2,5,2,9,4,2,0]

print(lists[len(lists)-3])
print(lists[len(lists)-2])
print(lists[len(lists)-1])


# In[49]:


some_list = [1, 2, 3, 6, 5, 1, 7, 3]

print(some_list[:-1])
print(some_list[-4:-2])
print(some_list[2:-3])


# In[55]:


some_string = "abacdaegakialaop"
print (some_string.split('a'))

