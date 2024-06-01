#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install SpeechRecognition')


# In[2]:


import speech_recognition as sr
#Initiаlize  reсоgnizer  сlаss  (fоr  reсоgnizing  the  sрeeсh)
r = sr.Recognizer()
# Reading Audio file as source
#  listening  the  аudiо  file  аnd  stоre  in  аudiо_text  vаriаble
with sr.AudioFile('/Users/shubhangisingh/Downloads/Brand Metrics Part 1.wav') as source:
    audio_text = r.listen(source,phrase_time_limit=100)
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        # using google speech recognition
        text = r.recognize_google(audio_text)
        print('Converting audio transcripts into text ...')
        print(text)
    except:
         print('Sorry.. run again...')


# In[ ]:




