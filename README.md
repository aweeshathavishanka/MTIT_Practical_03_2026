
# Building a Microservices Architecture with API Gateway using Python FastAPI

## Student Information

**Name:** Aweesha Wijesundara  
**Registration Number:** IT22183668  
**Batch:** WMAT Wijesundara

**Project Repository:**  
https://github.com/aweeshathavishanka/MTIT_Practical_03_2026

---

## Project Overview

This project demonstrates how to build a Microservices Architecture using Python FastAPI and implement an API Gateway pattern.

The system consists of two main components:

1. Student Microservice
2. API Gateway

The API Gateway acts as a single entry point and forwards requests to the Student Microservice.

---

## Architecture Diagram

```
Client
│
▼
API Gateway (Port 8000)
│
▼
Student Microservice (Port 8001)

```

---

## Technologies Used

- Python 3.11
- FastAPI
- Uvicorn
- Pydantic
- HTTPx
- VS Code
- Git & GitHub

---

## Project Structure

```

microservices-fastapi/
│
├── gateway/
│ └── main.py
│
├── student_service/
│ ├── main.py
│ ├── models.py
│ ├── service.py
│ └── data_service.py
│
├── venv/
├── requirements.txt
└── README.md

````

---

## Installation Guide (Step-by-Step)

### Step 1: Clone the Repository

```bash
git clone https://github.com/aweeshathavishanka/MTIT_Practical_03_2026.git
cd MTIT_Practical_03_2026
````

---

### Step 2: Install Python 3.11

Check version:

```bash
python3 --version
```

If not Python 3.11, install using Homebrew (Mac):

```bash
brew install python@3.11
```

---

### Step 3: Create Virtual Environment

```bash
python3.11 -m venv venv
```

Activate virtual environment:

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

---

### Step 4: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Running the Student Microservice

Navigate to student service folder:

```bash
cd student_service
```

Run service:

```bash
python -m uvicorn main:app --reload --port 8001
```

Server will start at:

```
http://127.0.0.1:8001
```

Swagger UI:

```
http://127.0.0.1:8001/docs
```

---

## Running the API Gateway

Open new terminal.

Activate virtual environment:

```bash
source venv/bin/activate
```

Navigate to gateway folder:

```bash
cd gateway
```

Run gateway:

```bash
python -m uvicorn main:app --reload --port 8000
```

Gateway URL:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## Testing the System

### Direct Microservice Access

```
GET http://127.0.0.1:8001/api/students
```

### Gateway Access

```
GET http://127.0.0.1:8000/gateway/students
```

Both return the same result.

---

## CRUD Operations

### Get All Students

```
GET /gateway/students
```

### Get Student by ID

```
GET /gateway/students/{id}
```

### Create Student

```
POST /gateway/students
```

Example JSON:

```json
{
  "name": "Alice",
  "age": 23,
  "email": "alice@example.com",
  "course": "Data Science"
}
```

### Update Student

```
PUT /gateway/students/{id}
```

### Delete Student

```
DELETE /gateway/students/{id}
```

---

## Debugging Guide

### Problem 1: uvicorn command not found

Solution:

Activate virtual environment:

```bash
source venv/bin/activate
```

or run:

```bash
python -m uvicorn main:app --reload --port 8001
```

---

### Problem 2: Could not import module "main"

Cause:
Wrong folder name or running from wrong directory.

Solution:

Ensure correct structure:

```
student_service/main.py
```

Run from correct directory:

```bash
cd student_service
python -m uvicorn main:app --reload --port 8001
```

---

### Problem 3: pydantic-core build error

Cause:
Python 3.14 not supported.

Solution:
Use Python 3.11

Check version:

```bash
python --version
```

---

### Problem 4: Port already in use

Solution:

Stop previous process:

```bash
CTRL + C
```

Or use different port:

```bash
--port 8002
```

---

## How API Gateway Works

API Gateway acts as a router.

Flow:

```
Client Request
     │
     ▼
API Gateway
     │
     ▼
Student Microservice
     │
     ▼
Response to Client
```

Benefits:

- Single entry point
- Better security
- Easy scaling
- Separation of services

---

## Features Implemented

- Microservice Architecture
- API Gateway Pattern
- CRUD Operations
- Request Forwarding
- FastAPI REST APIs
- Swagger Documentation

---

## Learning Outcomes

Through this project, I learned:

- Microservices architecture concepts
- API Gateway pattern implementation
- FastAPI framework usage
- REST API development
- Service communication using HTTPx
- Debugging Python microservices
- Virtual environment management
- GitHub project management

---

## Author

Aweesha Wijesundara
IT22183668
WMAT Wijesundara

---

## GitHub Repository

[https://github.com/aweeshathavishanka/MTIT_Practical_03_2026](https://github.com/aweeshathavishanka/MTIT_Practical_03_2026)

---

## License

This project is for academic purposes (MTIT Practical 03 – 2026).


