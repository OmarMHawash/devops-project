ARG PY_VERSION=3.10

FROM python:${PY_VERSION}-alpine

WORKDIR /usr/src/app
COPY requirements.txt ./
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./app.py" ]