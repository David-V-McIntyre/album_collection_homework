import pdb 
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Los Campesinos!")
artist_repository.save(artist_1)

artist_2 = Artist("Blur")
artist_repository.save(artist_2)

album_1 = Album("Hello Sadness", artist_1, "indie-pop")
album_repository.save(album_1)
album_2 = Album("Hold On Now, Youngster...", artist_1, "indie-pop")
album_repository.save(album_2)
album_3 = Album("Parklife", artist_2, "britpop")
album_repository.save(album_3)
album_4 = Album("Modern Life Is Rubbish", artist_2, "britpop")
album_repository.save(album_4)


for artist in artist_repository.select_all():
    print(artist.__dict__)

for album in album_repository.select_all():
    print(album.__dict__)