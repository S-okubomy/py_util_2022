# FROM python:3.10.14-alpine3.20
FROM python:3.11

WORKDIR /myapp

COPY . .

# RUN apk update \
#     && apk add --virtual build-deps gcc python3-dev musl-dev

RUN apt-get -y update \
    && apt-get -y upgrade \
    && apt-get install -y --no-install-recommends locales curl python3-distutils vim ca-certificates libpq-dev gcc python3-dev \
    # && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    # && python3 get-pip.py \
    # && pip install -U pip \
    # && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8 \
    # && apt-get clean \
    # && rm -rf /var/lib/apt/lists/* \
    && pip install -r requirements.txt --no-cache-dir

ENV LANG en_US.utf8

RUN pip install --upgrade pip \
    # && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8 \
    && pip install -r requirements.txt --no-cache-dir 
    # && pip install -r requirements.txt --no-cache-dir 
    # && pip install -r requirements.txt --no-cache-dir \
    # && pip install -e diffbgm --no-cache-dir \
    # && pip isntall -e diffbgm/mir_eval --no-cache-dir

RUN useradd -u 1000 -m user1
USER user1