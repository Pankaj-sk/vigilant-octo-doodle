import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

# Flask settings
FLASK_HOST = 'localhost'
FLASK_PORT = 5000
FLASK_DEBUG = True

# Spotify settings
SPOTIFY_REDIRECT_URI = f'http://{FLASK_HOST}:{FLASK_PORT}/callback'
SPOTIFY_SCOPE = 'user-modify-playback-state user-read-playback-state' 