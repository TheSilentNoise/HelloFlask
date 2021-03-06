from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('hello.config')

db = SQLAlchemy(app)

import hooks
import models
import views
