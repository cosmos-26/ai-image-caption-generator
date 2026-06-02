#  AI Image Caption Generator

An AI-powered web application that generates multiple types of captions from uploaded images using Google's Gemini Vision model.

## Features

*  Upload images through a simple web interface
*  Generate Formal Captions
*  Generate Casual Captions
*  Generate SEO-Friendly Captions
*  Generate Accessibility-Friendly Alt Text
*  Modern responsive UI with a pink-blush theme
*  FastAPI backend with Gemini Vision integration

## Tech Stack

### Backend

* FastAPI
* Python
* Google Gemini 2.5 Flash
* Pillow (Image Processing)

### Frontend

* HTML
* CSS
* JavaScript

### Other Tools

* Jinja2 Templates
* Python Dotenv

## Project Structure

```text
ai-caption-generator/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── .env
```

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-image-caption-generator.git
cd ai-image-caption-generator
```
## Live Demo

https://ai-image-caption-generator-8nfw.onrender.com/

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

## Running the Application

```bash
uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

## How It Works

1. User uploads an image.
2. FastAPI receives the image.
3. The image is sent to Google's Gemini Vision model.
4. Gemini analyzes the image and generates:

   * Formal Caption
   * Casual Caption
   * SEO Caption
   * Alt Text
5. Results are displayed on the webpage.

## Example Output

**Formal:**
A tri-color dog runs energetically along a sunny beach, splashing through shallow water.

**Casual:**
Look at this happy pup having the best day ever at the beach!

**SEO:**
Happy dog running on a sunny beach with ocean waves, playful pet enjoying outdoor summer activities.

**Alt Text:**
Tri-color dog running through shallow beach water on a sunny day.

## Future Improvements

* Download captions as TXT/PDF
* Copy-to-clipboard feature
* Multiple caption styles
* Social media caption generation
* Image preview before upload
* Deployment on Render



Built as part of an AI Engineering internship assignment using FastAPI and Google Gemini Vision.
