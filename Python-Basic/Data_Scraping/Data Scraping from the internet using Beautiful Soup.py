#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install bs4')


# # Fetching the HTML body of a web page

# In[75]:


from urllib.request import urlopen 
url_detail = "https://en.wikipedia.org/wiki/Android_version_history"

url_data = urlopen(url_detail)#getting the HTTP request
print(url_data)

html_body = url_data.read()# html body of that url link
print(html_body)


# # Parsing the data

# In[91]:


from bs4 import BeautifulSoup as soup# beautiful is a class
html_soup = soup(html_body, 'html.parser') # give you the html body in a well manner
#print(html_soup)
select_tables = html_soup.find('table', { "class":"wikitable"})
tables = select_tables.findAll('tr')


header = tables[0]
colum_title = header.findAll('th')
colum_title_text =[i.text[:-1] for i in colum_title]
print(colum_title_text)


# # Showing how to get the column details

# In[98]:


row = tables[1]
row_select = row.findAll('td')
for i in row_select:
    print(i.text)


# # All rows get collected

# In[119]:


row = tables[1:]
for i in row:
    print("-------------------------------------------")
    row_select = i.findAll('td')
    #for j in row_select:
    print(row_select[0].text,row_select[1].text)


# # Writing & Reading CSV files

# In[112]:


filename = 'Android_version.csv'
with open(filename, 'w', encoding = 'utf') as f:
    #write the header
    header_string = ','.join(colum_title_text)
    header_string+= '\n'
    f.write(header_string)
    
    for i in row:
        #print(j.text)
        row_select = i.findAll('td')
        for j in row_select:
            row_string = ''
            row_string = ''.join(j.text)
            row_string+= '\n'
            f.write(row_string)


# In[ ]:




