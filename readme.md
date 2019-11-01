## US State Address Geolocator

###Code setup:
1. Install the project requirements using `pip install -r requirements.txt`
2. 


###Database Setup (optional):
1. Install the Postgres.app application (https://postgresapp.com/). 
    * This gives us an easy-to-set up Postgres database, the PostGIS extension, a tool to import shape files into a PostGIS-enabled database called shp2pgsql
2. Open Postgres.app to start a Postgres server with 3 default databases.
3. Using a tool such as pgAdmin, add the extension PostGIS (see image below)
4. Now it is possible to execute the command to load the shape files. Run the following in your command line, substituting values where necessary.
    * `shp2pgsql resources/shape_files/tl_2019_us_state.shp DATATABLE | psql -U DATABASE_USER -d DATABASE_NAME`
5. Test by running a select statement against the table!
    * Note, you'll either need to double click your database in Postgress.app or run `psql -h localhost -U DATABASE_USER DATABASE_NAME` to start a db shell.
    
<img src="https://github.com/gmallory3/US-State-Geocode/tree/master/resources/DB_setup_img_001.png" width="48">


Run code by:
1. TBD

Design Notes:
1. Using postgres.app as the database manager.
2. It comes with Postgres and PostGIS extension. 
3. It also has a tool to import shape files into a PostGIS-enabled database called shp2pgsql

Possible Future Extensions:
* Swagger documentation
* Define tests in postman sandbox
* Containerize with Docker (potentially including DB instance as well)
* Street View Publish API could give image of the address as API endpoint

You can read more about Google's Geocoding API here: https://developers.google.com/maps/documentation/geocoding/intro