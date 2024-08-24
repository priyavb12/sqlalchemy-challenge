# sqlalchemy-challenge
## challenge 10
 
*Three* new **tools** :
 - SQLite 
 - SQLAlchemy and 
 - Flask. 

 ***

 
  These tools to build knowledge of SQL database structures and querying methods.

> SQLAlchemy, a Python library that’s designed to work with SQL databases. 

 >>- analyze weather data by using SQLAlchemy. 
 >>
 >>- Perform create, read, update, delete (CRUD) operations on data in a SQL database by using the SQLAlchemy object-relational mapper (ORM).

 1. Connect to a SQL database by using SQLAlchemy.

2. Perform basic SQL queries by using conn.execute().

3. Create Python classes and objects.

4. Perform create, read, update, delete (CRUD).

### Analyze and Explore the Climate Data

In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. 

Specifically, you’ll use **SQLAlchemy ORM queries, Pandas, and Matplotlib**. To do so, complete the following steps:

Note that you’ll use the provided files *(climate_starter.ipynb and hawaii.sqlite)*  to complete your climate analysis and data exploration.

- Use the SQLAlchemy create_engine() function to connect to your SQLite database.

- Use the SQLAlchemy automap_base() function to reflect your tables into classes, and then save references to the classes named station and measurement.

Link Python to the database by creating a SQLAlchemy session.

Perform a precipitation analysis and then a station analysis by completing the steps in the following two subsections.

### Design Your Climate App

Design a Flask API based on the queries that you just developed. To do so, use Flask to create your routes as follows:
 List all the available routes.

*/api/v1.0/precipitation*

Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.

Return the JSON representation of your dictionary.

*/api/v1.0/stations*

Return a JSON list of stations from the dataset. 

  */api/v1.0/tobs*

Query the dates and temperature observations of the most-active station for the previous year of data.

Return a JSON list of temperature observations for the previous year.

*/api/v1.0/<start> and /api/v1.0/<start>/<end>*

Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

- For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

- For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.


### References

My on go search engine is [markdownguide](https://www.markdownguide.org/basic-syntax/) for Readme.

<https://www.markdownguide.org/basic-syntax/>
<markdownguide.com>


### SQLalchemy

![sqlalchemy](https://miro.medium.com/v2/resize:fit:200/0*2gcZYBv6jmcbRtnY)