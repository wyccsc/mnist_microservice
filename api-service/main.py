from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import requests
import pandas as pd
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_URL = "http://mnist_microservice_model_service:8000/predict"
RESULT_FILE = "predictions.csv"

@app.post("/upload_predict")
async def upload_predict(datafile: UploadFile = File(...)):

    # 讀原始 CSV
    content = await datafile.read()
    df_input = pd.read_csv(io.BytesIO(content))

    # 呼叫模型服務
    response = requests.post(
        MODEL_URL,
        files={"file": (datafile.filename, content)}
    )
    result = response.json()
    labels = result["labels"]

    # 產生 IMAGE 名稱
    # 假設你想要 image_1, image_2, image_3...
    image_names = [f"image_{i+1}" for i in range(len(labels))]

    # 組成輸出資料表
    df_output = pd.DataFrame({
        "IMAGE": image_names,
        "LABEL": labels
    })

    # 儲存 predictions CSV
    df_output.to_csv(RESULT_FILE, index=False)

    return {"labels": labels}

@app.get("/download")
async def download():
    return FileResponse(
        path=RESULT_FILE,
        filename="predictions.csv",
        media_type="text/csv"
    )