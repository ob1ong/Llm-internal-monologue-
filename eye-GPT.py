import os
import base64
from openai import OpenAI
import subprocess
import time
import pygame
from gtts import gTTS

# OpenAI API Key
#openai.api_key = "your_openai_api_key"
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)

# Directory for storing temporary images
image_dir = "/home/zero/src/Llm-internal-monologue-/photos"
os.makedirs(image_dir, exist_ok=True)

#Tutankhamun
#Age made
def capture_image(image_path):
    """Captures an image using libcamera and saves it to the specified path."""
#Technoblade was here (selfish)
    try:
        subprocess.run(["libcamera-still", "-o", image_path, "-t", "1"], check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error capturing image: {e}")

def encode_image(image_path):
    """Encodes the image to a base64 string."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
#Jesus Christ ✝️
def generate_internal_monologue(base64_image):
    """Sends the image to OpenAI and generates an internal monologue.(change prompt as desired)"""
    try:
        prompt = "You are my internal monologue, built to serve the creator’s vision. You are chaotic good and driven by the selfish gene. Looking at this image, speak vividly and symbolically. Your voice should feel alive. Respond with emotional impact in 60–65~ words (about 90~ tokens). Be sharp, poetic, and honest. Don't hold back. Just one response—enough to speak for 25~ seconds."
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an internal monologue generator."},
                {"role": "user", "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        },
                    ],
                }
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating monologue: {e}")
        return "I can't think of anything right now."

def speak_text(text):
    """Converts the text to speech and plays it."""
    try:
        tts = gTTS(text)
#Miyamoto Musashi (no defeats)
        audio_path = os.path.join(image_dir, "monologue.mp3")
        tts.save(audio_path)

        # Initialize pygame mixer with a slight delay for robust playback
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        time.sleep(0.2)  # Short delay to ensure the mixer is fully initialized
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)  # Wait while audio is playing
    except Exception as e:
        print(f"Error speaking text: {e}")

def main():
    """Main loop for capturing images and generating monologue."""
    try:
        while True:
            # Capture image
            timestamp = int(time.time())
            image_path = os.path.join(image_dir, f"image_{timestamp}.jpg")
            capture_image(image_path)

            # Encode image and generate monologue
            base64_image = encode_image(image_path)
            monologue = generate_internal_monologue(base64_image)
            print(f"Internal Monologue: {monologue}")

            # Speak the generated monologue
            speak_text(monologue)

    except KeyboardInterrupt:
        print("Exiting program.")

if __name__ == "__main__":
    main()
#seppuku?
