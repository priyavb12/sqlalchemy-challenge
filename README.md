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

### Install Required Libraries:

Make sure you have Python installed on your system.
Install Flask and other necessary libraries by running the following command in your terminal:

*pip install Flask sqlalchemy numpy*

### Database Setup:

Ensure you have the SQLite database file **hawaii.sqlite** located in the Resources directory.
The database should contain the necessary tables for the app to query (e.g., Measurement and Station).

Run the Flask App:

Save the provided Flask app code in a file named app.py in your project directory.
Run the Flask app by executing the following command in the terminal:
python app.py
Accessing the API Endpoints:

Once the Flask app is running, you can access the API endpoints using a web browser. Use the following routes to interact with the API:

/api/v1.0/precipitation - Retrieve precipitation data.

/api/v1.0/stations - Get a list of stations.

/api/v1.0/tobs - Retrieve temperature observations.

/api/v1.0/temp/start_date - Get temperature statistics for a specific start date.

/api/v1.0/temp/<start>/<end> - Get temperature statistics for a date range.

#### Interacting with the API:

Make GET requests to the specified routes to retrieve the data in JSON format.
Ensure to follow the format requirements for date inputs in the /api/v1.0/temp/<start>/<end> route (MMDDYYYY).

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

### Create Flask app
*app = Flask(__name__)*

#### Create engine and reflect the tables
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine)

Measurement = Base.classes.measurement

Station = Base.classes.station

session = Session(engine)

#### Define routes

List all the available routes.

*/api/v1.0/precipitation*

 route returns a JSON object with precipitation data.

*/api/v1.0/stations*

route returns a JSON list of stations.

  */api/v1.0/tobs*

route returns a JSON list of temperature observations.

 */api/v1.0/temp/start_date*
 
route calculates temperature statistics for a specific start date.

*/api/v1.0/temp/<start>/<end>*

route calculates temperature statistics for a range of dates.

### References

My on go search engine is [markdownguide](https://www.markdownguide.org/basic-syntax/) for Readme.

<https://www.markdownguide.org/basic-syntax/>



### SQLalchemy

![sqlalchemy](https://miro.medium.com/v2/resize:fit:200/0*2gcZYBv6jmcbRtnY)