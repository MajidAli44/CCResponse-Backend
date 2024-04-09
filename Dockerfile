FROM python:3.8-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install --no-install-recommends build-essential python3-dev libpq-dev libxml2-dev \
libxslt-dev libffi-dev musl-dev openssl curl libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev \
libopenjp2.7-dev libtiff-dev tk tcl netcat wkhtmltopdf git

COPY ./Pipfile ./Pipfile.lock ./requirements.txt ./
RUN pip install --upgrade pip pipenv
RUN pipenv install --system --deploy --ignore-pipfile --dev
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .

# make entrypoint.sh executable
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/bin/bash", "/usr/src/app/entrypoint.sh"]
