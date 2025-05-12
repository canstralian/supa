from fastapi import FastAPI, HTTPException, Query
import httpx
import re

app = FastAPI()

# Helper function to fetch data from the given URL
async def fetch_data(url: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()  # Raise an error for non-2xx responses
            return response.json()
        except httpx.RequestError as e:
            raise HTTPException(status_code=500, detail=f"Error during request: {e}")
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=400, detail=f"Invalid response: {e}")
        except ValueError:
            raise HTTPException(status_code=500, detail="Invalid JSON response")

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Fetch endpoint with URL validation
@app.get("/fetch/{url:path}")
async def fetch_endpoint(url: str):
    # Simple validation to ensure the URL is from a safe domain (if needed)
    if not re.match(r"https?://", url):  # Ensure it's an http(s) URL
        raise HTTPException(status_code=400, detail="Invalid URL scheme. Only 'http' and 'https' are allowed.")
    
    # Add https:// if it's missing
    if not url.startswith("https://"):
        url = "https://" + url
    
    # Fetch the data from the provided URL
    data = await fetch_data(url)
    return data

# Run the app with uvicorn (if not running in a REPL-like environment)
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)