FROM alpine:latest

COPY index.html /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/
COPY torrc /etc/tor/

ARG PASSWORD

RUN apk --update add --no-cache tor nginx openssh \
  && sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config \
  && echo "root:${PASSWORD}" | chpasswd \
  && rm -rf /var/cache/apk/*

# Defining the Port 4242 for service
RUN sed -ie 's/#Port 22/Port 4242/g' /etc/ssh/sshd_config
RUN /usr/bin/ssh-keygen -A
RUN ssh-keygen -t rsa -b 4096 -f  /etc/ssh/ssh_host_key

ENTRYPOINT nginx; /usr/sbin/sshd; tor
