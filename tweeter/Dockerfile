FROM python:3.10.1-alpine
WORKDIR /app
RUN addgroup app adduser -S -G app app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install pycopg2
COPY . .
CMD ["python", "manage.py", "runserver"]