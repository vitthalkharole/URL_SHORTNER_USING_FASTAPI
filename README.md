# 🔗 URL Shortener App

A modern URL Shortener application built using **FastAPI**, **Streamlit**, **SQLAlchemy**, and **SQLite**.

The application allows users to convert long URLs into short, shareable links, view all generated URLs, and delete unwanted links through an easy-to-use Streamlit interface.

---

# 🚀 Features

✅ Generate Short URLs

✅ Redirect Short URL to Original Website

✅ View All Stored URLs

✅ Delete Short URLs

✅ SQLite Database Storage

✅ RESTful FastAPI Backend

✅ Interactive Streamlit Frontend

---

# 🛠 Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

### Frontend
- Streamlit
- Requests

### Database
- SQLite

---

# 📂 Project Structure

```
URL-Shortener/
│
├── main.py                 # FastAPI Application
├── api_service.py          # API Endpoints
├── database.py             # Database Connection
├── models.py               # SQLAlchemy Models
├── schemas.py              # Pydantic Schemas
├── urls.db                 # SQLite Database
├── .env
├── requirements.txt
│
├── streamlit_app.py        # Streamlit UI
│
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/url-shortener.git

cd url-shortener
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Mac/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run FastAPI

```bash
uvicorn main:app --reload
```

Backend runs at

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Streamlit

```bash
streamlit run streamlit_app.py
```

Streamlit Dashboard

```
http://localhost:8501
```

---

# 📌 API Endpoints

## Create Short URL

```
POST /url/shorten
```

Request

```json
{
    "original_url":"https://www.google.com"
}
```

Response

```json
{
   "original_url":"https://www.google.com",
   "short_code":"Ab12Cd",
   "short_url":"http://localhost:8000/Ab12Cd"
}
```

---

## Get All URLs

```
GET /url/all
```

Returns every shortened URL stored in the database.

---

## Redirect

```
GET /{short_code}
```

Automatically redirects the user to the original website.

Example

```
http://localhost:8000/Ab12Cd
```

---

## Delete URL

```
DELETE /url/delete/{short_code}
```

Deletes a shortened URL permanently.

---

# 💻 Streamlit Dashboard

The Streamlit application provides an intuitive interface to:

- Generate Short URLs
- View All URLs
- Open Short URLs
- Delete URLs
- Display Original URL
- Display Short URL
- Refresh Data

---

# 📷 Application Workflow

```
User
   │
   ▼
Streamlit UI
   │
HTTP Request
   ▼
FastAPI
   │
SQLAlchemy
   │
SQLite Database
   │
Response
   ▼
Streamlit UI
```

---

# 🗄 Database Schema

| Column | Type |
|---------|------|
| id | Integer |
| original_url | String |
| short_code | String |

---

# Example

Input

```
https://www.youtube.com/watch?v=12345
```

Generated

```
http://localhost:8000/A7Bc9D
```

Opening the short URL redirects to YouTube.

---

# Future Improvements

- User Authentication
- QR Code Generation
- Click Analytics
- URL Expiry
- Custom Short URLs
- Search URLs
- Copy Button
- Pagination
- Export URLs to CSV
- Dark Mode

---

# Requirements

- Python 3.10+
- FastAPI
- Streamlit
- SQLAlchemy
- SQLite
- Uvicorn

---

# Author

**Vitthal Kharole**

Computer Science Engineering Student

FastAPI • Python • SQL • Streamlit

---

# License

This project is developed for educational and portfolio purposes.