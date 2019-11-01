## US State Address Geolocator

###Setup:
######Code:
1. Install the project requirements using `pip install -r requirements.txt`

######Database (optional):
1. Install the Postgres.app application (https://postgresapp.com/). 
    * This gives us an easy-to-set up Postgres database, the PostGIS extension, a tool to import shape files into a PostGIS-enabled database called shp2pgsql
2. Open Postgres.app to start a Postgres server with 3 default databases.
3. Using a tool such as pgAdmin, add the extension PostGIS (see image below)
4. Now it is possible to execute the command to load the shape files. Run the following in your command line, substituting values where necessary.
    * `shp2pgsql resources/shape_files/tl_2019_us_state.shp DATATABLE | psql -U DATABASE_USER -d DATABASE_NAME`
5. Test by running a select statement against the table!
    * Note, you'll either need to double click your database in Postgress.app or run `psql -h localhost -U DATABASE_USER DATABASE_NAME` to start a db shell.
    
<img src="https://github.com/gmallory3/US-State-Geocode/tree/master/resources/DB_setup_img_001.png" width="48">

###Run:
1. In a terminal, run `python app.py`
2. Now that the API is running, go to a website such as `http://localhost:4996/api/v1/find_state/3535 Piedmont Rd NE, Atlanta, GA 30305` or use an API testing tool such as Postman to check it out!


###Design Notes:
1. External application Postgres.app used for it's simple setup.
2. External library Flask chosen for it's common use in industry.
 
###Possible (and necessary?) Future Extensions:
* Swagger documentation
* Define API Test suite in Postman sandbox
* Containerize with Docker (potentially including DB instance or DB setup script & maintenance tools such as Flyway as well)
* Street View Publish API could give image of the address as API endpoint
* Longitude and Latitude can be reversed into an address easily with Geocoding API
* Status messages, logging, testing can all be improved.

You can read more about Google's Geocoding API here: https://developers.google.com/maps/documentation/geocoding/intro