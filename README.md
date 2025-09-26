## ⏱ Timeout API (FastAPI)

This is a simple FastAPI project that provides endpoints to simulate delayed responses.
It is useful for testing timeout handling in other projects and clients (Python, C#, Node.js, etc.).

## 🚀 Features

- **GET /fast** → Instant response.  
- **GET /slow/{seconds}** → Delayed response, delay specified in route (default is **10 seconds** if not provided).  
- **POST /slow/{seconds}** → Same as above but with POST method (default is **10 seconds** if not provided).  

If the client’s timeout is set shorter than {seconds}, the request will fail — perfect for simulating external API timeouts.

## 🛠️ Setup & Installation

You can run this project with Conda or plain Python + pip.

### 🔹 Option 1: Conda (recommended)

1. Create environment:
```bash
conda create -n timeout-api python=3.11 fastapi uvicorn
```
2. Activate environment:
```bash
conda activate timeout-api
```
3. Run server:
```bash
uvicorn app.main:app --reload --port 8000
```
### 🔹Option 2: Plain Python (pip)

1. Create virtual environment:
```
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run server:
```bash
uvicorn app.main:app --reload --port 8000
```
📦 Requirements

`requirements.txt`:
```
fastapi
uvicorn
```
### 📚 API Documentation

When the server is running:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## 🧪 Endpoints

| Method | Path              | Description                              | Example             |
|--------|-------------------|------------------------------------------|---------------------|
| GET    | `/fast`           | Instant response                         | `/fast`             |
| GET    | `/slow/{seconds}` | Waits `{seconds}` seconds before responding | `/slow/5` → waits 5s |
| POST   | `/slow/{seconds}` | Same as above, but POST method           | `/slow/10` → waits 10s |

### ✅ Example Usage
```bash
# Instant response
curl http://127.0.0.1:8000/fast

# Simulate 5 second delay
curl http://127.0.0.1:8000/slow/5

# Simulate 10 second delay with POST
curl -X POST http://127.0.0.1:8000/slow/10
```