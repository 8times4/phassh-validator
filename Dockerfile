FROM python:slim-buster

RUN apt update && apt upgrade -y

WORKDIR /usr/src/app

COPY validator.py .

CMD ["validator.py"]

ENTRYPOINT ["python3"]