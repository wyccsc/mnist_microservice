from fastapi import FastAPI, UploadFile, File
import requests

app = FastAPI()

MODEL_URL = "http://model-service:8000/predict"

@app.post("/upload_predict")
async def upload_predict(datafile: UploadFile = File(...)):
    content = await datafile.read()
    response = requests.post(
        MODEL_URL,
        files={"file": (datafile.filename, content)}
    )
    return response.json()