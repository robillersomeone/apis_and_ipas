from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, Text, Float, ForeignKey, create_engine
from sqlalchemy.orm import relationship

class Style(Base):
    __tablename__ = 'styles'
    id = Column(Integer, primary_key = True)
    name = Column(Text, nullable = True)
    shortName = Column(Text, nullable = True)
    beers = relationship('Beer', back_populates = 'style_shortName')
    nameDisplay = Column(Text, nullable = True)
    category = Column(Text, nullable = True)
    description = Column(Text, nullable = True)
    abvMin = Column(Float, nullable = True)
    abvMax = Column(Float, nullable = True)
    ibuMin = Column(Float, nullable = True)
    ibuMax = Column(Float, nullable = True)

class Beer(Base):
    __tablename__ = 'beers'
    id = Column(Integer, primary_key = True)
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
