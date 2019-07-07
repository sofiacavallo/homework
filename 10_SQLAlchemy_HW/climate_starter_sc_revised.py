# # Step 2 - Climate App

# 1. Import Flask
from flask import Flask
import sys

# 2. Create an app, being sure to pass __name__ (boilerplate)
app = Flask(__name__)

# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Hawaii Climate' page...")
    return "Welcome to my 'Hawaii Climate' page!"

# 4. Define what to do when a user hits the /precipitation route
@app.route("/api/v1.0/precipitation")
def about():
    print("Server received request for 'Precipitation' page...")
    return "Welcome to my 'Precipitation' page!"

if __name__ == "__main__":
    app.run(debug=True)
