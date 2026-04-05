from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title = "Task Management REST API" , 
    description = "Fast API CRUD app with postgreSQL, basic auth ,Docker packaging & Github Actions CI/CD",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message" : "Welcome to the Task Management REST API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)