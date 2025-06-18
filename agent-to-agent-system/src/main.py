from fastapi import FastAPI
from src.api.routes import router as api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
}
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Agent to Agent System"}

app.include_router(api_router)

# To run the application, use the command: python -m src.main
# Replace 'src.main' with the module path to your FastAPI app