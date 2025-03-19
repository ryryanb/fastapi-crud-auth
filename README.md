# **FastAPI CRUD & JWT Authentication with Redis**  
A **FastAPI** project implementing **CRUD operations** with **JWT authentication** and **Redis caching**.  

## **🚀 Features**  
✅ **CRUD Operations** – Create, Read, Update, and Delete users  
✅ **JWT Authentication** – Secure login, registration, and protected routes  
✅ **Redis Session Caching** – Improve performance by storing user sessions  
✅ **FastAPI & Pydantic** – Efficient request validation and response models  
✅ **SQLAlchemy & PostgreSQL** – Database integration with async support  

## **🛠 Tech Stack**  
- **FastAPI** – High-performance web framework  
- **JWT (PyJWT)** – Token-based authentication  
- **Redis** – Session caching  
- **PostgreSQL** – Relational database  
- **SQLAlchemy** – ORM for database operations  
- **Docker** – Containerized development  

## **📌 Setup & Installation**  
```sh
# Clone the repository
git clone https://github.com/yourusername/fastapi-crud-auth.git
cd fastapi-crud-auth

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Start Redis (if using Docker)
docker run -d --name redis -p 6379:6379 redis

# Run the FastAPI server
uvicorn main:app --reload
```

## **🔗 Endpoints**  
| Method | Endpoint           | Description          | Auth Required |
|--------|--------------------|----------------------|--------------|
| POST   | `/register`        | Register a new user | ❌ No        |
| POST   | `/login`           | User login (JWT)    | ❌ No        |
| GET    | `/users`           | Get all users       | ✅ Yes       |
| GET    | `/users/{id}`      | Get user by ID      | ✅ Yes       |
| PUT    | `/users/{id}`      | Update user         | ✅ Yes       |
| DELETE | `/users/{id}`      | Delete user         | ✅ Yes       |

## **📜 License**  
MIT License  


