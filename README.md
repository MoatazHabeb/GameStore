# 🎮 Game Store API

A RESTful Game Store API built with **FastAPI**, **SQLAlchemy**, and **Oracle Database**. The project provides secure authentication using JWT, role-based authorization, game management, and order management.

---

## 🚀 Features

- 🔐 JWT Authentication
- 👥 Role-Based Authorization (Admin & Client)
- 👤 User Management
- 🎮 Game CRUD Operations
- 🛒 Order Creation with Multiple Items
- 💰 Automatic Total Price Calculation
- 🔒 Password Hashing with Passlib & Bcrypt
- 📖 Interactive API Documentation (Swagger)

---

## 🛠️ Technologies Used

- Python 3
- FastAPI
- SQLAlchemy
- Oracle Database
- Pydantic
- JWT Authentication
- OAuth2 Password Bearer
- Passlib
- Uvicorn

---

## 📂 Project Structure

```
GameStore/
│
├── game/
│   ├── repository/
│   ├── routers/
│   ├── database.py
│   ├── hashing.py
│   ├── jwt_handler.py
│   ├── models.py
│   ├── oauth.py
│   ├── schemas.py
│   └── ...
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🔐 Authentication

Login using:

```
POST /login
```

Example Response:

```json
{
    "access_token": "your_jwt_token",
    "token_type": "bearer",
    "role": "admin"
}
```

Use the token in the Authorization header:

```
Bearer YOUR_TOKEN
```

---

## 👥 Roles

### Admin

- Create Games
- Update Games
- Delete Games
- View All Orders
- Delete Orders

### Client

- Login
- View Games
- Create Orders
- View Order Details

---

## 📚 API Endpoints

### Authentication

| Method | Endpoint |
|---------|----------|
| POST | `/login` |

### Users

| Method | Endpoint |
|---------|----------|
| POST | `/users` |
| GET | `/users` |
| GET | `/users/{id}` |
| PUT | `/users/{id}` |
| DELETE | `/users/{id}` |

### Games

| Method | Endpoint |
|---------|----------|
| POST | `/games` |
| GET | `/games` |
| GET | `/games/{id}` |
| PUT | `/games/{id}` |
| DELETE | `/games/{id}` |

### Orders

| Method | Endpoint |
|---------|----------|
| POST | `/orders` |
| GET | `/orders` |
| GET | `/orders/{id}` |
| DELETE | `/orders/{id}` |

---

## 📦 Example Order Request

```json
{
  "items": [
    {
      "game_id": 1,
      "quantity": 2
    },
    {
      "game_id": 3,
      "quantity": 1
    }
  ]
}
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/MoatazHabeb/GameStore.git
```

Move into the project:

```bash
cd GameStore
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
uvicorn main:app --reload
```

---

## 📖 API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## 🔮 Future Improvements

- Shopping Cart
- Order History
- Payment Integration
- Game Categories
- Search & Filtering
- Pagination
- Refresh Tokens
- Unit Testing
- Docker Support

---

## 👨‍💻 Author

**Moataz Mohamed**

Backend Developer

- Java Backend Developer
- Python FastAPI Developer
