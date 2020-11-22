# For production we probably want to use the regular python system
# or the offical one from FastAPI
# For development we'll use the slim python because it's <400MB
# FROM python:3.7
# FROM python:3.7-alpine
FROM python:3.7-slim
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r /app/requirements.txt
COPY ./ /app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
