FROM python:3.8-alpine
WORKDIR /app
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add libffi-dev
RUN adduser -D user
USER user
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["entrypoint.sh"]
