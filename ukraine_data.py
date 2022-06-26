#!/usr/bin/env python
# coding: utf-8

# In[58]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as tick


# In[5]:


ukraine_data = {'Refugee_Arrivals_from_Ukraine': 8000000,
                'Internally_Displaced_People': 7100000,
                'Civilian_Casualties_Killed': 4634,
                'Civilian_Casualties_Injured':5769,
                'People_reached_within_Ukraine':8800000,
                'Attacks_on_Health_Care': 316,
                'Attacks_on_Education_Facilities': 1888
}
group_data = list(ukraine_data.values())
group_names = list(ukraine_data.keys())
group_mean = np.mean(group_data)


# In[ ]:





# In[114]:


plt.rcParams.update({'figure.autolayout': True})

def quantity(x, pos):
    if x >= 1e6:
        s = '{:1.1f}M'.format(x*1e-6)
    else:
        s = '{:1.0f}K'.format(x*1e-3)
    return s

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')

ax.axvline(group_mean, ls='-', color='y')

for group in [3, 5, 8]:
    ax.text(545000, group, "lowest areas", fontsize=10, verticalalignment='center')


ax.set(xlim=[-100000, 9000000], xlabel='Quantity', ylabel='Areas', title='Ukraine Data')
ax.xaxis.set_major_formatter(tick.FuncFormatter(quantity))
#The graph below shows the specific topics with a quantities of ukraines involved.


# plt.style.use('seaborn')

# In[71]:


fig.savefig('ukraine_data.pdf', transparent=True, dpi=80, bbox_inches='tight')


# In[88]:


names = ['first donations', 'second donations,', 'third donations', 'fourth donations', 'fith donations']
values = [5089, 12565, 45564, 80099, 160090]

plt.figure(figsize=(25, 4))
plt.subplot(132)
plt.bar(names, values)
plt.title('Incrementing of Donations')
plt.show()
#This graph shows the increment of donations cycle.


# In[106]:


np.random.seed(19680)
fig, ax = plt.subplots()
ax.plot(10000*np.random.rand(20))
def q(x, pos):
    if x >= 1e6:
        s = '{:1.1f}M'.format(x*1e-6)
    else:
        s = '{:1.0f}K'.format(x*1e-3)
    return s
ax.yaxis.set_major_formatter(tick.FuncFormatter(q))

# plt.annotate('max donations', xy=(2,1), xytext=(3, 2.5),
#             arrowprops=dict(facecolor='black', shrink=0.05),)

ax.yaxis.set_tick_params(which='major', labelcolor='green', labelleft=False, labelright=True)
plt.show()


# In[107]:


# In the graph above we can determine the results of the donation measures in days. hours format.
# In 17 days and 5 hours, our team managed to raise 72,000 thousand dollars in donations.
# In the 12 days, we collect 10,000 in donations as the maximum donation in one day


# In[113]:


df = pd.DataFrame(
{
    'Name': [
        'Leonel Cartwright', 'Nicholas Konopelski', 'Willy Wolff II', 
        'Miss Cortez Bernhard', 'Jace Sporer', 'Brooklyn Greenfelder', 'Ethelyn Hand',
        'Roslyn Weber','Fern Wintheiser', 'Luna Schaefer', 'Sofia Holynska', 'Amina Shella'
    ],
    'Age': [52 , 7, 70, 20, 9, 5 , 11, 29, 88, 14, 3, 4],
    'Sex': ['M', 'M', 'M', 'F', 'M', 'F', 'F', 'F', 'M', 'F','F','F'],
    'Weight': [193, 69, 211, 158, 49, 59, 67, 148, 149, 110, 50, 45,]
})


print(df)


# In[ ]:


# In the previous dataframe,
# we can observe,
#the first missing people we save by connecting our programmers with the-
#knowledge into an informative page with donation and reporting actions for ukrainians.
