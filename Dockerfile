FROM python:3.11.11-alpine3.21

EXPOSE 5000

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY wsgi.py .
COPY config.py .

COPY application application

CMD [ "python", "wsgi.py" ]