### How to use ###
#BUILD: docker build -t backend .
#RUN: docker run --rm -p 127.0.0.1:5000:5000 -t backend -d

FROM python:3.9.18-slim-bullseye
RUN apt update
RUN apt install -y dos2unix
RUN mkdir -p /opt/project


WORKDIR /opt/project/
COPY . /opt/project/
RUN find . -type f -exec dos2unix -q {} \;
# flaskblinker????
RUN pip install -r requirements.txt


RUN echo 'SECRET_KEY="secret key"\n\
SQLALCHEMY_DATABASE_URI="sqlite:////tmp/test.db"\n\
FLASK_ENV=development\n' >> .env


RUN pip install python-dotenv
CMD flask --env-file .env --app app.run run --debug --host 0.0.0.0



