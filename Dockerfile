FROM python:latest

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "manage.py", "makemigrations"]
CMD [ "python3", "manage.py", "migrate"]
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
