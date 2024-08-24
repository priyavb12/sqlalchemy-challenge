#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt


# In[4]:


import numpy as np
import pandas as pd
import datetime as dt


# # Reflect Tables into SQLAlchemy ORM

# In[6]:


# Python SQL toolkit and Object Relational Mapper
    import sqlalchemy
    from sqlalchemy.ext.automap import automap_base
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine, func


# In[10]:


# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# In[12]:


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine)


# In[14]:


# View all of the classes that automap found
Base.classes.keys()


# In[16]:


# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station


# In[18]:


# Create our session (link) from Python to the DB
session = Session(engine)


# # Exploratory Precipitation Analysis

# In[29]:


# Find the most recent date in the data set.
most_recent_date = session.query(func.max(Measurement.date)).first()
most_recent_date


# In[39]:


# Design a query to retrieve the last 12 months of precipitation data and plot the results. 
# Starting from the most recent data point in the database. 


# Calculate the date one year from the last date in data set.
prev_year = dt.date(2017,8,23) - dt.timedelta(days=365)

# Perform a query to retrieve the data and precipitation scores
results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()


# Save the query results as a Pandas DataFrame. Explicitly set the column names
df = pd.DataFrame(results, columns = ('date','precipitation'))

# Sort the dataframe by date
df = df.sort_values('date')

# Use Pandas Plotting with Matplotlib to plot the data
df.plot(x='date', y='precipitation',rot = 90)
plt.xlabel('Date')
plt.ylabel('Inches')


# In[41]:


# Use Pandas to calculate the summary statistics for the precipitation data
df.describe()


# # Exploratory Station Analysis

# In[53]:


# Design a query to calculate the total number of stations in the dataset
session.query(func.count(Station.station)).all()


# In[55]:


# Design a query to find the most active stations (i.e. which stations have the most rows?)
# List the stations and their counts in descending order.
session.query(Measurement.station, func.count(Measurement.station)).\
    group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()


# In[57]:


# Using the most active station id from the previous query, calculate the lowest, highest, and average temperature.
session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
    filter(Measurement.station == 'USC00519281').all()


# In[61]:


# Using the most a ctive station id
# Query the last 12 months of temperature observation data for this station and plot the results as a histogram

import datetime as dt
from pandas.plotting import table

prev_year = dt.date(2017,8,23) - dt.timedelta(days=365)

results = session.query(Measurement.tobs).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date >= prev_year).all()

df = pd.DataFrame(results, columns =['tobs'])
df.plot.hist(bins=12)
plt.tight_layout()
plt.xlabel('Temp')


# # Close Session

# In[63]:


# Close Session
session.close()


# In[ ]:




