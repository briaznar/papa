
# coding: utf-8

# # It's possible to read Simple English Wikipedia in 30 days time

# Avarage reading speed is 180 Words per minute (in a monitor)
# source: https://en.wikipedia.org/wiki/Words_per_minute#Reading_and_comprehension
# Speed readers can read about 700 words per minute
# source: https://en.wikipedia.org/wiki/Speed_reading
# 
# Given this: Count the total number of words in Simple English Wikipedia and calculate how long it will take for each to finish reading it.
# 
# Since the initial observation states that Simple English Wikipedia articles are short, counting this words, and taking this speeds into consideration we calculated that 30 days is a plausible time for doing this task.

# In[43]:

import os
import re
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


# In[8]:

def get_total_words():
    total_words = 0
    with open("simple-20160801-1-article-per-line\simple_english_wikipedia.txt", encoding="utf8") as file:
        for line in file:
            total_words += len(re.findall(r'\w+', line))
    return total_words


# In[9]:

def get_avg_time(words):
    avg_speed = 180
    return ((words/avg_speed)/60)/24
    
    


# In[10]:

def get_speedy_time(words):
    speedy_speed = 700
    return ((words/speedy_speed)/60)/24
    


# In[11]:

def get_wpm(words):
    time = 43200 #30 days in minutes
    return (words/time)


# In[12]:

words       = get_total_words()
avg_time    = get_avg_time(words)
speedy_time = get_speedy_time(words)

print("Total number of words: ", words)
print("Total time (in days) for an average reader: ", round(avg_time,2))
print("Total time (in days) for a speed reader: ", round(speedy_time,2))


# It is not possible to read simple english wikipedia within 30 days (for a normal reader)
# However it is possible to do it for a speed reader.

# In[14]:

wpm = get_wpm(words)
print("In order to be able to read single english wikipedia within 30 days, a person should read at least", round(wpm,2), "words per minute")


# In[54]:

y = [round(avg_time, 2),round(speedy_time,2)]
x = len([round(avg_time, 2),round(speedy_time,2)])
width = 1/1.5
plt.bar(1, round(avg_time, 2), width, color="blue")
plt.bar(2, round(speedy_time,2), width, color="red")
plt.ylabel('Time in days')
plt.xlabel('Readers')


avg_reader = mpatches.Patch(color='blue', label='Averge reader')
speedy_reader = mpatches.Patch(color='red', label='Speed reader')

plt.legend(handles=[avg_reader, speedy_reader],loc=5)
plt.show()


