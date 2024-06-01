#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install pandas praw')


# In[4]:


import pandas as pd
import praw


# In[15]:


user_agent = "Scraper 1.0 by /u/python_engineer"
reddit = praw.Reddit (
client_id="aR4OHWCpuNHfk29il4qXxw",
client_secret="Pitk53AETqnkEzXLN0ysohjvdUcbTw",
user_agent=user_agent
)


# In[80]:


headlines = set ( )
for submission in reddit.subreddit('SocialMediaMarketing').hot(limit=None):
    headlines.add(submission.title)
print(len(headlines))


# In[81]:


print (submission.title)
print (submission.id)
print (submission.author)
print (submission.score)
print (submission.upvote_ratio)
print (submission.url)


# In[82]:


df = pd.DataFrame(list(headlines), columns=["Reddit"])
df


# In[83]:


text = " ".join(review for review in df.Reddit)
print ("There are {} words in the combination of all review.".format(len(text)))
text


# In[85]:


import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[86]:


# Create stopword list:
stopwords = set(STOPWORDS)


# In[87]:


# Generate a word cloud image
wordcloud = WordCloud(stopwords=stopwords).generate(text)

# Display the generated image:
# the matplotlib way:
plt.figure( figsize=(10,10) )
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


# In[ ]:




