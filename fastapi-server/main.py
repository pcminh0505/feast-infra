from fastapi import FastAPI, Depends, APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from routers import projects, users

from .connection_pool import database_instance

router = APIRouter()

app = FastAPI()

app.include_router(users.router)
app.include_router(projects.router)

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.mount("/static", StaticFiles(directory="static"), name="static"

# Start up event


@app.on_event("startup")
async def startup():
    await database_instance.connect()


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
