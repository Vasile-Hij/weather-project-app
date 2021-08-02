Weather application with user authentication in Flask
--
**Quick description:**
 
This application will display a web page with user authentication by default, 
then check the weather for your desired location and measurements in Celsius or Fahrenheit degrees.

**Tools**

* Backend: python with API and SQLite database
* OpenWeatherMap API make the data collection
* SQLAlchemy stores the data for API queries and users registration
* Flask used for web application
* Front-End: HTML/CSS/Jinja 


**Functionality**

1.1 Deploy virtual environment Windows.
```
$ py -m venv myprojectenv
$ .\myprojectenv\Scripts\activate 
$ easy_install -U pip
```

1.2 Deploy virtual environment Linux.
```
$ sudo apt update
$ sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
$ sudo apt install python3-venv
$ python3.7 -m venv myprojectenv
$ source myprojectenv/bin/activate
```


2. Install requirements
```
$ pip install wheel
$ python3 -m pip install -r requirements.txt (linux)
$ py -m pip install -r requirements.txt (windows)
```

3. Create configuration
```
$ cd project
$ nano config.py
```
Fill `secret_key` with an API key from https://openweathermap.org/current.
Also add desired measurements in `units` as metric or imperial
```
>>>press ctrl+x, choose 'yes', hit enter
$ python3 config.py
```   
4. Create database 
```
$ python3
>>> from project import db, create_app
>>> db.create_all(app=create_app())
>>> exit()
```

5. Run server`$ python3 wsgi.py`
6. You need to register or log in to website
7. Check the weather by switching from Celsius to Fahrenheit temperature and
   adding/deleting cities.
