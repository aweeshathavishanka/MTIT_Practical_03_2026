from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import httpx

app = FastAPI()

SERVICES = {
    "student": "http://localhost:8001"
}

async def forward_request(service, path, method, json=None):

    url = f"{SERVICES[service]}{path}"

    async with httpx.AsyncClient() as client:

        if method == "GET":
            response = await client.get(url)

        elif method == "POST":
            response = await client.post(url, json=json)

        elif method == "PUT":
            response = await client.put(url, json=json)

        elif method == "DELETE":
            response = await client.delete(url)

        return JSONResponse(
            content=response.json(),
            status_code=response.status_code
        )

@app.get("/")
def root():
    return {"message": "Gateway running"}

@app.get("/gateway/students")
async def get_students():
    return await forward_request("student", "/api/students", "GET")

@app.post("/gateway/students")
async def create_student(request: Request):
    body = await request.json()
    return await forward_request("student", "/api/students", "POST", body)