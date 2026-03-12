FROM tensorflow/tensorflow:2.14.0-gpu

WORKDIR /app

COPY . .

RUN python -m pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]