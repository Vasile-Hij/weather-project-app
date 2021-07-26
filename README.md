Weather application with user authentication in Flask
--
**Quick description:**
 
This application will display a web page with user authentication by default, 
then check the weather for your desired location.

**Tools**

* Backend: python with API and database
* OpenWeatherMap API make the data collection
* SQLAlchemy stores the data for API queries and users registration
* Flask used for web application
* Front-End: HTML/CSS/Jinja2 


**Functionality**

1. Deploy virtual environment.
```
virtualenv venv
source ./venv/bin/activiate
```
2. Install requirements
```bash 
# install python requirements
python3 -m pip install -r requirements.txt
```
3. Create database 
```
$ python3
>>> from project import db, create_app
>>> db.create_all(app=create_app())
>>> exit()
```

4. Configuration
`$ python3 ./project/config.py`
5. Run server`$ python3 wsgi.py`
6. You need to register or log in to website
7. Check the weather by adding/deleting cities.
