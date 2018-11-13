from flask import render_template
from dash_package.models import Style, Beer
from dash_package import server
import pdb

@server.route('/beers')
def beer_facts():
    all_beers = Beer.query.all()
    list_of_beers = str([beer.name for beer in all_beers])
    return list_of_beers
    # return render_template('index.html', apartments = apartments)
