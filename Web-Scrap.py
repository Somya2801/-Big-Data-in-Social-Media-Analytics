#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests
from bs4 import BeautifulSoup


# In[3]:


import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

urls = [
    "https://drive.google.com/file/d/1mHjxHZB4ETsFmLBd89TNXfGmslrl6Xsz/view?ts=660fe691"
]

def scrape_url(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    return soup.get_text()

with ThreadPoolExecutor(max_workers=5) as executor: # Adjust max_workers as needed
    results = list(executor.map(scrape_url, urls))

for result in results:
    print(result)


# In[ ]:




