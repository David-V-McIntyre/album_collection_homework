from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

def save(album):
    sql = f"INSERT INTO albums (album_name) VALUES (%s) RETURNING *"
    values = [album.album_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return album