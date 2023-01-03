FROM python:3.11.1-alpine3.17

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt


CMD ["python", "code.py"]
