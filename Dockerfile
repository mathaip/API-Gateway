FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements.txt ./
COPY service-account.json ./

# Install production dependencies.
RUN pip install -r requirements.txt

COPY ./app /app/app
