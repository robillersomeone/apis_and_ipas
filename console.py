from beer_and_styles import Beer, Style, Base
from get_data import GetBeerData, BeerBuilder, StyleBuilder
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///beers.db', echo=True)

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

beer = BeerBuilder.run()
styles = StyleBuilder.run()
session.add_all(beer)
session.add_all(styles)
