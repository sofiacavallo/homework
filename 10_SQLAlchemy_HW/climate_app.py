# Imports from IPYNB file
import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

measurement = Base.classes.measurement
station = Base.classes.station
session = Session(engine)


# Create an app, being sure to pass __name__ (boilerplate)
app = Flask(__name__)

# HOME PAGE: when a user hits the index route, list all available api routes.
@app.route("/")
def home():
    print("Server received request for 'Hawaii Climate' page. List all available api routes.")
    return(
        f"Welcome to my 'Hawaii Climate' page!<br>"
        f"Available Routes:<br>"
        f"/api/v1.0/precipitation<br>"
        f"/api/v1.0/stations<br>"
        f"/api/v1.0/tobs<br>"
    )

# /api/v1.0/stations
# Convert the query results to a Dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.

@app.route("/api/v1.0/precipitation")
def precipitation():
    dict = {}
    data = df[(df.date >= str(prev_year)) & (df.date <= str(today))].groupby(['date']).sum()
    for index, row in df.iterrows():
       dict[row.date] = row.prcp
    return jsonify(dict)

# /api/v1.0/stations
# Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():
    stations = list(df.measurement.unique())
    return jsonify(stations)

# /api/v1.0/tobs
# query for the dates and temperature observations from a year from the last data point.
# Return a JSON list of Temperature Observations (tobs) for the previous year.

@app.route("/api/v1.0/tobs")
def tobs():
    results = session.query(measurement.date, measurement.tobs).filter(measurement.date >= prev_year).all()
    temp_results = list(np.ravel(results))
    return jsonify(temp_results)

# /api/v1.0/<start>/<end>
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

@app.route("/api/v1.0/<start>/<end>")
def temp_start_end(start, end):
    temps = df[(dfdate >= start) & (df.date <= end)]
    min_temp = temps.tobs.min()
    max_temp = temps.tobs.max()
    avg_temp = temps.tobs.mean()
    return jsonify({"min_temp": int(min_temp), "max_temp": int(max_temp), "avg_temp": (avg_temp)})

# Add boilerplade debugger at the end of the code.
if __name__ == "__main__":
    app.run(debug=True)