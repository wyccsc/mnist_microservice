from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import requests
import pandas as pd

app = FastAPI()

MODEL_URL = "http://mnist_microservice_model_service:8000/predict"

RESULT_FILE = "predictions.csv"

@app.post("/upload_predict")
async def upload_predict(datafile: UploadFile = File(...)):

    content = await datafile.read()

    response = requests.post(
        MODEL_URL,
        files={"file": (datafile.filename, content)}
    )

    result = response.json()

    labels = result["labels"]

    df = pd.DataFrame({"Label": labels})

    df.to_csv(RESULT_FILE,index=False)

    return {"labels":labels}


@app.get("/download")
async def download():

    return FileResponse(
        path=RESULT_FILE,
        filename="predictions.csv",
        media_type="text/csv"
    )