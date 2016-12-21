FROM python:2-alpine

ENV TOKEN=changeit \
    DAYS=30

ADD https://github.com/egermano/slack-files-delete/archive/master.zip /
RUN unzip -o master

CMD cd slack-files-delete-master && \
    sed -i "/TOKEN.*=/c\TOKEN=\"${TOKEN}\"" main.py && \
    sed -i "/DAYS.*=/c\DAYS=${DAYS}" main.py && \
    python main.py