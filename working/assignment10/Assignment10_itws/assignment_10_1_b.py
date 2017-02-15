
# coding: utf-8

# In[54]:

import numpy as np
import pandas as pd
from collections import Counter
import math
import matplotlib.pyplot as plt


# In[55]:

data = pd.read_table('onlyhash.data',names=["user_name","date","hashtag"])


# In[57]:

data["hashtag_list"] = data.hashtag.apply(lambda x: x.split(" "))


# In[58]:

users = data.user_name.unique()
index = [i for i in range(1, len(users)+1)]

dates = data.date.unique()
index2 = [i for i in range(1, len(dates)+1)]


# In[59]:

df = pd.DataFrame(users, index=index, columns=['user_name'])


# In[60]:

def get_hash(user_name, dataframe):
    dataframe = dataframe[dataframe["user_name"] == user_name]
    hashtag_list = dataframe["hashtag_list"].values
    hashtag_list = [value for sublist in hashtag_list for value in sublist]
    return hashtag_list


# In[ ]:

df["hashtags"] = df.user_name.apply(lambda x: get_hash(x, data))


# In[ ]:

def entropy(counter_list):
    c = Counter(counter_list)
    ent = 0.0
    for k,v in c.items():
        prob = float(v)/len(counter_list)
        ent = ent - prob * math.log2(p)
    return ent


# In[ ]:

df["user_entropy"] = df.hashtags.apply(lambda x: entropy(x))


# In[ ]:

data["entropy"] = data.hashtag_list.apply(lambda x: entropy(x))


# In[ ]:

grp = data.groupby(["date"]).entropy.mean()
user_entropy_by_day = grp.to_frame()


# In[ ]:

df2 = pd.DataFrame(dates, index=index2, columns=['date'])


# In[ ]:

def get_hash_date(date, dataframe):
    dataframe = dataframe[dataframe["date"] == date]
    hashtag_list = dataframe["hashtag_list"].values
    list_hash = [val for sublist in hashtag_list for val in sublist]
    return list_hash


# In[ ]:

df2["hashtags"] = df2.date.apply(lambda x: get_hash_date(x, data))


# In[ ]:

df2["sys_entropy"] = df2.hashtags.apply(lambda x: entropy(x))


# In[ ]:

user_entropy_by_day['date'] = user_entropy_by_day.index


# In[ ]:

sorted = entropy_df.sort_values(by="sys_entropy")


# In[ ]:

import matplotlib.pyplot as plt
length=len(ranked)
x = [x for x in range(0,length)]
plt.title("System Entropy(sorted) and user Entropy (Average) per day")
plt.xticks(np.arange(0,max(x),40))
plt.yticks(range(0,int(max(ranked.sys_entropy)+2)))
plt.xlabel("Days Rank")
plt.ylabel("Entropy")
plt.scatter(x,ranked.entropy.values,label='User Entropy',color="g")
plt.scatter(x,ranked.sys_entropy.values,label='System Entropy',color="b")
plt.show()

