FROM python:3.10.9-alpine


COPY ./requirements.txt .
RUN pip install -r ./requirements.txt

COPY ./boot.sh .
ENTRYPOINT /bin/sh ./boot.sh
CMD [ "/bin/sh" ]

RUN apk add --no-cache netcat-openbsd
