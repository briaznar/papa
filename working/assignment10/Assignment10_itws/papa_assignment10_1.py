import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter


def get_hash(user_name, dataframe):
    dataframe = dataframe[dataframe["user_name"] == user_name]
    hashtag_list = dataframe["hashtag_list"].values
    hashtag_list = [value for sublist in hashtag_list for value in sublist]
    return hashtag_list

def entropy(counter_list):
    c = Counter(counter_list)
    ent = 0.0
    for k,v in c.items():
        prob = float(v)/len(counter_list)
        ent = ent - prob * math.log2(prob)
    return ent

def get_hash_date(date, dataframe):
    dataframe = dataframe[dataframe["date"] == date]
    hashtag_list = dataframe["hashtag_list"].values
    list_hash = [val for sublist in hashtag_list for val in sublist]
    return list_hash

def plotting(sorted):
    length=len(sorted)
    x = [x for x in range(0,length)]
    plt.title("System Entropy(sorted) and user Entropy (Average) per day")
    plt.xticks(np.arange(0,max(x),40))
    plt.yticks(range(0,int(max(sorted.sys_entropy)+2)))
    plt.xlabel("Days Rank")
    plt.ylabel("Entropy")
    plt.scatter(x,sorted.entropy.values,label='User Entropy',color="g")
    plt.scatter(x,sorted.sys_entropy.values,label='System Entropy',color="y")
    plt.show()

def main():

    data = pd.read_table('onlyhash.data',names=["user_name","date","hashtag"])
    data["hashtag_list"] = data.hashtag.apply(lambda x: x.split(" "))

    users = data.user_name.unique()
    index = [i for i in range(1, len(users)+1)]

    dates = data.date.unique()
    index2 = [i for i in range(1, len(dates)+1)]

    df = pd.DataFrame(users, index=index, columns=['user'])
    df["hashtags"] = df.user.apply(lambda x: get_hash(x, data))
    df["user_entropy"] = df.hashtags.apply(lambda x: entropy(x))

    data["entropy"] = data.hashtag_list.apply(lambda x: entropy(x))

    grp = data.groupby(["date"]).entropy.mean()
    user_entropy_by_day = grp.to_frame()

    df2 = pd.DataFrame(dates, index=index2, columns=['date'])
    df2["hashtags"] = df2.date.apply(lambda x: get_hash_date(x, data))
    df2["sys_entropy"] = df2.hashtags.apply(lambda x: entropy(x))

    user_entropy_by_day['date'] = user_entropy_by_day.index

    entropy_df = pd.merge(df2, user_entropy_by_day, on='date', how='outer')

    sorted = entropy_df.sort_values(by="sys_entropy")
    plotting(sorted)

if __name__ == "__main__":
    main()

