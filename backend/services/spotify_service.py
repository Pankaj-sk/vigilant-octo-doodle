import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import (
    SPOTIFY_CLIENT_ID,
    SPOTIFY_CLIENT_SECRET,
    SPOTIFY_REDIRECT_URI,
    SPOTIFY_SCOPE
)

class SpotifyService:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET,
            redirect_uri=SPOTIFY_REDIRECT_URI,
            scope=SPOTIFY_SCOPE
        ))

    def search_content(self, theme, audio_type="track", limit=5):
        """
        Search for content based on theme and audio type
        """
        try:
            if audio_type == "podcast":
                results = self.sp.search(q=theme, limit=limit, type='show')
                return results['shows']['items']
            else:
                results = self.sp.search(q=theme, limit=limit, type='track')
                return results['tracks']['items']
        except Exception as e:
            print(f"Error in Spotify search: {str(e)}")
            return []

    def play_content(self, uri):
        """
        Play the selected content
        """
        try:
            self.sp.start_playback(uris=[uri])
            return True
        except Exception as e:
            print(f"Error in Spotify playback: {str(e)}")
            return False

    def pause_playback(self):
        """
        Pause the current playback
        """
        try:
            self.sp.pause_playback()
            return True
        except Exception as e:
            print(f"Error in Spotify pause: {str(e)}")
            return False

    def resume_playback(self):
        """
        Resume the current playback
        """
        try:
            self.sp.start_playback()
            return True
        except Exception as e:
            print(f"Error in Spotify resume: {str(e)}")
            return False

    def set_volume(self, volume_percent):
        """
        Set the playback volume
        """
        try:
            self.sp.volume(volume_percent)
            return True
        except Exception as e:
            print(f"Error in Spotify volume control: {str(e)}")
            return False 