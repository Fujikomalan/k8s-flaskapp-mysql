FROM python:alpine

RUN mkdir /var/flaskapp

WORKDIR /var/flaskapp

COPY .  .
RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD ["python3","app.py"]
