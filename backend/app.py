from flask import Flask, request, jsonify
from flask_cors import CORS
from services.openai_service import OpenAIService
from services.spotify_service import SpotifyService
from config import FLASK_HOST, FLASK_PORT, FLASK_DEBUG

app = Flask(__name__)
CORS(app)

# Initialize services
openai_service = OpenAIService()
spotify_service = SpotifyService()

@app.route('/analyze', methods=['POST'])
def analyze_content():
    """
    Analyze webpage content and return theme analysis
    """
    try:
        content = request.json.get('content')
        if not content:
            return jsonify({"error": "No content provided"}), 400

        analysis = openai_service.analyze_theme(content)
        return jsonify(analysis)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/search_audio', methods=['POST'])
def search_audio():
    """
    Search for audio content based on theme
    """
    try:
        theme = request.json.get('theme')
        audio_type = request.json.get('audio_type', 'track')
        
        if not theme:
            return jsonify({"error": "No theme provided"}), 400

        results = spotify_service.search_content(theme, audio_type)
        return jsonify({"results": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/play', methods=['POST'])
def play_audio():
    """
    Play selected audio content
    """
    try:
        uri = request.json.get('uri')
        if not uri:
            return jsonify({"error": "No URI provided"}), 400

        success = spotify_service.play_content(uri)
        return jsonify({"success": success})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/pause', methods=['POST'])
def pause_audio():
    """
    Pause current playback
    """
    try:
        success = spotify_service.pause_playback()
        return jsonify({"success": success})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/resume', methods=['POST'])
def resume_audio():
    """
    Resume current playback
    """
    try:
        success = spotify_service.resume_playback()
        return jsonify({"success": success})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/volume', methods=['POST'])
def set_volume():
    """
    Set playback volume
    """
    try:
        volume = request.json.get('volume')
        if volume is None:
            return jsonify({"error": "No volume provided"}), 400

        success = spotify_service.set_volume(volume)
        return jsonify({"success": success})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG) 