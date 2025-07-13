from utils.opensubtitles_client import fetch_subtitles
from utils.subtitle_parser import parse_subtitle, donwload_subtitle
from db.mongodb_client import MongoDBClient
import os, json, time

database = MongoDBClient("cinebot", "subtitles")

if __name__=="__main__":
    filename= "movies.json"
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            movies = json.load(f)
    else:
        print("File not found :(")
    for movie in movies:
        try:
            time.sleep(5)
            print("Fetching Subtitles....")
            subtitle_url = fetch_subtitles(movie["id"])
            print(f"Subtitle url: {subtitle_url}")
            time.sleep(15) 
            print("Downloading Subtitles....")
            subtitle_file = donwload_subtitle(subtitle_url)
            time.sleep(10) 
            print(f"Subtitle file: {subtitle_file}")
            print("Parsing Subtitles....")
            subtitles = parse_subtitle(subtitle_file)
            for sub in subtitles:
                sub["title"] = movie["title"]
                sub["movie_id"] = movie["id"]
                print(f"Inserting into database")
                database.insert_one(sub)
                print("Data inserted successfully")
        except Exception as e:
            print(f"Error: {e}")

    
        
    



