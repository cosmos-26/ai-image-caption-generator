from fastapi import FastAPI, UploadFile, File, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from google import genai
from PIL import Image
from dotenv import load_dotenv
import tempfile
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

app = FastAPI()

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/generate")
async def generate(image: UploadFile = File(...)):

    temp_path = None

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp:
            temp.write(await image.read())
            temp_path = temp.name

        img = Image.open(temp_path)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                img,
                """
Generate the following:

1. Formal Caption
2. Casual Caption
3. SEO Caption (15-25 words)
4. Alt Text (under 125 characters)

Return EXACTLY in this format:

Formal:
...

Casual:
...

SEO:
...

Alt Text:
...
"""
            ]
        )

        return {
            "result": response.text
        }

    except Exception as e:
        return {
            "error": str(e)
        }

    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)