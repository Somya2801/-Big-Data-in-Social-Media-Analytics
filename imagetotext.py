#!/usr/bin/env python
# coding: utf-8

# In[16]:


get_ipython().system('pip install google_images_search')
get_ipython().system('pip install pandas')
get_ipython().system('pip install pytesseract')


# In[19]:


from google_images_search import GoogleImagesSearch
import os

# Initialize Google Images Search
gis = GoogleImagesSearch('AIzaSyCnRlPZP2BOdx_I7Leo1-Ynu3WLxh3SnwY', '52118a8712ab04ff8', validate_images=True)

# Function to search and download images
def search(keyword, imageNumber):
    _search_params = {
        'q': keyword,
        'num': imageNumber,
    }

    # Specify directory to save images
    image_dir = 'C:\\Users\\varch\\Downloads\\Imagesforproject'

    # Create directory if it doesn't exist
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    # Search for images and save to specified directory
    gis.search(search_params=_search_params, path_to_dir=image_dir)

# Function call to search and download images
search('Social Media Bigdata', 10)


# In[ ]:




