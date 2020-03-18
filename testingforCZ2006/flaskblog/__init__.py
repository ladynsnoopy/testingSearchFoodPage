from flask import Flask
from flaskblog.forms import RegistrationForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Integer, Column, Float, DateTime
from sqlalchemy.orm import relationship
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'the random string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)




from flaskblog import routes