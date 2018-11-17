# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()
# from sqlalchemy import db.Column,db. Integer, Text, Float, ForeignKey, create_engine
# from sqlalchemy.orm import relationship
from dash_package import db

class Style(db.Model):
    __tablename__ = 'styles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable = True)
    shortName = db.Column(db.Text, nullable = True)
    nameDisplay = db.Column(db.Text, nullable = True)
    category = db.Column(db.Text, nullable = True)
    description = db.Column(db.Text, nullable = True)
    abvMin = db.Column(db.Float, nullable = True)
    abvMax = db.Column(db.Float, nullable = True)
    ibuMin = db.Column(db.Float, nullable = True)
    ibuMax = db.Column(db.Float, nullable = True)
    beers = db.relationship('Beer', back_populates = 'style_shortName')

class Beer(db.Model):
    __tablename__ = 'beers'
    id = db.Column(db.Integer, primary_key = True)
    beercode = db.Column(db.Text, nullable = True)
    name = db.Column(db.Text, nullable = True)
    nameDisplay = db.Column(db.Text, nullable = True)
    description = db.Column(db.Text, nullable = True)
    abv = db.Column(db.Float, nullable = True)
    ibu = db.Column(db.Float, nullable = True)
    isOrganic = db.Column(db.Text, nullable = True)
    foodPairings = db.Column(db.Text, nullable = True)
    style = db.Column(db.Text)
    style_id = db.Column(db.Integer, db.ForeignKey('styles.id'))
    style_shortName = db.relationship('Style', back_populates = 'beers')
    ingredients = db.relationship('Ingredient', secondary = "beer_ingredients", back_populates = 'beers')

class Ingredient(db.Model):
    __tablename__ = 'ingredients'
    id = db.Column(db.Integer, primary_key = True)
    ingredientcode = db.Column(db.Integer, nullable = True)
    name = db.Column(db.Text, nullable = True)
    category = db.Column(db.Text, nullable = True)
    categoryDisplay = db.Column(db.Text, nullable = True)
    beers = db.relationship('Beer', secondary = "beer_ingredients", back_populates = 'ingredients')



class BeerIngredients(db.Model):
    __tablename__ = "beer_ingredients"
    beer_id = db.Column(db.Integer, db.ForeignKey('beers.id'), primary_key = True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.id'), primary_key = True)
