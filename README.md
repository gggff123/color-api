# 🎨 Color Mood ML API

> Predict emotional moods from colors, generate palettes, check contrast, and explore color relationships — powered by machine learning.

---

## ✨ Features

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | `GET` | Health check |
| `/predict` | `POST` | Predict the mood/emotion of a color |
| `/similar` | `POST` | Generate visually similar color variations |
| `/palette` | `POST` | Generate a color palette from a base color |
| `/contrast` | `POST` | Check contrast ratio between two colors |

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/color-mood-ml-api.git
cd color-mood-ml-api
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the API

```bash
uvicorn main:app --reload
```

The API will be live at `http://localhost:8000`

---

## 📡 API Reference

### `GET /`
Returns a simple health check message.

**Response**
```json
{
  "message": "Color Mood ML API running 🎨"
}
```

---

### `POST /predict`
Predicts the emotional mood associated with a hex color using a KNN classifier.

**Request Body**
```json
{
  "hex": "#FF0000"
}
```

**Response**
```json
{
  "color": "#FF0000",
  "rgb": [255, 0, 0],
  "mood": "energetic",
  "confidence": 1.0
}
```

**Mood Labels**

| Color Family | Mood |
|---|---|
| 🔴 Red | `energetic` |
| 🟢 Green | `calm` |
| 🔵 Blue | `trust` |
| 🟡 Yellow | `happy` |
| 🟣 Purple | `creative` |
| 🟠 Orange | `excited` |
| 🩵 Cyan | `refreshing` |
| 🩷 Pink | `romantic` |

---

### `POST /similar`
Returns 5 color variations close to the input color.

**Request Body**
```json
{
  "hex": "#3A7BD5"
}
```

**Response**
```json
{
  "base_color": "#3A7BD5",
  "similar_colors": ["#2f6fcb", "#4585d9", "#3370c2", "#4180d8", "#376ed0"]
}
```

---

### `POST /palette`
Generates a 5-color palette inspired by the input color.

**Request Body**
```json
{
  "hex": "#8E44AD"
}
```

**Response**
```json
{
  "base_color": "#8E44AD",
  "palette": ["#a35bc4", "#7230a1", "#b468d8", "#6e2d9f", "#9a4fba"]
}
```

---

### `POST /contrast`
Checks the contrast between two colors and returns a rating.

**Request Body**
```json
{
  "color1": "#FFFFFF",
  "color2": "#000000"
}
```

**Response**
```json
{
  "color1": "#FFFFFF",
  "color2": "#000000",
  "contrast_score": 441.67,
  "rating": "excellent"
}
```

**Contrast Ratings**

| Score | Rating |
|---|---|
| > 200 | `excellent` |
| 120 – 200 | `good` |
| < 120 | `low` |

---

## 🛠 Tech Stack

- **[FastAPI](https://fastapi.tiangolo.com/)** — Modern async web framework
- **[scikit-learn](https://scikit-learn.org/)** — KNN-based mood classification
- **[NumPy](https://numpy.org/)** — Color math and vector operations
- **[Uvicorn](https://www.uvicorn.org/)** — ASGI server

---

## 📁 Project Structure

```
color-mood-ml-api/
├── main.py           # FastAPI application & ML model
├── requirements.txt  # Python dependencies
└── README.md         # You are here
```

---

## 📖 Interactive Docs

Once running, visit the auto-generated docs:

- **Swagger UI** → [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc** → [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 📄 License

MIT © 2024
