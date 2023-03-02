from flask import render_template, jsonify

from my_app import app

import datetime as dt
import numpy as np
# import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# For debugging/printing to console
import sys

engine = create_engine("sqlite:///hawaii.sqlite", connect_args={'check_same_thread': False}) # set thread to False to fix error: "Objects created in a thread can only be used in that same thread"
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)


@app.route('/')
def index():
    custom_message = "Flask API Example"
    return render_template("index.html", message=custom_message)

@app.route("/api/v1.0/precipitation")
def precipitation():
   # Subtract 1 year for date 2017-08-23
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   # Query measurement table
   # Filter date: Select all records newer than or equal to prev_year 2017-08-23 for station USC00519397
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).filter(Measurement.station == "USC00519397").all()
   # Assign dictionary comprehension to iterate data and assign results to variable
   precip = {date: prcp for date, prcp in precipitation}
   # print(precip, file=sys.stderr)
   # Return JSON
   return jsonify(precip)

@app.route("/api/v1.0/stations")
def stations():
    # Query all weather stations from station table
    results = session.query(Station.station).all()
    # Return 1D list with .ravel()
    stations = list(np.ravel(results))
    # Return a JSON with 'stations' (key) and station list (values)
    return jsonify(stations=stations)

@app.route("/api/v1.0/tobs")
def temp_monthly():
   # Subtract 1 year for date 2017-08-23
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Query measurement table
    # Filter date: Select all records newer than or equal to prev_year 2017-08-23 for station USC00519281
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    # Return 1D list with .ravel()
    temps = list(np.ravel(results))
    print(temps, file=sys.stderr)
    # Return a JSON with 'temps' (key) and temperature list (values)
    return jsonify(temps=temps)

# Create routes for wildcard values
@app.route("/api/v1.0/temp/<start>")
# URL contains <start> placeholder for user e.g., http://localhost:5500/api/v1.0/temp/2017-06-01/2017-06-30
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    # Create variable to store arguments for minimum, average, and maximum temperature
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    # If no end date is provided include all dates
    if not end:
        # Pass list of arguments to session.query()
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    # If start and end dates are provided
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    
    # Return JSON with summarized results
    return jsonify(temps)