import array
from app import db, Artist

artist_1 = Artist(name="Guns N Petals")

artist_1.genres = ["Rock n Roll"]
artist_1.city = "San Francisco"
artist_1.state = "CA"
artist_1.phone = "326-123-5000"
artist_1.website = "https://www.gunsnpetalsband.com"
artist_1.facebook_link = "https://www.facebook.com/GunsNPetals"
artist_1.seeking_venue = True
artist_1.seeking_description = "Looking for shows to perform at in the San Francisco Bay Area!"
artist_1.image_link = "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80"

artist_2 = Artist(name="Matt Quevedo")
artist_2.genres = ["Jazz"]
artist_2.city = "New York"
artist_2.state = "NY"
artist_2.phone = "300-400-5000"
artist_2.facebook_link = "https://www.facebook.com/mattquevedo923251523"
artist_2.seeking_venue = False
artist_2.image_link = "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80"

artist_3 = Artist(name="The Wild Sax Band")
artist_3.genres = ["Jazz", "Classical"]
artist_3.city = "San Francisco"
artist_3.state = "CA"
artist_3.phone = "432-325-5432"
artist_3.seeking_venue = False
artist_3.image_link = "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80"


db.session.add_all([artist_1, artist_2, artist_3])
try:
    db.session.commit()
except:
    db.session.roll_back()
finally:
    db.session.close()
