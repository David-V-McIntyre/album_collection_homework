import pdb 
from models.artist import Artist
import repositories.artist_repository as artist_repository

artist_1 = Artist("Los Campesinos!")
artist_repository.save(artist_1)

