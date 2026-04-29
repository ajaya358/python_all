# FastAPI Learning Reference

---

## Project Folder Structure

```
FastApi/
├── server/
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── endpoints/
│   │   │       │   ├── auth.py        → Login API
│   │   │       │   ├── user.py        → User CRUD APIs
│   │   │       │   ├── product.py     → Product CRUD APIs
│   │   │       │   └── file.py        → File upload/download APIs
│   │   │       └── api.py             → Combines all routers
│   │   ├── core/
│   │   │   ├── security.py            → JWT token verification
│   │   │   ├── limiter.py             → Rate limiter setup
│   │   │   ├── exceptions.py          → Custom exception classes
│   │   │   └── exception_handlers.py  → Exception handler functions
│   │   ├── db/
│   │   │   └── db.py                  → Database connection
│   │   ├── models/
│   │   │   ├── user.py                → User table definition
│   │   │   └── product.py             → Product table definition
│   │   ├── schemas/
│   │   │   ├── auth.py                → Token response shape
│   │   │   ├── user.py                → User request/response shape
│   │   │   └── product.py             → Product request/response shape
│   │   ├── services/
│   │   │   ├── auth_service.py        → Login business logic
│   │   │   ├── user_service.py        → User business logic
│   │   │   └── product_service.py     → Product business logic
│   │   ├── utils/
│   │   │   ├── hashing.py             → Password hash & verify
│   │   │   └── jwt.py                 → Create & verify JWT token
│   │   ├── tasks/
│   │   │   └── background_tasks.py    → Background task functions
│   │   └── main.py                    → App entry point
│   ├── uploads/                       → Uploaded files storage
│   ├── .env                           → Secret config values
│   └── requirements.txt               → All packages list
└── ui/                                → React frontend
```

---

## What Each File Does (Simple)

| File | Purpose |
|------|---------|
| `main.py` | Starts the app, connects DB, adds middleware |
| `db.py` | Creates DB connection for LoginDB and ProductDB |
| `models/user.py` | Defines users table columns |
| `models/product.py` | Defines products table columns |
| `schemas/user.py` | Validates user input and output format |
| `schemas/product.py` | Validates product input and output format |
| `schemas/auth.py` | Defines token response format |
| `services/user_service.py` | Create, read, update, delete user logic |
| `services/product_service.py` | Create, read, update, delete product logic |
| `services/auth_service.py` | Check email/password, return JWT token |
| `utils/hashing.py` | Hash password before saving, verify on login |
| `utils/jwt.py` | Create JWT token, decode JWT token |
| `core/security.py` | Protect routes - check if token is valid |
| `core/limiter.py` | Limit how many times an IP can call an API |
| `core/exceptions.py` | Custom exception classes (404, 400, 401) |
| `core/exception_handlers.py` | Functions that handle exceptions and return JSON |
| `endpoints/auth.py` | POST /auth/login route |
| `endpoints/user.py` | All /users/ routes |
| `endpoints/product.py` | All /products/ routes |
| `endpoints/file.py` | File upload, download, list, delete routes |
| `api.py` | Joins auth + user + product + file routers together |
| `tasks/background_tasks.py` | Functions that run after response is sent |

---

## Steps - What Was Done & Why

---

### Step 1 - Project Setup
- Installed FastAPI and uvicorn
- Created folder structure (api, core, db, models, schemas, services, utils)
- Created `requirements.txt` with all packages
- **Why:** Clean structure so each file has one job

---

### Step 2 - Database Connection
- **File:** `db/db.py`
- Connected to 2 databases: `logindb` and `productdb`
- Created sessions for each DB
- Created `get_login_db()` and `get_product_db()` functions
- **Why:** Users and Products are in separate databases

---

### Step 3 - Models
- **Files:** `models/user.py`, `models/product.py`
- Defined table columns using SQLAlchemy
- User table: id, name, email, password
- Product table: id, name, price, description
- **Why:** Models tell SQLAlchemy how to create tables in DB

---

### Step 4 - Schemas (Pydantic)
- **Files:** `schemas/user.py`, `schemas/product.py`, `schemas/auth.py`
- `UserCreate` → what fields are needed to create a user
- `UserResponse` → what fields to return (no password!)
- `TokenResponse` → access_token and token_type
- **Why:** Validates incoming data and controls what goes out in response

---

### Step 5 - Services Layer
- **Files:** `services/user_service.py`, `services/product_service.py`, `services/auth_service.py`
- All database logic lives here (create, get, update, delete)
- Endpoints just call service functions
- **Why:** Keeps endpoints clean, business logic in one place

---

### Step 6 - Routers / Endpoints
- **Files:** `endpoints/auth.py`, `endpoints/user.py`, `endpoints/product.py`, `api/v1/api.py`
- Each file has routes for one topic
- `api.py` combines all routers under `/api/v1`
- **Why:** Organized routing, easy to add new features

---

### Step 7 - JWT Authentication
- **Files:** `utils/jwt.py`, `core/security.py`
- `jwt.py` → creates token on login, decodes token to verify
- `security.py` → `get_current_user()` protects routes
- Protected routes: GET/PUT/DELETE users
- **Why:** Only logged-in users can access protected APIs

---

### Step 8 - Password Hashing
- **File:** `utils/hashing.py`
- `hash_password()` → converts plain password to bcrypt hash before saving
- `verify_password()` → checks plain password against hash on login
- **Why:** Never store plain passwords in database

---

### Step 9 - Logging
- **File:** `main.py`
- Added `logging.basicConfig()` with format and level
- Logs DB connection success/failure on startup
- **Why:** See what's happening in the app without print statements

---

### Step 10 - CORS
- **File:** `main.py`
- Added `CORSMiddleware` to allow frontend to call backend
- Allowed origins stored in `.env` as `ALLOWED_ORIGINS`
- **Why:** Browser blocks requests from different origins by default

---

### Step 11 - Rate Limiting
- **Files:** `core/limiter.py`, `main.py`, `endpoints/auth.py`, `endpoints/user.py`
- `limiter.py` → creates Limiter using client IP
- `main.py` → registers limiter and 429 error handler
- Login → max 5 requests/minute
- Register → max 3 requests/minute
- **Why:** Prevents brute force attacks and spam

---

### Step 12 - Background Tasks
- **Files:** `tasks/background_tasks.py`, `endpoints/user.py`, `endpoints/product.py`
- `background_tasks.py` → 2 functions: `send_welcome_email()` and `update_inventory()`
- `user.py` → added `BackgroundTasks` parameter, calls email task after user creation
- `product.py` → added `BackgroundTasks` parameter, calls inventory task after product creation
- Tasks run **after** response is sent, user doesn't wait
- **Why:** Don't make user wait for slow operations like emails or logging

---

### Step 13 - File Upload/Download
- **Files:** `endpoints/file.py`, `api.py`, `uploads/` folder
- `file.py` → 4 routes: upload, download, list files, delete file
- `api.py` → added file router
- `uploads/` folder → stores all uploaded files
- Uses `UploadFile` and `FileResponse` from FastAPI
- **Why:** Allow users to upload images, PDFs, and download them back

---

### Step 14 - Pagination & Filtering
- **Files:** `services/product_service.py`, `endpoints/product.py`
- `product_service.py` → added parameters: `skip`, `limit`, `name`, `min_price`, `max_price`
- Added filtering logic using SQLAlchemy `.filter()` and `.ilike()`
- Added pagination using `.offset()` and `.limit()`
- `product.py` → added query parameters to GET /products/ endpoint
- **Why:** Handle large datasets efficiently, allow users to search and filter products

---

### Step 15 - Global Exception Handling
- **Files:** `core/exceptions.py`, `core/exception_handlers.py`, `main.py`, all service files
- `exceptions.py` → 3 custom exception classes: `NotFoundException`, `BadRequestException`, `UnauthorizedException`
- `exception_handlers.py` → 5 handler functions for different error types
- `main.py` → registered all exception handlers
- Updated all services to use custom exceptions instead of `HTTPException`
- All errors now return consistent JSON format with `error` and `message` fields
- **Why:** Centralized error handling, consistent error responses, better logging

---

## API Endpoints Quick Reference

| Method | URL | Auth | Limit | What it does |
|--------|-----|------|-------|--------------|
| POST | `/api/v1/auth/login` | No | 5/min | Login, returns JWT |
| POST | `/api/v1/users/` | No | 3/min | Register new user |
| GET | `/api/v1/users/` | Yes | - | Get all users |
| GET | `/api/v1/users/{id}` | Yes | - | Get one user |
| PUT | `/api/v1/users/{id}` | Yes | - | Update user |
| DELETE | `/api/v1/users/{id}` | Yes | - | Delete user |
| POST | `/api/v1/products/` | No | - | Create product |
| GET | `/api/v1/products/` | No | - | Get all products (with pagination & filters) |
| GET | `/api/v1/products/{id}` | No | - | Get one product |
| PUT | `/api/v1/products/{id}` | No | - | Update product |
| DELETE | `/api/v1/products/{id}` | No | - | Delete product |
| POST | `/api/v1/files/upload` | No | - | Upload a file |
| GET | `/api/v1/files/download/{filename}` | No | - | Download a file |
| GET | `/api/v1/files/list` | No | - | List all uploaded files |
| DELETE | `/api/v1/files/{filename}` | No | - | Delete a file |

---

## How to Run

```bash
# Backend
cd server
uvicorn app.main:app --reload

# Frontend
cd ui
npm run dev
```

- Backend runs on → http://localhost:8000
- Frontend runs on → http://localhost:5173
- Swagger docs → http://localhost:8000/docs

---

## All Steps Completed! ✅

| # | Topic | Status |
|---|-------|--------|
| 1 | Project Setup | ✅ |
| 2 | Database Connection (Multi-DB) | ✅ |
| 3 | Models | ✅ |
| 4 | Schemas (Pydantic) | ✅ |
| 5 | Services Layer | ✅ |
| 6 | Routers / Endpoints | ✅ |
| 7 | JWT Auth | ✅ |
| 8 | Hashing (bcrypt) | ✅ |
| 9 | Logging | ✅ |
| 10 | CORS | ✅ |
| 11 | Rate Limiting | ✅ |
| 12 | Background Tasks | ✅ |
| 13 | File Upload/Download | ✅ |
| 14 | Pagination & Filtering | ✅ |
| 15 | Exception Handling (Global) | ✅ |

---

## What You Learned

✅ **FastAPI Basics** - Routes, request/response, dependency injection  
✅ **Database** - SQLAlchemy ORM, multi-database setup, sessions  
✅ **Authentication** - JWT tokens, password hashing, protected routes  
✅ **Validation** - Pydantic schemas, request validation  
✅ **Architecture** - Service layer pattern, clean code structure  
✅ **Security** - CORS, rate limiting, password hashing  
✅ **Advanced Features** - Background tasks, file upload, pagination, filtering  
✅ **Error Handling** - Global exception handlers, consistent error responses  
✅ **Best Practices** - Logging, environment variables, code organization

---
