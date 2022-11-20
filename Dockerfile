FROM python:3.7.7

WORKDIR /webapp/server
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]

EXPOSE 8000
