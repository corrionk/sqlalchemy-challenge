import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite", connect_args={'check_same_thread': False})


Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

#weather app
app = Flask(__name__)


@app.route("/")
def home():
    return (f"Welcome to Surf's Up!: Hawai'i Climate API<br/>"
            f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br/>"
            f"Available Routes:<br/>"
            f"/api/v1.0/stations <br/>"
            f"/api/v1.0/precipitaton<br/>"
            f"/api/v1.0/temperature <br/>"
            f"~~~ datesearch (yyyy-mm-dd)<br/>"
            f"/api/v1.0/datesearch/2015-05-30 br/>"
            f"/api/v1.0/datesearch/2015-05-30/2016-01-30<br/>"



