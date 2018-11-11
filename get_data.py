import requests
from beer_and_styles import Beer, Style
from sqlalchemy.orm import sessionmaker
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
engine = sqlalchemy.create_engine('sqlite:///beers.db', echo=True)
Base = declarative_base()
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()


class GetBeerData:
    def get_beer_data(self):
        pages = range(1,24)
        full_pages = []
        for i in pages:
            r = requests.get(f'http://api.brewerydb.com/v2/beers?key=f684318419e2e8da8014c50bb077ddc6&p={i}')
            data = r.json()['data']
            full_pages.append(data)
        all_pages = []
        list(map(all_pages.extend, full_pages))
        return all_pages

class BeerBuilder:
    def run(self):
        beer_data = GetBeerData()
        beer_data.get_beer_data()
        beers = []
        for beer in beer_data.get_beer_data():
            try:
                each_beer = Beer(name = beer['name'],
                nameDisplay = beer['nameDisplay'], description = beer['description'],
                abv = beer['abv'], ibu = beer['ibu'], isOrganic = beer['isOrganic'],
                foodPairings = beer['foodPairings'], style = beer['style']['name'])
                Beer.style_shortname = session.query(Style).filter(Style.style_shortName == beer['style']['shortName'])
            except:
                each_beer = Beer(name = beer['name'],
                nameDisplay = beer['nameDisplay'], abv = beer['abv'], isOrganic = beer['isOrganic'],
                style = beer['style']['name'])
                Beer.style_shortname = session.query(Style).filter(Style.style_shortName == beer['style']['shortName'])
            beers.append(each_beer)
        return beers



class StyleBuilder:
    def run(self):
        styler = requests.get('http://api.brewerydb.com/v2/styles?key=f684318419e2e8da8014c50bb077ddc6&p=1')
        style_data = styler.json()['data']
        styles = []
        for style in style_data:
            try:
                each_style = Style(name = style['name'], category = style['category']['name'], description = style['description'], ibuMin = style['ibuMin'], ibuMax = style['ibuMax'], abvMin = style['abvMin'], abvMax = style['abvMax'])
            except:
                each_style = Style(name = style['name'], category = style['category']['name'])
            styles.append(each_style)
            session.add_all(styles)
        return styles
