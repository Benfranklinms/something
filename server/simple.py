from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "SUCCESS AT LAST"}

if __name__ == "__main__":
    print("🔥 SERVER DEFINITELY STARTING ON PORT 8005")
    uvicorn.run(app, host="0.0.0.0", port=8005, log_level="info")