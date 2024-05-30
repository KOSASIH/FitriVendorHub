# Import necessary libraries and frameworks
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.background import BackgroundTasks
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime, timedelta
import json
import os
import uuid
import hashlib
import jwt
import redis

# Initialize FastAPI app
app = FastAPI(
    title="Inventory Management System",
    description="A high-tech inventory management system",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Initialize templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Initialize Redis cache
cache_backend = RedisBackend("redis://localhost:6379/0")
FastAPICache.init(cache_backend)

# Define OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Define user model
class User(BaseModel):
    id: int
    username: str
    email: str
    password: str

# Define inventory item model
class InventoryItem(BaseModel):
    id: int
    name: str
    description: str
    quantity: int
    price: float
    created_at: datetime
    updated_at: datetime

# Define authentication function
async def authenticate_user(username: str, password: str):
    # Simulate database query
    user = User(id=1, username="admin", email="admin@example.com", password="password")
    if user.username == username and user.password == password:
        return user
    return None

# Define token generator function
async def generate_token(user: User):
    payload = {
        "exp": datetime.utcnow() + timedelta(minutes=30),
        "iat": datetime.utcnow(),
        "sub": user.id
    }
    token = jwt.encode(payload, os.environ["SECRET_KEY"], algorithm="HS256")
    return token

# Define login endpoint
@app.post("/login")
async def login(username: str, password: str):
    user = await authenticate_user(username, password)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = await generate_token(user)
    return JSONResponse(content={"token": token}, status_code=200)

# Define protected endpoint
@app.get("/protected")
async def protected(token: str = Depends(oauth2_scheme)):
    user_id = jwt.decode(token, os.environ["SECRET_KEY"], algorithms=["HS256"])["sub"]
    return JSONResponse(content={"message": f"Hello, user {user_id}!"}, status_code=200)

# Define inventory endpoint
@app.get("/inventory")
@cache(ttl=60)  # Cache for 1 minute
async def get_inventory():
    # Simulate database query
    inventory_items = [
        InventoryItem(id=1, name="Item 1", description="Description 1", quantity=10, price=10.99, created_at=datetime.utcnow(), updated_at=datetime.utcnow()),
        InventoryItem(id=2, name="Item 2", description="Description 2", quantity=20, price=20.99, created_at=datetime.utcnow(), updated_at=datetime.utcnow())
    ]
    return JSONResponse(content={"inventory": inventory_items}, status_code=200)

# Define background task
async def background_task(item_id: int):
    # Simulate long-running task
    await asyncio.sleep(5)
    print(f"Background task completed for item {item_id}")

# Define create inventory item endpoint
@app.post("/inventory")
async def create_inventory_item(item: InventoryItem):
    # Simulate database query
    item.id = uuid.uuid4().int
    item.created_at = datetime.utcnow()
    item.updated_at = datetime.utcnow()
    # Run background task
    background_tasks = BackgroundTasks()
    background_tasks.add_task(background_task, item_id=item.id)
    return JSONResponse(content={"message": "Inventory item created successfully"}, status_code=201)

# Define update inventory item endpoint
@app.put("/inventory/{item_id}")
async def update_inventory_item(item_id: int, item: InventoryItem):
    # Simulate database query
    item.updated_at = datetime.utcnow()
    return JSONResponse(content={"message": "Inventory item updated successfully"}, status_code=200)

# Define delete inventory item endpoint
@app.delete("/inventory/{item_id}")
async def delete_inventory_item(item_id: int):
    # Simulate database query
    return JSONResponse(content={"message": "Inventory item deleted successfully"}, status_code=200)

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
