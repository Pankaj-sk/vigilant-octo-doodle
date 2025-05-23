# Theme-Based Audio Player Chrome Extension

A Chrome extension that analyzes webpage content and plays contextually relevant audio content from Spotify.

## Features

- Analyzes webpage content using OpenAI's GPT model
- Determines theme, mood, and suitable audio type
- Searches and plays relevant music/podcasts from Spotify
- Provides audio player controls in a popup interface
- Supports volume control and track navigation

## Prerequisites

- Python 3.7+
- Node.js and npm
- Chrome browser
- OpenAI API key
- Spotify Developer account and API credentials

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd project
```

2. Set up the Python backend:
```bash
cd backend
pip install -r requirements.txt
```

3. Create a `.env` file in the backend directory with your API keys:
```
OPENAI_API_KEY=your_openai_api_key
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
```

4. Start the backend server:
```bash
python app.py
```

5. Load the Chrome extension:
- Open Chrome and go to `chrome://extensions/`
- Enable Developer mode
- Click "Load unpacked"
- Select the `chrome_extension` directory

## Usage

1. Visit any webpage
2. Click the extension icon in Chrome
3. The extension will:
   - Analyze the page content
   - Display the theme and mood
   - Show recommended audio content
   - Start playing the first recommendation

4. Use the popup controls to:
   - Play/pause audio
   - Skip to next track
   - Adjust volume
   - View and select from recommendations

## Development

### Backend Structure
- `app.py`: Main Flask application
- `services/`: API integration services
- `utils/`: Helper functions and utilities

### Extension Structure
- `popup/`: Extension popup interface
- `content/`: Content script for page analysis
- `background/`: Background script for extension management

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for the GPT API
- Spotify for the Web API
- Chrome Extension APIs 