import os
import base64
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

# Initialize Flask app
app = Flask(__name__)

# Load environment variables from .env
load_dotenv()

# Convert image file to base64 string
def convert_image_to_base64(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode('utf-8')

@app.route('/', methods=['GET', 'POST'])
def homepage():
    hashtags = None
    image_data_url = None

    if request.method == 'POST':
        uploaded_file = request.files['image']
        saved_path = "static/user_upload.jpg"
        uploaded_file.save(saved_path)

        image_base64 = convert_image_to_base64(saved_path)
        image_data_url = f"data:image/jpeg;base64,{image_base64}"

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('OPENAI_KEY')}"
        }

        prompt_payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are a hashtag generation model. "
                        "When given an image, respond with exactly 30 hashtags, separated by commas."
                    )
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Generate hashtags for this image:"},
                        {"type": "image_url", "image_url": {"url": image_data_url}}
                    ]
                }
            ],
            "max_tokens": 300
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=prompt_payload)
        hashtags_text = response.json()["choices"][0]["message"]["content"]
        hashtags = [tag.strip() for tag in hashtags_text.split(',')]

    return render_template('index.html', hashtags=hashtags, image_data=image_data_url)

if __name__ == '__main__':
    app.run(debug=True)
