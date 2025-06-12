from dotenv import load_dotenv
import os

load_dotenv()

TMDB_BEARER_TOKEN = os.getenv("TMDB_BEARER_TOKEN")
OPENSUB_API_KEY = os.getenv("OPENSUB_API_KEY")
MONGODB_URI = os.getenv("MONGODB_URI")