FROM python:3.9

# 設定工作目錄
WORKDIR /main

# 複製你的 FastAPI 代碼
COPY ./api-service .

# 複製並安裝套件依賴
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 啟動 FastAPI
CMD ["uvicorn", "main.main:app", "--host", "0.0.0.0", "--port", "8000"]