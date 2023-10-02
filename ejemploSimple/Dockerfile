FROM python:3.11
USER root
ENV DEBIAN_FRONTEND noninteractive
ENV USER_UID 1000
ENV USER_GID 1000
ENV DOCKER_GID 999


# Setup and install base system software
RUN echo "locales locales/locales_to_be_generated multiselect es_CO.UTF-8 UTF-8" | debconf-set-selections \
    && echo "locales locales/default_environment_locale select es_CO.UTF-8" | debconf-set-selections \
    && apt-get update \
    && apt-get --yes --no-install-recommends install \
        locales tzdata ca-certificates sudo libmariadb-dev libmariadb3 \
        bash-completion tar unzip curl rsync vim nano tree build-essential cmake \
        python3-aiomysql python3-mysqldb inetutils-ping iproute2 \
    && rm -rf /var/lib/apt/lists/*
ENV LANG es_CO.UTF-8

# copy all files here into /app in image
COPY manage.py requirements.txt inicio.sh entrypoint.sh /app/
COPY renta /app/renta
COPY ejemploSimple /app/ejemploSimple
WORKDIR /app
# instalar Django
RUN pip3 install --no-cache-dir -r requirements.txt
# run the node app
CMD ["/app/entrypoint.sh"]

