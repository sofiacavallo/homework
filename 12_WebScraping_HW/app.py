from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import json
# import scrape_costa

# import scraping file
import mission_to_mars_sc_revised

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connecstion
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    print('Fetching Mars Data from DB...')
    mars_data = mongo.db.mars_collection.find_one()
    print('mars_data:', mars_data)

    # Return template and data
    return render_template("index.html", mars_data=mars_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    # use the scraping file
    scraped_data = mission_to_mars_sc_revised.mars_scrape()

    # Run the scrape function
    # costa_data = scrape_costa.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.mars_collection.update({}, scraped_data, upsert=True)

    # Redirect back to home page
    return json.dumps(scraped_data)

if __name__ == "__main__":
    app.run(debug=True)
