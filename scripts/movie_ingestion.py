import requests
import json
import os
from config import TMDB_BEARER_TOKEN

def get_movies(page=1):
    url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page={page}&sort_by=vote_average.desc&without_genres=99,10755&vote_count.gte=200"

    headers = {
        "User-Agent": "Postman/7.44.0",
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_BEARER_TOKEN}"
    }

    response = requests.get(url, headers=headers)
    return response.json()["results"]

if __name__ == "__main__":
    filename = "movies.json"

    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            all_movies = json.load(f)
    else:
        all_movies = []

    new_movies = []
    for movie in get_movies(page=7): 
        if movie["original_language"] == "en":
            new_movies.append({
                "title": movie["original_title"],
                "id": movie["id"]
            })

    all_movies.extend(new_movies)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(all_movies, f, indent=2, ensure_ascii=False)

    print(f"Appended {len(new_movies)} new movies to {filename}")
