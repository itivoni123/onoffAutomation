FROM python:3.8-slim

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN mkdir e2e
WORKDIR /usr/src/app/e2e
COPY . /usr/src/app/e2e


#COPY .. /app

#RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN apt-get update && apt-get install -y wget unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    apt-get clean

#CMD ["python", "test_onoff_login.py"]
