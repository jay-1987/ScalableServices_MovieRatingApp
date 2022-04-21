FROM python:3.6-alpine3.15
EXPOSE 5000
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]