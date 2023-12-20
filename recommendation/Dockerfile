FROM python:3.9-slim
LABEL authors="romainmarques & antoinelachaud"

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Run app.py when the container launches
CMD ["python", "server.py"]