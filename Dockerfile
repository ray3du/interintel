# Pull base image
FROM python:3.8-alpine
LABEL authors="ray3du"

# set work directory
WORKDIR /app
RUN mkdir /app/staticfiles
RUN mkdir /app/mediafiles

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
