from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import dash

server = Flask(__name__)
server.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///beers4.db'
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
server.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(server)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, server=server, url_base_pathname='/dashboard/', external_stylesheets=external_stylesheets)

from dash_package.get_data import GetBeerData, BeerBuilder, StyleBuilder, IngredientBuilder

from dash_package.models import *
from dash_package.routes import *
from dash_package.plots import *
from dash_package.dashboard import *
