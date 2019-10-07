FROM python:3.7-slim

RUN mkdir -p /app 

COPY ./zc-client /app
COPY ./requirements.txt /app
RUN pip install --trusted-host pypi.python.org -r /app/requirements.txt

WORKDIR /app
CMD ["python", "app.py"]
