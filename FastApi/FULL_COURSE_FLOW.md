# FastAPI Complete Course - Full Flow & Connections

---

## 📦 All Packages & Their Usage

| Package | ఎందుకు use చేస్తాం | ఎక్కడ use చేస్తాం |
|---------|-------------------|------------------|
| `fastapi` | Web framework - APIs create చేయడానికి | `main.py`, all endpoint files |
| `uvicorn` | Server - FastAPI app run చేయడానికి | Command line: `uvicorn app.main:app` |
| `sqlalchemy` | Database ORM - tables, queries | `db.py`, all model files, service files |
| `pydantic` | Data validation - request/response validation | All schema files |
| `pydantic-settings` | Settings management | Not used yet (optional) |
| `python-dotenv` | `.env` file read చేయడానికి | `main.py`, `db.py` |
| `psycopg2-binary` | PostgreSQL database driver | SQLAlchemy internally uses |
| `email-validator` | Email validation in Pydantic | `schemas/user.py` |
| `bcrypt` | Password hashing | `utils/hashing.py` |
| `python-jose[cryptography]` | JWT token create & verify | `utils/jwt.py` |
| `python-multipart` | File upload support | `endpoints/file.py` |
| `slowapi` | Rate limiting | `core/limiter.py`, `main.py` |

---

## 🔄 Node.js vs FastAPI - Package Comparison (For Node Developers)

| Category | Python Package | = | Node.js Package | What it does |
|----------|----------------|---|-----------------|-------------|
| **Framework** | `fastapi` | = | `express` | Create REST APIs, handle routes |
| **Server** | `uvicorn` | = | `nodemon` | Run the server, auto-reload |
| **Environment** | `python-dotenv` | = | `dotenv` | Read `.env` file variables |
| **Config** | `pydantic-settings` | = | `dotenv` + custom config | Manage app settings with validation |
| **Validation** | `pydantic` | = | `joi` or `zod` | Validate request body, response |
| **Email Check** | `email-validator` | = | `validator.js` | Check if email is valid |
| **ORM** | `sqlalchemy` | = | `sequelize` / `typeorm` / `prisma` | Work with database (models, queries) |
| **DB Driver** | `psycopg2-binary` | = | `pg` | Connect to PostgreSQL |
| **Password** | `bcrypt` | = | `bcrypt` / `bcryptjs` | Hash passwords |
| **JWT** | `python-jose` | = | `jsonwebtoken` | Create & verify JWT tokens |
| **File Upload** | `python-multipart` | = | `multer` | Handle file uploads |
| **Rate Limit** | `slowapi` | = | `express-rate-limit` | Limit API requests per user |
| **Excel Files** | `openpyxl` or `pandas` | = | `exceljs` | Read & create Excel files |
| **Send Email** | `fastapi-mail` | = | `nodemailer` | Send emails (SMTP, attachments) |
| **Async Files** | `aiofiles` | = | `fs.promises` | Read/write files asynchronously |
| **HTTP Client** | `httpx` | = | `axios` or `node-fetch` | Call external APIs |
| **Background Jobs** | `celery` | = | `bullmq` or `bull` | Background tasks & scheduling |
| **Caching** | `redis` | = | `redis` or `ioredis` | Cache data, session storage |
| **DB Migration** | `alembic` | = | `sequelize-cli` or `knex` | Track & manage database changes |

### 📝 Code Comparison Examples:

#### 1. Loading Environment Variables
```javascript
// Node.js
require('dotenv').config();
const dbHost = process.env.DB_HOST;
```
```python
# Python
from dotenv import load_dotenv
import os
load_dotenv()
db_host = os.getenv("DB_HOST")
```

#### 2. Creating Web Server
```javascript
// Node.js + Express
const express = require('express');
const app = express();
app.listen(3000);
```
```python
# Python + FastAPI
from fastapi import FastAPI
import uvicorn
app = FastAPI()
uvicorn.run(app, port=8000)
```

#### 3. Data Validation
```javascript
// Node.js + Joi
const Joi = require('joi');
const schema = Joi.object({
  email: Joi.string().email().required(),
  age: Joi.number().min(18)
});
```
```python
# Python + Pydantic
from pydantic import BaseModel, EmailStr
class User(BaseModel):
    email: EmailStr
    age: int
```

#### 4. Database ORM
```javascript
// Node.js + Sequelize
const User = sequelize.define('User', {
  name: DataTypes.STRING,
  email: DataTypes.STRING
});
```
```python
# Python + SQLAlchemy
class User(Base):
    __tablename__ = "users"
    name = Column(String)
    email = Column(String)
```

#### 5. JWT Token
```javascript
// Node.js
const jwt = require('jsonwebtoken');
const token = jwt.sign({ userId: 1 }, SECRET_KEY);
```
```python
# Python
from jose import jwt
token = jwt.encode({"user_id": 1}, SECRET_KEY)
```

#### 6. Password Hashing
```javascript
// Node.js
const bcrypt = require('bcrypt');
const hash = await bcrypt.hash(password, 10);
```
```python
# Python
import bcrypt
hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
```

---

## 🔗 Complete File Connection Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                         .env (Environment Variables)             │
│  DB_HOST, DB_USER, DB_PASSWORD, SECRET_KEY, ALLOWED_ORIGINS    │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│                          main.py (Entry Point)                   │
│  • Reads .env using load_dotenv()                               │
│  • Creates FastAPI app                                          │
│  • Registers middleware (CORS, Rate Limiter)                    │
│  • Registers exception handlers                                 │
│  • Includes routers from api.py                                 │
│  • Connects to databases on startup (lifespan)                  │
└────────────┬────────────────────────────────────────────────────┘
             │
             ├──────────────────────────────────────────────────┐
             │                                                  │
             ↓                                                  ↓
┌────────────────────────┐                    ┌─────────────────────────┐
│   db/db.py             │                    │  api/v1/api.py          │
│  • Reads .env          │                    │  • Combines all routers │
│  • Creates engines     │                    │  • Prefix: /api/v1      │
│  • Creates sessions    │                    └──────────┬──────────────┘
│  • get_login_db()      │                               │
│  • get_product_db()    │                               │
└────────┬───────────────┘                               │
         │                                               │
         │                                               ↓
         │                              ┌────────────────────────────────┐
         │                              │  api/v1/endpoints/             │
         │                              │  ├── auth.py                   │
         │                              │  ├── user.py                   │
         │                              │  ├── product.py                │
         │                              │  └── file.py                   │
         │                              └────────┬───────────────────────┘
         │                                       │
         │                                       │ (calls services)
         │                                       ↓
         │                              ┌────────────────────────────────┐
         │                              │  services/                     │
         │                              │  ├── auth_service.py           │
         │                              │  ├── user_service.py           │
         │                              │  └── product_service.py        │
         │                              └────────┬───────────────────────┘
         │                                       │
         │ (provides db session)                 │ (uses db session)
         └───────────────────────────────────────┤
                                                 │
                                                 │ (queries database)
                                                 ↓
                                        ┌────────────────────────┐
                                        │  models/               │
                                        │  ├── user.py           │
                                        │  └── product.py        │
                                        └────────────────────────┘
```

---

## 📋 Import Flow - Who Imports What

### 1️⃣ main.py imports:
```python
from fastapi import FastAPI                          # FastAPI framework
from fastapi.middleware.cors import CORSMiddleware   # CORS middleware
from fastapi.exceptions import RequestValidationError # Validation errors
from slowapi import _rate_limit_exceeded_handler     # Rate limit handler
from slowapi.errors import RateLimitExceeded         # Rate limit error
from sqlalchemy import text                          # SQL queries
from contextlib import asynccontextmanager           # Lifespan context
from dotenv import load_dotenv                       # Load .env file
import logging                                       # Logging
import os                                            # Environment variables

# Our files
from app.db.db import login_engine, product_engine, Base
from app.models import user, product
from app.api.v1.api import router
from app.core.limiter import limiter
from app.core.exceptions import NotFoundException, BadRequestException, UnauthorizedException
from app.core.exception_handlers import (...)
```

**Why:** main.py is entry point, so it needs everything to start the app

---

### 2️⃣ db/db.py imports:
```python
from sqlalchemy import create_engine          # Create DB connection
from sqlalchemy.orm import sessionmaker, declarative_base  # ORM setup
import os                                     # Read environment variables
```

**Exports:**
- `login_engine` → used in main.py, services
- `product_engine` → used in main.py, services
- `Base` → used in models
- `get_login_db()` → used in user/auth endpoints
- `get_product_db()` → used in product endpoints

**Flow:**
```
.env → os.getenv() → create_engine() → sessionmaker() → get_login_db()/get_product_db()
                                                              ↓
                                                    endpoints use as Depends()
```

---

### 3️⃣ models/user.py imports:
```python
from sqlalchemy import Column, Integer, String  # Table columns
from app.db.db import Base                      # Base class for models
```

**Exports:**
- `User` class → used in services, main.py

**Flow:**
```
Base (from db.py) → User(Base) → main.py creates tables → services query User table
```

---

### 4️⃣ models/product.py imports:
```python
from sqlalchemy import Column, Integer, String, Float  # Table columns
from app.db.db import Base                             # Base class
```

**Exports:**
- `Product` class → used in services, main.py

---

### 5️⃣ schemas/user.py imports:
```python
from pydantic import BaseModel, EmailStr  # Validation
```

**Exports:**
- `UserCreate` → used in endpoints (request body)
- `UserResponse` → used in endpoints (response)

**Flow:**
```
Client sends JSON → FastAPI validates using UserCreate → Service processes → Returns UserResponse
```

---

### 6️⃣ schemas/product.py imports:
```python
from pydantic import BaseModel  # Validation
```

**Exports:**
- `ProductCreate` → request validation
- `ProductResponse` → response format

---

### 7️⃣ schemas/auth.py imports:
```python
from pydantic import BaseModel  # Validation
```

**Exports:**
- `TokenResponse` → login response format

---

### 8️⃣ utils/hashing.py imports:
```python
import bcrypt  # Password hashing library
```

**Exports:**
- `hash_password()` → used in user_service.py
- `verify_password()` → used in auth_service.py

**Flow:**
```
Registration: plain password → hash_password() → hashed → save to DB
Login: plain password + hashed (from DB) → verify_password() → True/False
```

---

### 9️⃣ utils/jwt.py imports:
```python
from jose import jwt                          # JWT library
from datetime import datetime, timedelta      # Token expiry
import os                                     # Read SECRET_KEY from env
```

**Exports:**
- `create_access_token()` → used in auth_service.py
- `verify_token()` → used in core/security.py

**Flow:**
```
Login success → create_access_token() → return token to client
Client sends token → verify_token() → extract user info → allow access
```

---

### 🔟 core/security.py imports:
```python
from fastapi import Depends, HTTPException           # Dependency injection
from fastapi.security import OAuth2PasswordBearer    # OAuth2 scheme
from app.utils.jwt import verify_token               # JWT verification
from jose import JWTError                            # JWT errors
```

**Exports:**
- `get_current_user()` → used in protected endpoints

**Flow:**
```
Protected endpoint → Depends(get_current_user) → extracts token from header → verify_token() → returns user data
```

---

### 1️⃣1️⃣ core/limiter.py imports:
```python
from slowapi import Limiter                    # Rate limiter
from slowapi.util import get_remote_address    # Get client IP
```

**Exports:**
- `limiter` → used in main.py, endpoints

**Flow:**
```
Client request → limiter checks IP → counts requests → allows or blocks (429)
```

---

### 1️⃣2️⃣ core/exceptions.py imports:
```python
# No imports - just defines custom exception classes
```

**Exports:**
- `NotFoundException` → used in services
- `BadRequestException` → used in services
- `UnauthorizedException` → used in services

---

### 1️⃣3️⃣ core/exception_handlers.py imports:
```python
from fastapi import Request, status                  # Request object, status codes
from fastapi.responses import JSONResponse           # JSON response
from fastapi.exceptions import RequestValidationError # Validation errors
from app.core.exceptions import (...)                # Our custom exceptions
import logging                                       # Logging
```

**Exports:**
- Handler functions → registered in main.py

**Flow:**
```
Service raises NotFoundException → main.py catches → exception_handler → returns JSON response
```

---

### 1️⃣4️⃣ services/user_service.py imports:
```python
from sqlalchemy.orm import Session                   # DB session
from fastapi import HTTPException                    # Errors
from app.models.user import User                     # User model
from app.schemas.user import UserCreate              # Request schema
from app.utils.hashing import hash_password          # Password hashing
from app.core.exceptions import (...)                # Custom exceptions
```

**Exports:**
- `create_user()` → used in endpoints/user.py
- `get_users()` → used in endpoints/user.py
- `get_user()` → used in endpoints/user.py
- `update_user()` → used in endpoints/user.py
- `delete_user()` → used in endpoints/user.py

**Flow:**
```
Endpoint → calls service function → service queries DB using model → returns data
```

---

### 1️⃣5️⃣ services/product_service.py imports:
```python
from sqlalchemy.orm import Session                   # DB session
from fastapi import HTTPException                    # Errors
from app.models.product import Product               # Product model
from app.schemas.product import ProductCreate        # Request schema
from app.core.exceptions import NotFoundException    # Custom exception
```

**Exports:**
- CRUD functions → used in endpoints/product.py

---

### 1️⃣6️⃣ services/auth_service.py imports:
```python
from sqlalchemy.orm import Session                   # DB session
from fastapi import HTTPException                    # Errors
from app.models.user import User                     # User model
from app.utils.hashing import verify_password        # Password verification
from app.utils.jwt import create_access_token        # JWT creation
from app.core.exceptions import UnauthorizedException # Custom exception
import logging                                       # Logging
```

**Exports:**
- `login()` → used in endpoints/auth.py

**Flow:**
```
Login request → auth_service.login() → verify password → create JWT → return token
```

---

### 1️⃣7️⃣ tasks/background_tasks.py imports:
```python
import logging  # Logging
import time     # Simulate delay
```

**Exports:**
- `send_welcome_email()` → used in endpoints/user.py
- `update_inventory()` → used in endpoints/product.py

**Flow:**
```
User created → endpoint adds background task → response sent immediately → task runs after
```

---

### 1️⃣8️⃣ endpoints/auth.py imports:
```python
from fastapi import APIRouter, Depends, Request              # FastAPI
from fastapi.security import OAuth2PasswordRequestForm       # Login form
from sqlalchemy.orm import Session                           # DB session
from app.db.db import get_login_db                           # DB dependency
from app.schemas.auth import TokenResponse                   # Response schema
from app.services import auth_service                        # Business logic
from app.core.limiter import limiter                         # Rate limiting
```

**Exports:**
- `router` → included in api.py

---

### 1️⃣9️⃣ endpoints/user.py imports:
```python
from fastapi import APIRouter, Depends, Request, BackgroundTasks  # FastAPI
from sqlalchemy.orm import Session                                # DB session
from app.db.db import get_login_db                                # DB dependency
from app.schemas.user import UserCreate, UserResponse             # Schemas
from app.services import user_service                             # Business logic
from app.core.security import get_current_user                    # Auth
from app.core.limiter import limiter                              # Rate limiting
from app.tasks.background_tasks import send_welcome_email         # Background task
```

**Exports:**
- `router` → included in api.py

---

### 2️⃣0️⃣ endpoints/product.py imports:
```python
from fastapi import APIRouter, Depends, BackgroundTasks  # FastAPI
from sqlalchemy.orm import Session                       # DB session
from app.db.db import get_product_db                     # DB dependency
from app.schemas.product import ProductCreate, ProductResponse  # Schemas
from app.services import product_service                 # Business logic
from app.tasks.background_tasks import update_inventory  # Background task
```

**Exports:**
- `router` → included in api.py

---

### 2️⃣1️⃣ endpoints/file.py imports:
```python
from fastapi import APIRouter, UploadFile, File, HTTPException  # FastAPI
from fastapi.responses import FileResponse                      # File download
import os                                                       # File operations
import shutil                                                   # File copy
```

**Exports:**
- `router` → included in api.py

---

### 2️⃣2️⃣ api/v1/api.py imports:
```python
from fastapi import APIRouter                        # Router
from app.api.v1.endpoints import user, product, auth, file  # All endpoint routers
```

**Exports:**
- `router` → included in main.py

**Flow:**
```
main.py includes api.py router → api.py includes all endpoint routers → endpoints define routes
```

---

## 🔄 Complete Request Flow Example

### Example: User Registration

```
1. Client sends POST request to /api/v1/users/
   Body: {"name": "John", "email": "john@test.com", "password": "pass123"}

2. Request hits main.py → routes to api.py → routes to endpoints/user.py

3. endpoints/user.py:
   - Rate limiter checks (3 requests/min)
   - Pydantic validates request body using UserCreate schema
   - Calls user_service.create_user()

4. services/user_service.py:
   - Checks if email exists (queries DB using User model)
   - If exists → raises BadRequestException
   - Calls hash_password() from utils/hashing.py
   - Creates new User object
   - Saves to DB using session from get_login_db()
   - Returns user object

5. endpoints/user.py:
   - Adds background task: send_welcome_email()
   - Returns response (UserResponse schema)

6. Background task runs after response sent:
   - tasks/background_tasks.py → send_welcome_email() → logs message

7. Client receives response:
   {"id": 1, "name": "John", "email": "john@test.com"}
```

---

## 🗄️ Database Connection Flow

```
.env file
  ↓
DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
  ↓
db/db.py reads using os.getenv()
  ↓
create_engine() creates connection
  ↓
sessionmaker() creates session factory
  ↓
get_login_db() / get_product_db() functions
  ↓
Used in endpoints as Depends(get_login_db)
  ↓
Session passed to service functions
  ↓
Service queries database using models
  ↓
Session closed automatically (try/finally)
```

---

## 🔐 Authentication Flow

```
1. Registration:
   plain password → hash_password() → bcrypt hash → save to DB

2. Login:
   Client sends email + password
     ↓
   auth_service.login()
     ↓
   Query DB for user by email
     ↓
   verify_password(plain, hashed)
     ↓
   If valid → create_access_token()
     ↓
   Return JWT token to client

3. Protected Route Access:
   Client sends request with header: Authorization: Bearer <token>
     ↓
   Depends(get_current_user) extracts token
     ↓
   verify_token() decodes JWT
     ↓
   If valid → returns user data
     ↓
   Endpoint executes
```

---

## 📊 Data Validation Flow

```
Client sends JSON
  ↓
FastAPI receives request
  ↓
Pydantic schema validates (UserCreate, ProductCreate, etc.)
  ↓
If invalid → RequestValidationError → exception_handler → 422 response
  ↓
If valid → data passed to endpoint function
  ↓
Endpoint calls service
  ↓
Service processes and returns data
  ↓
Pydantic response schema formats output (UserResponse, ProductResponse)
  ↓
FastAPI sends JSON response to client
```

---

## 🚨 Error Handling Flow

```
Service raises custom exception (NotFoundException, BadRequestException, etc.)
  ↓
Exception bubbles up to main.py
  ↓
main.py has registered exception handlers
  ↓
Appropriate handler function executes
  ↓
Handler logs error
  ↓
Handler returns JSONResponse with consistent format
  ↓
Client receives: {"error": "...", "message": "..."}
```

---

## 📁 File Storage Flow

```
Client uploads file
  ↓
endpoints/file.py receives UploadFile
  ↓
File saved to uploads/ folder using shutil.copyfileobj()
  ↓
Returns success message

Download:
Client requests /files/download/{filename}
  ↓
endpoints/file.py checks if file exists
  ↓
Returns FileResponse with file content
```

---

## ⏱️ Background Task Flow

```
Endpoint function receives BackgroundTasks parameter
  ↓
Endpoint calls: background_tasks.add_task(function_name, args)
  ↓
Endpoint returns response immediately
  ↓
After response sent, FastAPI executes background task
  ↓
Task function runs (send_welcome_email, update_inventory, etc.)
  ↓
Task completes (logs message)
```

---

## 🎯 Summary - Why Each Package

| Package | Real Usage in Our Project |
|---------|---------------------------|
| `fastapi` | Creates all routes, handles requests/responses |
| `uvicorn` | Runs the server on port 8000 |
| `sqlalchemy` | Connects to PostgreSQL, creates tables, runs queries |
| `pydantic` | Validates email format, required fields, data types |
| `python-dotenv` | Reads DB credentials from .env file |
| `psycopg2-binary` | Allows SQLAlchemy to talk to PostgreSQL |
| `email-validator` | Checks if email is valid format |
| `bcrypt` | Hashes passwords before saving, verifies on login |
| `python-jose` | Creates JWT tokens on login, verifies on protected routes |
| `python-multipart` | Allows file uploads in /files/upload endpoint |
| `slowapi` | Limits login to 5 attempts/min, register to 3/min |

---

## 🔗 Key Connections Summary

```
.env → db.py → models → services → endpoints → api.py → main.py

main.py = Entry point (starts everything)
db.py = Database connection (provides sessions)
models = Table definitions (User, Product)
schemas = Validation (request/response format)
services = Business logic (CRUD operations)
endpoints = API routes (HTTP methods)
utils = Helper functions (hashing, JWT)
core = App-level features (security, rate limiting, exceptions)
tasks = Background jobs (run after response)
```

---

**ఇప్పుడు అర్థమైందా? ఏదైనా doubt ఉందా?** 🚀
