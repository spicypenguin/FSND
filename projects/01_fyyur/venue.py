import array
from app import db, Venue

venue_1 = Venue(name="The Musical Hop")
venue_1.genres = ["Jazz", "Reggae", "Swing", "Classical", "Folk"]
venue_1.address = "1015 Folsom Street"
venue_1.city = "San Francisco"
venue_1.state = "CA"
venue_1.phone = "123-123-1234"
venue_1.website = "https://www.themusicalhop.com"
venue_1.facebook_link = "https://www.facebook.com/TheMusicalHop"
venue_1.seeking_talent = True
venue_1.seeking_description = "We are on the lookout for a local artist to play every two weeks. Please call us."
venue_1.image_link = "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60"

venue_2 = Venue(name="The Dueling Pianos Bar")
venue_2.genres = ["Classical", "R&B", "Hip-Hop"]
venue_2.address = "335 Delancey Street"
venue_2.city = "New York"
venue_2.state = "NY"
venue_2.phone = "914-003-1132"
venue_2.website = "https://www.theduelingpianos.com"
venue_2.facebook_link = "https://www.facebook.com/theduelingpianos"
venue_2.seeking_talent = False
venue_2.image_link = "https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80"


venue_3 = Venue(name="Park Square Live Music & Coffee")
venue_3.genres = ["Rock n Roll", "Jazz", "Classical", "Folk"]
venue_3.address = "34 Whiskey Moore Ave"
venue_3.city = "San Francisco"
venue_3.state = "CA"
venue_3.phone = "415-000-1234"
venue_3.website = "https://www.parksquarelivemusicandcoffee.com"
venue_3.facebook_link = "https://www.facebook.com/ParkSquareLiveMusicAndCoffee"
venue_3.seeking_talent = False
venue_3.image_link = "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80"

db.session.add_all([venue_1, venue_2, venue_3])
try:
    db.session.commit()
except:
    db.session.roll_back()
finally:
    db.session.close()
