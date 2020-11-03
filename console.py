import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

## swap these 2, delete albums before artist

artist = Artist("Simply Red", 55)
artist2 = Artist("Barbera", 17)
artist3 = Artist("Bob", 12)
album = Album("Complexly Black", artist, "pop")
album2 = Album("Convex", artist, "classical")
album3 = Album("Little by little", artist2, "jazz")
album4 = Album("High Life", artist3, "pop")

artist_repository.save(artist)
artist_repository.save(artist2)
artist_repository.save(artist3)
album_repository.save(album)
album_repository.save(album2)
album_repository.save(album3)
album_repository.save(album4)
