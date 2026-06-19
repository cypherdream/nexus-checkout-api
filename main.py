from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.middleware import start_up_db
from api.endpoints import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://nexus-frontend-zeta-swart.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def start_up():
    start_up_db()


app.include_router(router)
