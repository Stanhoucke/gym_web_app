# Gym Web App
A management facing web application to manage gym members and classes. Using a cross country ski club as the client.

## Brief
A local gym has asked you to build a piece of software to help them to manage memberships, and register members for classes.

### MVP

- The app should allow the gym to create and edit Members
- The app should allow the gym to create and edit Classes
- The app should allow the gym to book members on specific classes
- The app should show a list of all upcoming classes
- The app should show all members that are booked in for a particular class

### Extensions
- Anything else you would like to add

## How to run
#### Installations
The web app runs on a Flask framework and uses the psycopg2 library for database connections.

To install Flask:
  `pip3 install flask`

To install pyscopg2:
  `pip3 install pyscopg2`

#### Database
PostgreSQL was used in this project. SQL queries are included in the app (gym_app.sql) to create tables in the database.

To create a database and tables:
1. `createdb gym_web_app`
1. `psql -d gym_web_app -f db/gym_app.sql`
1. If you would like some data to start with, execute the following in the terminal within the app directory: `python3 console.py`

#### Run Web App
In the terminal, within the app folder, execute `flask run` to run the web app. When running, the app can be viewed in a browser on localhost:5000.

