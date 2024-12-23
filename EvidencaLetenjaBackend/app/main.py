import uvicorn as uvicorn
import os
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine, Base
from app.routes import letalo, pilot, polet

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_URL")],  # Add your frontend origin here
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

Base.metadata.create_all(bind=engine)

app.include_router(polet.router)
app.include_router(letalo.router)
app.include_router(pilot.router)

@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)