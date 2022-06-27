#!/usr/bin/env python
# coding: utf-8

# In[2]:


import folium
import pandas as pd


# In[26]:


my_map = folium.Map(
    location = [13.133932434766733, 16.103938729508073],
    zoom_start=2
)
my_map


# In[ ]:





# In[33]:


import csv
new_dict = {"South Korea": 29000, "Recife": 5000, "Miami":50000, "New York":25000, "Brazil":25000,
"Mexico": 12000, "Costa Rica":10000, "Paris":2040, "Japan":50000}
with open('ukraine.csv', 'w', newline='') as csvfile:
    header_key = ['Countries', 'Donations($)']
    new_val = csv.DictWriter(csvfile, fieldnames=header_key)
    
    new_val.writeheader()
    for new_k in new_dict:
        new_val.writerow({'Countries': new_k, 'Donations($)': new_dict[new_k]})
        
        
        
        


# In[34]:


donations = pd.read_csv('ukraine.csv')



# In[35]:


print(donations)


# In[38]:


next_dict = {35.9078: 127.7669, 8.0577: 34.8830, 25.761681:-80.191788, 40.712776:-74.005974, -10.333333:-53.2,
23.6585116: -102.0077097, 10.2735633:-84.0739102, 48.8588897:2.320041, 36.5748441:139.2394179}
with open('area.csv', 'w', newline='') as csvfiled:
    head_key = ['Latitute', 'Longitute']
    next_val = csv.DictWriter(csvfiled, fieldnames=head_key)
    
    next_val.writeheader()
    for next_k in next_dict:
        next_val.writerow({'Latitute': next_k, 'Longitute': next_dict[next_k]})
        
        
areas = pd.read_csv('area.csv')
print(areas)


# In[83]:


my_map = folium.Map(
    location = [13.133932434766733, 16.103938729508073],
    zoom_start=2
)

for _, places in areas.iterrows():
    folium.Marker(
        location=[places['Latitute'], places['Longitute']],
        popup = donations[['Countries', 'Donations($)']],
        tooltip=donations[['Countries', 'Donations($)']],
    ).add_to(my_map)
    
my_map


# In[86]:


def donations_range(row):
    if row['Donations($)'] >= 50000:
        return 'green'
    elif row['Donations($)'] < 50000:
        return 'red'
    return 'blue'

donations['color'] = donations.apply(donations_range, axis=1)


# In[98]:


my_map = folium.Map(
    location = [13.133932434766733, 16.103938729508073],
    zoom_start=2
)

    
for _, places in areas.iterrows():
    folium.Marker(
        location=[places['Latitute'], places['Longitute']],
        popup = donations[['Countries', 'Donations($)']],
        tooltip=donations[['Countries', 'Donations($)']],
        icon=folium.Icon(color=donation['color'])
    ).add_to(my_map)
    
my_map


# In[100]:


my_map.save('donations_map.html')






