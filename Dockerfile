FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . ./app

EXPOSE 8050

CMD ["python", "main.py"]