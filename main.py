from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

app = FastAPI(title="Color Mood ML API")


# ---------------------
# Training Data
# ---------------------

colors = np.array([
    [255,0,0],
    [0,255,0],
    [0,0,255],
    [255,255,0],
    [128,0,128],
    [255,165,0],
    [0,255,255],
    [255,192,203]
])

labels = [
    "energetic",
    "calm",
    "trust",
    "happy",
    "creative",
    "excited",
    "refreshing",
    "romantic"
]

model = KNeighborsClassifier(n_neighbors=1)
model.fit(colors, labels)


# ---------------------
# Models
# ---------------------

class ColorInput(BaseModel):
    hex: str


class ContrastInput(BaseModel):
    color1: str
    color2: str


# ---------------------
# Utils
# ---------------------

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return [int(hex_color[i:i+2],16) for i in (0,2,4)]


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % tuple(rgb)


# ---------------------
# Routes
# ---------------------

@app.get("/")
def home():
    return {"message":"Color Mood ML API running 🎨"}


# ---------------------
# Mood Prediction
# ---------------------

@app.post("/predict")
def predict_color_mood(data: ColorInput):

    rgb = hex_to_rgb(data.hex)

    prediction = model.predict([rgb])[0]
    confidence = model.predict_proba([rgb]).max()

    return {
        "color": data.hex,
        "rgb": rgb,
        "mood": prediction,
        "confidence": float(confidence)
    }


# ---------------------
# Similar Colors
# ---------------------

@app.post("/similar")
def similar_colors(data: ColorInput):

    rgb = np.array(hex_to_rgb(data.hex))

    variations = []

    for i in range(5):
        noise = np.random.randint(-40,40,3)
        new = np.clip(rgb + noise,0,255)
        variations.append(rgb_to_hex(new))

    return {
        "base_color": data.hex,
        "similar_colors": variations
    }


# ---------------------
# Palette Generator
# ---------------------

@app.post("/palette")
def generate_palette(data: ColorInput):

    rgb = np.array(hex_to_rgb(data.hex))

    palette = []

    for i in range(5):
        shift = np.random.randint(-80,80,3)
        new = np.clip(rgb + shift,0,255)
        palette.append(rgb_to_hex(new))

    return {
        "base_color": data.hex,
        "palette": palette
    }


# ---------------------
# Contrast Checker
# ---------------------

@app.post("/contrast")
def contrast(data: ContrastInput):

    rgb1 = np.array(hex_to_rgb(data.color1))
    rgb2 = np.array(hex_to_rgb(data.color2))

    diff = np.linalg.norm(rgb1 - rgb2)

    rating = "low"
    if diff > 200:
        rating = "excellent"
    elif diff > 120:
        rating = "good"

    return {
        "color1": data.color1,
        "color2": data.color2,
        "contrast_score": float(diff),
        "rating": rating
    }
