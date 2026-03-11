from fastapi import FastAPI, UploadFile, File
import requests

app = FastAPI()

MODEL_URL="http://model-service:9000/predict"

@app.post("/predict")

async def predict(file:UploadFile=File(...)):

    response = requests.post(
        MODEL_URL,
        files={"file":file.file}
    )

    return response.json()