#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('mamba install bs4==4.10.0 -y')
get_ipython().system('pip install lxml==4.6.4')
get_ipython().system('mamba install html5lib==1.1 -y')
# !pip install requests==2.26.0


# In[ ]:





# In[2]:


from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page


# In[3]:


get_ipython().run_cell_magic('html', '', "<!DOCTYPE html>\n<html>\n<head>\n<title>Page Title</title>\n</head>\n<body>\n<h3><b id='boldest'>Lebron James</b></h3>\n<p> Salary: $ 92,000,000 </p>\n<h3> Stephen Curry</h3>\n<p> Salary: $85,000, 000 </p>\n<h3> Kevin Durant </h3>\n<p> Salary: $73,200, 000</p>\n</body>\n</html>")


# In[4]:


html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"


# In[5]:


soup = BeautifulSoup(html, "html.parser")


# In[6]:


print(soup.prettify())


# In[7]:


tag_object=soup.title
print("tag object:",tag_object)


# In[8]:


print("tag object type:",type(tag_object))


# In[9]:


tag_object=soup.h3
tag_object


# In[10]:


tag_child =tag_object.b
tag_child


# In[11]:


parent_tag=tag_child.parent
parent_tag


# In[12]:


tag_object


# In[13]:


tag_object.parent


# In[14]:


sibling_1=tag_object.next_sibling
sibling_1


# In[15]:


sibling_2=sibling_1.next_sibling
sibling_2


# In[16]:


sibling_2.next_sibling


# In[17]:


tag_child['id']


# In[18]:


tag_child.attrs


# In[19]:


tag_child.get('id')


# In[20]:


tag_string=tag_child.string
tag_string


# In[21]:


type(tag_string)


# In[22]:


unicode_string = str(tag_string)
unicode_string


# In[23]:


get_ipython().run_cell_magic('html', '', "<table>\n  <tr>\n    <td id='flight' >Flight No</td>\n    <td>Launch site</td> \n    <td>Payload mass</td>\n   </tr>\n  <tr> \n    <td>1</td>\n    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td>\n    <td>300 kg</td>\n  </tr>\n  <tr>\n    <td>2</td>\n    <td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td>\n    <td>94 kg</td>\n  </tr>\n  <tr>\n    <td>3</td>\n    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td>\n    <td>80 kg</td>\n  </tr>\n</table>")


# In[24]:


table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"


# In[25]:


table_bs = BeautifulSoup(table, "html.parser")


# In[26]:


table_rows=table_bs.find_all('tr')
table_rows


# In[27]:


first_row =table_rows[0]
first_row


# In[28]:


print(type(first_row))


# In[29]:


first_row.td


# In[30]:


for i,row in enumerate(table_rows):
    print("row",i,"is",row)
    


# In[31]:


for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('colunm',j,"cell",cell)


# In[32]:


list_input=table_bs .find_all(name=["tr", "td"])
list_input


# In[33]:


table_bs.find_all(id="flight")


# In[34]:


list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
list_input


# In[35]:


table_bs.find_all(href=True)


# In[36]:


table_bs.find_all(href=False)


# In[37]:


soup.find_all(id="boldest")


# In[38]:


table_bs.find_all(string="Florida")


# In[39]:


table_bs.find_all(string="Florida")


# In[40]:


get_ipython().run_cell_magic('html', '', "<h3>Rocket Launch </h3>\n\n<p>\n<table class='rocket'>\n  <tr>\n    <td>Flight No</td>\n    <td>Launch site</td> \n    <td>Payload mass</td>\n  </tr>\n  <tr>\n    <td>1</td>\n    <td>Florida</td>\n    <td>300 kg</td>\n  </tr>\n  <tr>\n    <td>2</td>\n    <td>Texas</td>\n    <td>94 kg</td>\n  </tr>\n  <tr>\n    <td>3</td>\n    <td>Florida </td>\n    <td>80 kg</td>\n  </tr>\n</table>\n</p>\n<p>\n\n<h3>Pizza Party  </h3>\n  \n    \n<table class='pizza'>\n  <tr>\n    <td>Pizza Place</td>\n    <td>Orders</td> \n    <td>Slices </td>\n   </tr>\n  <tr>\n    <td>Domino's Pizza</td>\n    <td>10</td>\n    <td>100</td>\n  </tr>\n  <tr>\n    <td>Little Caesars</td>\n    <td>12</td>\n    <td >144 </td>\n  </tr>\n  <tr>\n    <td>Papa John's </td>\n    <td>15 </td>\n    <td>165</td>\n  </tr>\n      ")


# In[41]:


two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"


# In[42]:


two_tables_bs= BeautifulSoup(two_tables, 'html.parser')


# In[43]:


two_tables_bs.find("table")


# In[44]:


two_tables_bs.find("table",class_='pizza')


# In[45]:


url = "http://www.ibm.com"


# In[46]:


data  = requests.get(url).text 


# In[47]:


soup = BeautifulSoup(data,"html.parser")


# In[48]:


for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>

    print(link.get('href'))


# In[49]:


for link in soup.find_all('img'):# in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))


# In[50]:


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"


# In[51]:


data  = requests.get(url).text


# In[52]:


soup = BeautifulSoup(data,"html.parser")


# In[53]:


table = soup.find('table')


# In[54]:


for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].string # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))


# In[55]:


import pandas as pd


# In[56]:


url = "https://en.wikipedia.org/wiki/World_population"


# In[57]:


data  = requests.get(url).text


# In[58]:


soup = BeautifulSoup(data,"html.parser")


# In[59]:


tables = soup.find_all('table')


# In[60]:


len(tables)


# In[61]:


for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)


# In[62]:


print(tables[table_index].prettify())


# In[63]:


population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])

for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)

population_data


# In[64]:


pd.read_html(str(tables[5]), flavor='bs4')


# In[65]:


population_data_read_html = pd.read_html(str(tables[5]), flavor='bs4')[0]

population_data_read_html


# In[66]:


dataframe_list = pd.read_html(url, flavor='bs4')


# In[67]:


len(dataframe_list)


# In[68]:


dataframe_list[5]


# In[69]:


pd.read_html(url, match="10 most densely populated countries", flavor='bs4')[0]


# In[70]:


import piplite
await piplite.install(['seaborn', 'lxml', 'openpyxl'])

import pandas as pd


# In[ ]:




