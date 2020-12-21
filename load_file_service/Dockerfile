FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
  binutils \
  gdal-bin \
  python3-gdal \
  libproj-dev
RUN mkdir /code
WORKDIR /code
COPY /requierements/base.txt /code/
COPY /requierements/development.txt /code/
RUN pip install -r development.txt
COPY . /code/
EXPOSE 8000
RUN chmod +x /code/start.sh
ENTRYPOINT ["sh","/code/start.sh"]
