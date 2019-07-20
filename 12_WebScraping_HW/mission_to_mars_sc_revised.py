#!/usr/bin/env python
# coding: utf-8

# In[1]:


# # Initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
# import sys
# !{sys.executable} -m pip install pymongo


# In[2]:


# Import dependencies 
from bs4 import BeautifulSoup
from splinter import Browser
import pymongo
import requests
import pandas as pd
import time


# In[5]:


# Set up splinter browser
executable_path = {'executable_path': 'C:/Users/19143/Desktop/chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# NASA MARS NEWS

# In[6]:


# NASA MARS NEWS SCRAPING

# Visit URL
# executable_path = {'executable_path': 'C:/Users/19143/Desktop/chromedriver.exe'}
# browser = Browser('chrome', **executable_path, headless=False)
nasa_url = "https://mars.nasa.gov/news/"

# Put url into search bar
browser.visit(nasa_url)
# Load the page
# Wait for 3 secs
time.sleep(3)

# Pull html 
nasa_html = browser.html

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(nasa_html, "html.parser")
# browser.quit()


# In[7]:


#soup.find_all('a')[0]


# In[8]:


# Grab information of interest (article title and teaser copy)
news_title = soup.find('div', class_="content_title").text
news_teaser = soup.find('div', class_="article_teaser_body").text

# Test print to check work
print(news_title)
print(news_teaser) 


# JPL MARS SPACE IMAGES (FEATURED IMAGE)

# In[9]:


# Visit URL
# executable_path = {'executable_path': 'C:/Users/19143/Desktop/chromedriver.exe'}
# browser = Browser('chrome', **executable_path, headless=False)
jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

# Put url into search bar
browser.visit(jpl_url)
# Load the page
# Set wait time to 3 secs so that you don't wait for the entire page's HTML to load (you only need latest data elements)
time.sleep(3)

# Pull HTML
jpl_html = browser.html

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(jpl_html, "html.parser")
# browser.quit()


# In[10]:


# Find the information of interest (featured image) and create relative path for it
featured_image = soup.find('article', class_= "carousel_item") 
style = featured_image['style']
relative_path = style.split("'")[1]
relative_path


# In[12]:


# Create a full URL for the image path.
image_full_path = "https://www.jpl.nasa.gov" + relative_path

# Test print to check work
print(image_full_path)


# MARS WEATHER

# In[13]:


# Visit URL
# executable_path = {'executable_path': 'C:/Users/19143/Desktop/chromedriver.exe'}
# browser = Browser('chrome', **executable_path, headless=False)
marsweather_url = "https://twitter.com/marswxreport?lang=en"

# Put url into search bar
browser.visit(marsweather_url)

# Load the page
# Set wait time to 3 secs so that you don't wait for the entire page's HTML to load (you only need latest data elements)
time.sleep(3)

# Pull HTML
marsweather_html = browser.html

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(marsweather_html, "html.parser")
# browser.quit()

# Grab information of interest (weather)
marsweather = soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

# Test print to check work
print(marsweather)


# MARS FACTS

# In[41]:


# Visit URL
# executable_path = {'executable_path': 'C:/Users/19143/Desktop/chromedriver.exe'}
# browser = Browser('chrome', **executable_path, headless=False)
marsfacts_url = "https://space-facts.com/mars/"

# Put url into search bar
browser.visit(marsfacts_url)

# Load the page
# Set wait time to 3 secs so that you don't wait for the entire page's HTML to load (you only need latest data elements)
time.sleep(3)

# Use Pandas Read HTML to parse the HTML code
marsfacts = pd.read_html(marsfacts_url)
marsfacts


# In[45]:


# Results returns a list. Find mars facts dataframe in the list. Assign it to marsfacts_df variable.
marsfacts_df = marsfacts[1]
marsfacts_df


# In[46]:


# Change column headers to "Description" and "Value"
marsfacts_df.columns=['Description', 'Value']
marsfacts_df


# In[49]:


# Use pandas to convert the data into an HTML string
marsfacts_table = marsfacts_df.to_html(header = False, index = False)
marsfacts_table


# MARS HEMISPHERES

# In[51]:


# Visit URL
#hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

# Put url into search bar
#browser.visit(hemispheres_url)

# Load the page
# Set wait time to 3 secs so that you don't wait for the entire page's HTML to load (you only need latest data elements)
#time.sleep(3)

# Pull HTML
#hemispheres_html = browser.html

# Parse HTML using BeautifulSoup
#soup = BeautifulSoup(hemispheres_html, "html.parser")

# Grab information of interest (items with hemispheres information) and create a list for hemisphere image URLs.
#items = soup.find_all('div', class_='item')
#hemisphere_image_urls = []


# In[ ]:


#hemisphere_image_urls


# In[52]:


# Store the full URL path as a variable
#hemispheres_full_url = 'https://astrogeology.usgs.gov/'

# Run a for-loop to grab the thumb image URLs and modify them to be the full jpgs.
#for i in items:
    # Store title
#    title = i.find('alt').text
    
    # Store URL for full image

    
# --> go to full image URL and scrape there? or scrape from this page and remove/appent full image attributes? 
    
#featured_image = soup.find('article', class_= "carousel_item") 
#style = featured_image['style']
#relative_path = style.split("'")[1]
#relative_path

# Test print to check work
#print(hemisphere_image_urls)


# ### Create Data for Storage (to Mongo)

# In[55]:


scraped_data = {
    'news_title': news_title,
    'news_teaser': news_teaser,
    'image_full_path': image_full_path,
    'mars_weather_text': marsweather,
    'marsfacts_table': marsfacts_table
}


# In[56]:


scraped_data


# In[ ]:




