from get_data import session


#def food_pairings(session):
#    return session.query(Beer.name, Beer.foodPairings).where(Beer.foodPairings != None).all()

#print(session.query(Beer.name, Beer.foodPairings).filter(Beer.foodPairings != None).all())

def food_pairings():
    return session.query(Beer.name, Beer.foodPairings).filter(Beer.foodPairings != None).all()




print(food_pairings())
