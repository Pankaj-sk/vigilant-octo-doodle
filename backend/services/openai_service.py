import openai
from config import OPENAI_API_KEY

class OpenAIService:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY

    def analyze_theme(self, content):
        """
        Analyze the content and return theme, mood, and suitable audio type
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "Analyze the following content and determine its theme, mood, and suitable audio content type (music/podcast). Return the response in JSON format with keys: theme, mood, audio_type"
                    },
                    {
                        "role": "user",
                        "content": content
                    }
                ]
            )
            
            # Parse the response to get structured data
            analysis = response.choices[0].message.content
            return {
                "theme": analysis.get("theme", ""),
                "mood": analysis.get("mood", ""),
                "audio_type": analysis.get("audio_type", "music")
            }
        except Exception as e:
            print(f"Error in OpenAI analysis: {str(e)}")
            return {
                "theme": "general",
                "mood": "neutral",
                "audio_type": "music"
            } 