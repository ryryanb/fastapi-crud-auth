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

## Clone the repository
git clone https://github.com/yourusername/fastapi-crud-auth.git
cd fastapi-crud-auth

## Create a virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows

## Install dependencies
pip install -r requirements.txt

## **🚀 Running the Application**  

### **Option 1: Run Everything in Docker (Recommended)**  
This will start both FastAPI and PostgreSQL in Docker.  
```
docker-compose up -d
```
- **FastAPI will run on** `http://127.0.0.1:8000`
- **PostgreSQL will be accessible at** `postgresql://postgres:yourpassword@db/fastcharge`
- **Redis must be started separately** (see below).  

### **Option 2: Use Local PostgreSQL**  
1. **Install PostgreSQL** (if not installed).  
2. **Create a new PostgreSQL database** (`fastcharge`).  
3. **Update your `.env` file** with:  

   ```
   DATABASE_URL=postgresql://postgres:yourpassword@localhost/fastcharge
   ```

4. **Run the database migration** to create tables:  

   ```sh
   python init_db.py
   ```

5. **Start Redis** (if not already running):  

   ```sh
   docker run -d --name redis -p 6379:6379 redis
   ```

6. **Start the FastAPI application**:  

   ```sh
   uvicorn main:app --reload
   ```

## **🧪 Testing the APIs**  
After starting the app, visit:  
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  

Click on an endpoint, enter any required parameters, and hit "Execute" to test.  

---

## **🔗 Endpoints**  

| Method | Endpoint           | Description          | Auth Required |
|--------|--------------------|----------------------|--------------|
| POST   | `/register`        | Register a new user | ❌ No        |
| POST   | `/token`           | User login (JWT)    | ❌ No        |
| GET    | `/me`              | Current user        | ✅ Yes       |
| GET    | `/users`           | Get all users       | ✅ Yes       |
| GET    | `/users/{id}`      | Get user by ID      | ✅ Yes       |
| PUT    | `/users/{id}`      | Update user         | ✅ Yes       |
| DELETE | `/users/{id}`      | Delete user         | ✅ Yes       |

![Redoc UI](assets/redocUI.png)

## **📜 License**  
MIT License  
```
