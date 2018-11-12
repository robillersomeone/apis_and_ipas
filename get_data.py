import requests
from beer_and_styles import Beer, Style, Base
from sqlalchemy.orm import sessionmaker
import sqlalchemy


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
                beer['style']
                try:
                    beer['style']['shortName']
                    try:
                        each_beer = Beer(name = beer['name'],
                        nameDisplay = beer['nameDisplay'], description = beer['description'],
                        abv = beer['abv'], ibu = beer['ibu'], isOrganic = beer['isOrganic'],
                        foodPairings = beer['foodPairings'], style = beer['style']['name'])
                        each_beer.style_shortName = session.query(Style).filter(Style.shortName == beer['style']['shortName']).first()
                    except:
                        keys = beer.keys()
                        each_beer = Beer(name = beer['name'])
                        if "description" in keys:
                            each_beer.description = beer['description']
                        if "nameDisplay" in keys:
                            each_beer.name = beer['nameDisplay']
                        if "abv" in keys:
                            each_beer.abv = beer['abv']
                        if "ibu" in keys:
                            each_beer.abv = beer['ibu']
                        if "isOrganic" in keys:
                            each_beer.isOrganic = beer['isOrganic']
                        if "foodPairings" in keys:
                            each_beer.foodPairings = beer['foodPairings']
                        if "style" in keys:
                            each_beer.style = beer['style']['name']
                        each_beer.style_shortName = session.query(Style).filter(Style.shortName == beer['style']['shortName']).first()
                except:
                    pass
            except:
                pass
            beers.append(each_beer)
        return beers


class StyleBuilder:
    def run(self):
        styler = requests.get('http://api.brewerydb.com/v2/styles?key=f684318419e2e8da8014c50bb077ddc6&p=1')
        style_data = styler.json()['data']
        beer_styles = []
        for style in style_data:
            try:
                each_style = Style(name = style['name'], shortName = style['shortName'], category = style['category']['name'], description = style['description'],
                ibuMin = style['ibuMin'], ibuMax = style['ibuMax'], abvMin = style['abvMin'], abvMax = style['abvMax'])
            except:
                keys = style.keys()
                each_style = Style(name = style['name'])
                if "shortName" in keys:
                    each_style.shortName = style['shortName']
                if "description" in keys:
                    each_style.description = style['description']
                if "category" in keys:
                    each_style.category = style['category']['name']
                if "ibuMin" in keys:
                    each_style.ibuMin = style['ibuMin']
                if "ibuMax" in keys:
                    each_style.ibuMax = style['ibuMax']
                if "abvMin" in keys:
                    each_style.abvMin = style['abvMin']
                if "abvMax" in keys:
                    each_style.abvMax = style['abvMax']
            beer_styles.append(each_style)
        return beer_styles


engine = sqlalchemy.create_engine('sqlite:///beers.db', echo=True)
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

# x = StyleBuilder()
# session.add_all(x.run())
# session.commit()
#
# y = BeerBuilder()
# session.add_all(y.run())
# session.commit()
