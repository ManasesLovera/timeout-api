import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get("/fast")
async def fast_endpoint():
    return {"message": "Quick response"}

# Delay via GET route param (default = 10 seconds)
@app.get("/slow/{seconds}")
async def slow_endpoint(seconds: int = 10):
    await asyncio.sleep(seconds)
    return {"message": f"This took {seconds} seconds (async GET)"}

# Delay via POST route param (default = 10 seconds)
@app.post("/slow/{seconds}")
async def slow_post_endpoint(seconds: int = 10):
    await asyncio.sleep(seconds)
    return {"message": f"This took {seconds} seconds (async POST)"}
