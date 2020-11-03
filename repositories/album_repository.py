from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist
from repositories import artist_repository

def save(album):         # artist was called artist_id (its named artist in sql)
    sql = "INSERT INTO albums (name, artist, genre) VALUES (%s, %s, %s) RETURNING *;"
    values = [album.name, album.artist.id, album.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def select_all():
    albums = []

    sql = "SELECT * FROM albums;"
    results = run_sql(sql)

    for row in results:
        # artist = artist_repository.select(row['user_id'])
        album = Album(row['name'], row['artist'], row['genre'] , row['id'])
        albums.append(album)
    return albums

def delete_all():
    sql = "DELETE  FROM albums" 
    run_sql(sql)