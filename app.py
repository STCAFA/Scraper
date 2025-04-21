from fastapi import FastAPI
import asyncio
from scraper import get_products

app = FastAPI()

@app.get("/")
async def root():
    data = await get_products()
    return {"products": data}