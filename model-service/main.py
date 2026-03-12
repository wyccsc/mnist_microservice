from fastapi import FastAPI, UploadFile, File
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model

app = FastAPI()

model = load_model("my_cnn_model.keras")

@app.post("/predict")

async def predict(file:UploadFile=File(...)):

    df = pd.read_csv(file.file)

    data = df.values/255.0
    data = data.reshape(-1,28,28,1)

    preds = model.predict(data)

    labels = np.argmax(preds,axis=1)

    return {"labels":labels.tolist()}