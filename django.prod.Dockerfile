FROM python:3.10.9-alpine


RUN apk add --no-cache netcat-openbsd

WORKDIR /App
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt

COPY ./ ./
ENTRYPOINT /bin/sh ./boot.sh
CMD [ "/bin/sh" ]
