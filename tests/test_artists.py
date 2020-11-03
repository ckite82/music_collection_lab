import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):

    def setUp(self):
        self.artist = Artist("Simply Red", 55)

    def test_artist_has_name(self):
        self.assertEqual("Simply Red", self.artist.name)

    def test_artist_has_age(self):
        self.assertEqual(55, self.artist.age)