
from fastapi import FastAPI
import httpx

app = FastAPI()

async def fetch_data(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/fetch/{url:path}")
async def fetch_endpoint(url: str):
    data = await fetch_data(f"https://{url}")
    return data

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
