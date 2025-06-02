# Hashtag AI Generator

This is a simple Flask web app that uses OpenAI's GPT-4o model to generate 30 hashtags based on an uploaded image. Just upload an image, and the app will suggest hashtags you can copy and use for social media or marketing.

## Features

- Upload an image and get AI-generated hashtags
- Live image preview before submission
- Click-to-select hashtags
- Copy selected hashtags to a text area

## Tech Stack

- Python (Flask)
- HTML / CSS / JavaScript
- OpenAI API
- Jinja2 Templating

## Setup

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Create a `.env` file and add your OpenAI API key:
```bash
OPENAI_KEY=your_api_key_here
```
4. Run the app:

5. Open your browser and go to `http://localhost:5000`

## Notes

- Make sure your API key has access to GPT-4o.
- Uploaded images are saved temporarily during processing.

## License

MIT License
