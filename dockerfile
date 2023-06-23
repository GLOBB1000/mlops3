FROM ubuntu:latest

WORKDIR /app
COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 8000
CMD ["uvicorn", "server:app", "--host", "0.0.0.0"]