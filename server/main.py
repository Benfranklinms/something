from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Working on port 8005"}

if __name__ == "__main__":
    print("🔥 SERVER DEFINITELY RUNNING ON PORT 8005")
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8005,  # Changed to 8005
        reload=True,
        log_level="debug"
    )