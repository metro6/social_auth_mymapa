FROM python:3.7.2
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true
RUN mkdir /src
RUN mkdir /static
WORKDIR /src
ADD ./src /src
COPY /entrypoint.sh /entrypoint.sh
EXPOSE 80
ENTRYPOINT ["/entrypoint.sh"]
RUN apt-get update && apt-get -y install netcat cron nano swig gcc && apt-get clean
RUN pip install -r requirements.txt