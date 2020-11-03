from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist
from repositories import album_repository

def save(artist):
    sql = "INSERT INTO artists (name, age) VALUES (%s, %s) RETURNING *;"
    values = [artist.name, artist.age]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def select_all():
    artists = []

    sql = "SELECT * FROM artsits;"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['name'], row['age'], row['id'])
        artists.append(artist)
    return artists

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s;"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = Artist(result['name'], result['age'], result['id'])
    return artist

def get_albums(artist):
    albums = []
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]
    result = run_sql(sql, values)

    for row in result:
        album = Album(row['name'], row['artist'], row['genre'], row['id'])
        albums.append(album)
    return albums

def delete_all():
    sql = "DELETE  FROM artists" 
    run_sql(sql)