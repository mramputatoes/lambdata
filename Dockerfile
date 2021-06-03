

FROM ubuntu

RUN apt-get update &&\
    apt-get upgrade -y && \
    apt-get install python3 python3-pip curl -y && \
    pip3 install pipenv

RUN pip3 install pandas numpy
RUN pip3 install lambdata