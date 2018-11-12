from console import *
import nltk
import re
from nltk.corpus import stopwords
stopwords = stopwords.words('english') #set stopwords as a global variable

#a list of lists populated with each descriptions as a list of words as string
def get_descriptions(shortname):
    list_of_descriptions = session.query(Beer.description).join(Style).filter(Style.shortName == shortname).filter(Beer.description != None).all()
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
    return fdist1.most_common(50)


from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

import plotly.graph_objs as go
def plot_words(shortname):
    words = [word[0] for word in count_key_words(shortname)]
    counts = [word[1] for word in count_key_words(shortname)]
    init_notebook_mode(connected=True)
    iplot([{"x": words, "y": counts}])

plot_words('American Lager')


def beers_in_style(shortname):
    return len(session.query(Beer.name).join(Style).filter(Style.shortName == shortname).all())
