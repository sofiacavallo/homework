# Import dependencies 
from bs4 import BeautifulSoup
from splinter import Browser
import pymongo
import requests
import pandas as pd
import time

def mars_scrape():
    print('mars_scrape - Scraping NASA')

    # # NASA Mars News Scrape

    # Set up splinter browser and declare website
    executable_path = {'executable_path': 'C:/Users/19143/Desktop/chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    nasa_url = "https://mars.nasa.gov/news/"

    # Load URL into search bar
    browser.visit(nasa_url)
    # Set wait time to 3 secs so that you don't wait for the entire page's HTML to load (you only need latest data elements)
    time.sleep(3)

    # Pull html. Parse HTML using BeautifulSoup
    nasa_html = browser.html
    soup = BeautifulSoup(nasa_html, "html.parser")

    # Grab information of interest (article title and teaser copy)
    news_title = soup.find('div', class_="content_title").text
    news_teaser = soup.find('div', class_="article_teaser_body").text

    # Test print to check work
    print(news_title)
    print(news_teaser) 

    # # JPL Mars Space Image (Featured Image) Scrape

    # Declare website to visit and load in search bar
    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url)

    # Set wait time to 3 secs so that you don't wait for the entire page's HTML to load (you only need latest data elements)
    time.sleep(3)

    # Pull html. Parse HTML using Beautiful Soup
    jpl_html = browser.html
    soup = BeautifulSoup(jpl_html, "html.parser")

    # Find the information of interest (featured image) and create relative path for it
    featured_image = soup.find('article', class_= "carousel_item") 
    style = featured_image['style']
    relative_path = style.split("'")[1]
    relative_path

    # Create a full URL for the image path.
    image_full_path = "https://www.jpl.nasa.gov" + relative_path

    # Test print to check work
    print(image_full_path)

    # # Mars Weather Tweet Scrape

    # Declare website to visit and load in search bar
    marsweather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(marsweather_url)

    # Set wait time to 3 secs so that you don't wait for the entire page's HTML to load (you only need latest data elements)
    time.sleep(3)

    # Pull HTML. Parse HTML using BeautifulSoup
    marsweather_html = browser.html
    soup = BeautifulSoup(marsweather_html, "html.parser")

    # Grab information of interest (weather)
    mars_tweets = soup.find_all('div', class_='js-tweet-text-container')
    
    # Retrieve only tweets that contain weather information
    for tweet in mars_tweets:
        marsweather_tweet = tweet.find('p').text
        if 'InSight sol' in marsweather_tweet:
            print(marsweather_tweet)
            break
        else:
            pass

    # Test print to check work
    print(marsweather_tweet)


    # # MARS FACTS

    # Declare website to visit and load in search bar
    marsfacts_url = "https://space-facts.com/mars/"
    browser.visit(marsfacts_url)

    # Set wait time to 3 secs so that you don't wait for the entire page's HTML to load (you only need latest data elements)
    time.sleep(3)

    # Use Pandas Read HTML to parse the HTML code
    marsfacts = pd.read_html(marsfacts_url)
    print(marsfacts)

    # Results returns a list. Find mars facts dataframe in the list [1]. Assign it to marsfacts_df variable.
    marsfacts_df = marsfacts[1]
    marsfacts_df

    # Change column headers to "Description" and "Value"
    marsfacts_df.columns=['Description', 'Value']
    marsfacts_df

    # Use pandas to convert the data into an HTML string
    marsfacts_table = marsfacts_df.to_html(header = False, index = False)
    marsfacts_table


    #  # MARS HEMISPHERES

    # Declare website to visit and load in search bar
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)

    # Set wait time to 3 secs so that you don't wait for the entire page's HTML to load (you only need latest data elements)
    time.sleep(3)

    # Pull html. Parse HTML using Beautiful Soup
    hemispheres_html = browser.html
    soup = BeautifulSoup(hemispheres_html, "html.parser")

    # Retrieve all items that contain thumbnail image URL. You will need to open the thumbnail links and scrape that page for the high-res URLs.
    items = soup.find_all('div', class_='item')

    # Create a list to store the high-res image URLs
    hemispheres_hires_imgs = []

    # Store the main URL
    hemispheres_main_url = 'https://astrogeology.usgs.gov'

    # Usa a loop to go through the thumbnail URLs stored in the list, open the links, and scrape that page for the high-res image URL and title.
    for i in items:
        # Store image title
        title = i.find('h3').text
    
        # Store the partial link to the page containing high-res image
        hires_img_page_url = i.find('a', class_='itemLink product-item')['href']
    
        # Visit this page
        browser.visit(hemispheres_main_url + hires_img_page_url)
    
        # Open the page and parse with BeautifulSoup.
        hires_img_page_html = browser.html
        soup = BeautifulSoup(hires_img_page_html, "html.parser")

        # Store partial URL for the high-res image
        hires_img_partial_url = soup.find('img', class_='wide-image')['src']

        # Generate full URL for high res image
        hires_img_full_url = hemispheres_main_url + hires_img_partial_url
    
        # Append full URLs to list of dictionaries
        hemispheres_hires_imgs.append({'title': title, 'img_url': hires_img_full_url})

    # Print high-res image titles and URLs
    print(hemispheres_hires_imgs)

    # # Create Data for Storage (to Mongo)

    scraped_data = {
        'news_title': news_title,
        'news_teaser': news_teaser,
        'image_full_path': image_full_path,
        'mars_weather_text': marsweather_tweet,
        'marsfacts_table': marsfacts_table,
        'mars_hemispheres_imgs': hemispheres_hires_imgs
    }

    return scraped_data






