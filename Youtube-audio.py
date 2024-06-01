#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install youtube_search')
get_ipython().system('pip install pytube')


# In[10]:


from youtube_search import YoutubeSearch
from pytube import YouTube
from flask import send_file
import zipfile
import os


def searchtube(artist, songNumber):
    results = YoutubeSearch(artist, max_results=songNumber).to_dict()
    s = 'www.youtube.com'
    urls = []
    for value in results:
        urls.append(s+value['url_suffix'])

    for url in urls:
        audio = YouTube(url)
        audio.streams.filter(only_audio=True).first().download(
            output_path='/Users/shubhangisingh/Downloads/audio')

    handle = zipfile.ZipFile('audios.zip', 'w')


# In[13]:


searchtube('ted talks on big data in social media analytics',20)


# In[ ]:




