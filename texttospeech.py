import requests
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment

PIXABAY_API_KEY = "45755073-58ae2520687e531ffe10333a8"
PIXABAY_API_URL = "https://pixabay.com/api/"

def get_pixabay_media(query, media_type='photo'):
    """
    Fetch media from Pixabay API based on the query and media type.

    Args:
    - query (str): The search query for the media.
    - media_type (str): The type of media to fetch (e.g., 'photo' or 'video').

    Returns:
    - dict: JSON response from Pixabay API or None if there was an error.
    """
    url = f"{PIXABAY_API_URL}?key={PIXABAY_API_KEY}&q={query}&image_type={media_type}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data from Pixabay")
        return None

def text_to_speech(text):
    """
    Convert text to speech using gTTS and return the audio as an AudioSegment.

    Args:
    - text (str): The text to convert to speech.

    Returns:
    - AudioSegment: The audio segment with the synthesized speech.
    """
    tts = gTTS(text)
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    audio = AudioSegment.from_file(audio_fp, format="mp3")
    return audio

def main():
    query = "nature"
    media_type = "photo"
    media_data = get_pixabay_media(query, media_type)
    if media_data:
        print("Pixabay Media Data:")
        print(media_data)

    text = "Hello, this is a test of the text to speech function."
    audio = text_to_speech(text)
    output_filename = 'output.mp3'
    audio.export(output_filename, format='mp3')
    print(f'Audio content saved to file "{output_filename}"')

if __name__ == "__main__":
    main()
