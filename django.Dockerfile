FROM python:3.10.9


COPY ./requirements.txt .
RUN pip install -r ./requirements.txt

COPY ./boot.sh .
ENTRYPOINT /bin/bash ./boot.sh
CMD [ "/bin/bash" ]
