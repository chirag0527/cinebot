from utils.opensubtitles_client import fetch_subtitles
from utils.subtitle_parser import parse_subtitle, donwload_subtitle
from db.mongodb_client import MongoDBClient
import os, json

database = MongoDBClient("cinebot", "subtitles")

if __name__=="__main__":
    filename= "movies.json"
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            movies = json.load(f)
    else:
        print("File not found :(")
    
        
    



