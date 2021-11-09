from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

def save(artist):
    sql = f"INSERT INTO artists (artist_name) VALUES (%s) RETURNING *"
    values = [artist.artist_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist