# Flask API Example

* Live app: 

### Summary
This repository contains a basic REST API I built with Python and Flask as part of a data analysis course. The 3 available GET routes are listed below:
1. /api/v1.0/precipitation => precipitation (Inch)
   * ...
2. /api/v1.0/stations => weather station info
   * ...
3. /api/v1.0/tobs => temperature (Fahrenheit)
4. /api/v1.0/temp/<start>/<end> => start and end are date placeholders, e.g., .../temp/2017-06-01/2017-06-30

The database I used is SQLite but Flask can be used with many other databases, including PostgreSQL and MS SQL Server. The principle is the same with any relational database, the GET request will receive a JSON file. The database contains 2 weather station tables: measurement (measured precipitation and temperature per weather station) and station (weather station info). The data was collected between 2010 and 2017. The purpose of this basic app is to show that Python, in addition to being used for data science and analysis, can also be used to build robust back-end web applications.
