import unittest
from models.album import Album
from models.artist import Artist

class TestAlbum(unittest.TestCase):

    def setUp(self):
        self.artist = Artist("Simply Red", 55)
        self.album = Album("Complexly Black", self.artist, "pop")

    def test_album_has_name(self):
        self.assertEqual("Complexly Black", self.album.name)

    def test_album_has_artist(self):
        self.assertEqual(55, self.album.artist.age)

    def test_album_has_genre(self):
        self.assertEqual("pop", self.album.genre)