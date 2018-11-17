from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, Text, Float, ForeignKey, create_engine
from sqlalchemy.orm import relationship

import sqlalchemy


class Style(Base):
    __tablename__ = 'styles'
    id = Column(Integer, primary_key = True)
    name = Column(Text, nullable = True)
    shortName = Column(Text, nullable = True)
    nameDisplay = Column(Text, nullable = True)
    category = Column(Text, nullable = True)
    description = Column(Text, nullable = True)
    abvMin = Column(Float, nullable = True)
    abvMax = Column(Float, nullable = True)
    ibuMin = Column(Float, nullable = True)
    ibuMax = Column(Float, nullable = True)
    beers = relationship('Beer', back_populates = 'style_shortName')

class Beer(Base):
    __tablename__ = 'beers'
    id = Column(Integer, primary_key = True)
    beercode = Column(Text, nullable = True)
    name = Column(Text, nullable = True)
    nameDisplay = Column(Text, nullable = True)
    description = Column(Text, nullable = True)
    abv = Column(Float, nullable = True)
    ibu = Column(Float, nullable = True)
    isOrganic = Column(Text, nullable = True)
    foodPairings = Column(Text, nullable = True)
    style = Column(Text)
    style_id = Column(Integer, ForeignKey('styles.id'))
    style_shortName = relationship('Style', back_populates = 'beers')
    ingredients = relationship('Ingredient', secondary = "beer_ingredients", back_populates = 'beers')

class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key = True)
    ingredientcode = Column(Integer, nullable = True)
    name = Column(Text, nullable = True)
    category = Column(Text, nullable = True)
    categoryDisplay = Column(Text, nullable = True)
    beers = relationship('Beer', secondary = "beer_ingredients", back_populates = 'ingredients')



class BeerIngredients(Base):
    __tablename__ = "beer_ingredients"
    beer_id = Column(Integer, ForeignKey('beers.id'), primary_key = True)
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'), primary_key = True)


engine = sqlalchemy.create_engine('sqlite:///beers.db', echo=True)
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
