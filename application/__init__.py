# import Flask class from the flask module
from flask import Flask
#import SQLAlchemy class from the flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from os import getenv


# create a new instance of Flask and store it in app
# This usage mode binds the instance to a very specific Flask application.
app = Flask(__name__)

#  ORM Object Relational Mapper
#  Object is Python classes
#  Relational is MySQL
# SQLAlchemy is the MAPPING layer between them
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://myapp:password@localhost/flask_team_a"
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://username:password@host/database_name"
# app.config['SQLALCHEMY_DATABASE_URI']=('mysql+pymysql://' + getenv('MYSQL_USER') + ':' + getenv('MYSQL_PASSWORD') + '@' + getenv('MYSQL_HOST') + '/' + getenv('MYSQL_DB'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
# app.config['SECRET_KEY'] = getenv('FLASK_SECRETKEY')

# link our app to the persistence layer
db = SQLAlchemy(app)



