
FROM python:3.12

LABEL version 1.0
LABEL author corentin@cclaudel.fr

ENV SECRET_WEB_KEY=fsjnjkesbfskqhbflh
ENV DATABASE_URL=database.db
ENV SECRET_FILE_KEY=secret.key
ENV BASE_URL=http://127.0.0.1:8080/

WORKDIR /data

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 8080

COPY . .

CMD [ "python3","app.py"]