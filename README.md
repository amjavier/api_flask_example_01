# Flask API Example

* Live app: https://api-flask-example-01.herokuapp.com/

* API routes:

<img src="./img/api_001.PNG " width="400">

### Summary
This repository contains a basic REST API I built with Python and Flask as part of a data analysis course.
<br>
The database I used is SQLite but Flask can be used with many other databases, including PostgreSQL and MS SQL Server. The principle is the same with any relational database, the GET request will supply a JSON file. There are of course other HTTP methods like POST, PUT, and DELETE but those are not part of this example.
<br>
The database contains 2 weather station tables: measurement (measured precipitation and temperature per weather station) and station (weather station info). The dataset contains between 2010 and 2017. The purpose of this basic app is to show that Python, in addition to being used for data science and analysis, can also be used to build robust back-end web applications.
<br>
<br>
The 3 available GET routes are listed below:
1. /api/v1.0/precipitation => precipitation (Inch)
   * <img src="./img/precipitation_002.PNG" width="400">
2. /api/v1.0/stations => weather station info
   * <img src="./img/stations_003.PNG" width="400">
3. /api/v1.0/tobs => temperature (Fahrenheit)
   * <img src="./img/temp_004.PNG" width="400">
4. /api/v1.0/temp/<start>/<end> => start and end are date placeholders, e.g., .../temp/2017-06-01/2017-06-30
   * <img src="./img/temp_005.PNG" width="400">

