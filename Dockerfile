FROM python:3.12

LABEL version=1.0
LABEL author=corentin@cclaudel.fr

ENV SECRET_WEB_KEY=fsjnjkesbfskqhbflh
ENV DATABASE_URL=database.db
ENV SECRET_FILE_KEY=secret.key
ENV BASE_URL=http://127.0.0.1:8080/

WORKDIR /data

RUN apt-get update \
	&& apt install git -y \
	&& git clone https://github.com/Lhokamn/Message_crypter.git \
	&& pip3 install -r Message_crypter/requirements.txt

EXPOSE 8080

CMD [ "python3","Message_crypter/app.py"]
