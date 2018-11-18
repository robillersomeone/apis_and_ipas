from dash_package import app, db
from dash_package.models import *
import nltk
import re
from nltk.corpus import stopwords
from statistics import mean
stopwords = stopwords.words('english') #set stopwords as a global variable

from flask_sqlalchemy import SQLAlchemy

#a list of lists populated with each descriptions as a list of words as string
def get_descriptions(shortname):
    list_of_descriptions = db.session.query(Beer.description).join(Style).filter(Style.shortName == shortname).filter(Beer.description != None).all()
    return [description[0].split() for description in list_of_descriptions]


#returns a list of sentences as strings
def get_all_words(shortName):
    b = []
    for i in get_descriptions(shortName):
        new_i = ' '.join(i)
        b.append(new_i)
    return b

#splits the sentences into one list of strings
def desc_to_string(shortName):
    new_list = []
    for x in get_all_words(shortName):
        new_list.append(x)
    first_string = ' '.join(new_list)
    words_first_string = re.sub(r'[^\w\s]','',first_string).lower()
    final_string = words_first_string.split()
    return final_string


#counts the number of key words
def count_key_words(shortName):
    mynewtext = [w.title() for w in desc_to_string(shortName) if w not in stopwords]
    mynewtext
    fdist1 = nltk.FreqDist(mynewtext)
    return fdist1.most_common(20)


from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

import plotly.graph_objs as go
def plot_words(shortname):
    words = [word[0] for word in count_key_words(shortname)]
    counts = [word[1] for word in count_key_words(shortname)]
    return {'x': words, 'y': counts, 'type': 'bar', 'name': shortname}



def beers_in_style(shortname):
    return len(db.session.query(Beer.name).join(Style).filter(Style.shortName == shortname).all())

def dropdown():
    all_shortnames = db.session.query(Style.shortName).all()
    options = []
    for name in all_shortnames:
        options.append({'label': name[0], 'value': name[0]})
    return options

def style_description(shortname):
    description = db.session.query(Style.description).filter(Style.shortName == shortname).first()[0]
    return str(description)

def min_max_abv(shortname):
    abv_min_max = db.session.query(Style.abvMin, Style.abvMax).filter(Style.shortName == shortname).all()
    abv_min = abv_min_max[0][0]
    abv_max = abv_min_max[0][1]
    return f"For {shortname} beers, the ABV ranges from {abv_min} to {abv_max}"

def avg_abv(shortname):
    all_abvs = db.session.query(Beer.abv).join(Style).filter(Style.shortName == shortname).all()
    return all_abvs
    #return mean([float(abv) for abv in all_abvs])

def style_foodpairings(shortname):
    list_of_descriptions = db.session.query(Beer.name, Beer.foodPairings).join(Style).filter(Style.shortName == shortname).filter(Beer.foodPairings != None).all()
    pairing_list = []
    for beer in list_of_descriptions:
        pairing = f"{beer[0]} goes with {beer[1]}"
        #pairing = {"beer name" : beer[0], "food pairing": beer[1].replace("\r\n", " ")}
        pairing_list.append(pairing)
    return ('\n'.join(map(str, pairing_list))) 

def style_name(shortname):
    name = db.session.query(Style.shortName).filter(Style.shortName == shortname).first()[0]
    foodpairings = style_foodpairings(shortname)
    return f"Hungry for dinner? Here are some {name}-style beers and their suggested food pairings for you to try!"
