FROM python:3.10

ARG NON_PRIVILEGED_USER_NAME="developer"

RUN apt update

RUN groupadd --gid 1000 ${NON_PRIVILEGED_USER_NAME} \
    && useradd ${NON_PRIVILEGED_USER_NAME} --create-home --uid 1000 --gid 1000 --shell /bin/bash \
    && usermod --append --groups www-data ${NON_PRIVILEGED_USER_NAME} \
    && echo 'alias ll="ls -al"' >> /root/.bashrc \
    && echo 'alias ll="ls -al"' >> /home/${NON_PRIVILEGED_USER_NAME}/.bashrc


WORKDIR /app

COPY src/requirements.txt .
RUN pip3 install -r requirements.txt

COPY src .

CMD ["tail", "-f", "/dev/null"]
