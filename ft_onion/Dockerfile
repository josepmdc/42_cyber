FROM alpine:latest

COPY index.html /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/
COPY torrc /etc/tor/
COPY sshd_config /etc/ssh/sshd_config

ARG PASSWORD

RUN apk --update add --no-cache tor nginx openssh && rm -rf /var/cache/apk/*
RUN echo "root:${PASSWORD}" | chpasswd
RUN /usr/bin/ssh-keygen -A
RUN ssh-keygen -t rsa -b 4096 -f  /etc/ssh/ssh_host_key

ENTRYPOINT nginx; /usr/sbin/sshd; tor
