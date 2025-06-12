import requests
from config import OPENSUB_API_KEY

HEADERS = {
    "User-Agent": "Cinebot v1.0",
    "Api-Key": OPENSUB_API_KEY
}

def fetch_subtitles(movie_id: int):
    search_url = f"https://api.opensubtitles.com/api/v1/subtitles?tmdb_id={movie_id}"
    response = requests.get(search_url, headers=HEADERS)
    response = response.json()
    #response.data is a list of dictionaries, we need to get the files.file_id where attributes.language is "es"
    file_id = ""
    for file in response["data"]:
        if file["attributes"]["language"] == "en":
            file_id = file["attributes"]["files"][0]["file_id"]
            break
    if file_id == "":
        raise Exception("No subtitles found for the movie")
    download_url = f"https://api.opensubtitles.com/api/v1/download?file_id={file_id}"
    response = requests.post(download_url, headers=HEADERS)
    response = response.json()
    return response["link"]

if __name__=="__main__":
    print(fetch_subtitles(550))