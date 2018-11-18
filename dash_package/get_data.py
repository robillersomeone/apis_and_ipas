import requests
from dash_package.models import Beer, Style, Ingredient, BeerIngredients
from sqlalchemy.orm import sessionmaker
import sqlalchemy


class GetBeerData:
    def get_beer_data(self):
        pages = range(100,125)
        full_pages = []
        for i in pages:
            r = requests.get(f'http://api.brewerydb.com/v2/beers?key=34225f421585f1bbfa123e72317bd44a&p={i}')
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
                        each_beer = Beer(name = beer['name'], beercode = beer['id'],
                        nameDisplay = beer['nameDisplay'], description = beer['description'],
                        abv = beer['abv'], ibu = beer['ibu'], isOrganic = beer['isOrganic'],
                        foodPairings = beer['foodPairings'], style = beer['style']['name'])
                        each_beer.style_shortName = session.query(Style).filter(Style.shortName == beer['style']['shortName']).first()
                    except:
                        keys = beer.keys()
                        each_beer = Beer(name = beer['name'])
                        if "id" in keys:
                            each_beer.beercode = beer['id']
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


class GetIngredientData():
    #list of dictionaries. Each dictionary is an ingredient with id, name, category, categoryDisplay.
    def get_ingredient_data(self):
        pages = range(1,4)
        all_ingredients = []
        for page in pages:
            page_ingredients = requests.get(f'http://api.brewerydb.com/v2/ingredients?key=34225f421585f1bbfa123e72317bd44a&p={page}')
            ingredients = page_ingredients.json()['data']
            all_ingredients.append(ingredients)
        all_pages = []
        list(map(all_pages.extend, all_ingredients))
        return all_pages

class IngredientBuilder():
    def run(self):
        ingredients = GetIngredientData()
        ingredients_list = ingredients.get_ingredient_data()
        ingredients = []
        for ingredient in ingredients_list:
            each_ingredient = Ingredient(name = ingredient['name'], ingredientcode = ingredient['id'], category = ingredient['category'], categoryDisplay = ingredient['categoryDisplay'])
            ingredients.append(each_ingredient)
        return ingredients


class StyleBuilder:
    def run(self):
        styler = requests.get('http://api.brewerydb.com/v2/styles?key=34225f421585f1bbfa123e72317bd44a&p=1')
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


# id_list = GetBeerData()
# id_list.get_beer_data()

def get_ingredients_data():
    list_of_ids = [beer['id'] for beer in id_list.get_beer_data()]
    beers_and_ingredients = []
    for beer_id in list_of_ids:
        beer_ingredients = requests.get(f'http://api.brewerydb.com/v2/beer/{beer_id}/ingredients?key=34225f421585f1bbfa123e72317bd44a')
        ingredients = beer_ingredients.json()
        beer_ingredient_dict = {"beercode": beer_id, "beer_ingredients": ingredients}
        beers_and_ingredients.append(beer_ingredient_dict)
    return beers_and_ingredients


def ids_and_ingredients():
    ingr = []
    for i in get_ingredients_data():
        if i['beer_ingredients'].get('data'):
            just_data = i['beer_ingredients']['data']
            id_beer = i['beercode']
            ingr.append({'beercode':id_beer, 'data':just_data})
    return ingr


def beer_ingredient_ids():
    for beer in ids_and_ingredients():
        matched_beer = session.query(Beer).filter(Beer.beercode == beer['beercode'])[0]
        for ingredient in beer['data']:
            matched_ingredient = session.query(Ingredient).filter(Ingredient.ingredientcode == ingredient['id'])[0]
            matched_beer.ingredients.append(matched_ingredient)
