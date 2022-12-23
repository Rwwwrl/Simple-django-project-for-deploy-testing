FROM python:3.10

RUN yes | apt update
RUN yes | apt upgrade
RUN yes | apt install -y vim
RUN yes | apt install netcat

RUN mkdir -p /usr/src

WORKDIR /usr/src

COPY . .

RUN chmod +x postgres_check_health.sh
RUN chmod +x gunicorn_entrypoint.sh
RUN chmod +x entrypoint.sh

RUN pip install -r requirements.txt

RUN mkdir static media
RUN python manage.py collectstatic

# gunicorn
RUN pip install gunicorn

CMD ["./entrypoint.sh"]
