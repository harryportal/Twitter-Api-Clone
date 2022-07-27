FROM python:3.10.1
WORKDIR /app
COPY requirements.txt .
RUN ["pip", "install", "requirements.txt"]
COPY . .
CMD ["python", "manage.py", "runserver"]