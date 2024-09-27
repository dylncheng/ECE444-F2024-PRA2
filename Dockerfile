FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev-is-python3 build-essential python3.12-venv

COPY . /app
WORKDIR /app

RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install -r requirements.txt

ENV PATH="/opt/venv/bin:$PATH"

RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["hello.py"]