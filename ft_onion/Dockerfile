FROM alpine:latest

COPY index.html /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/
COPY torrc /etc/tor/

RUN apk --update add tor nginx

ENTRYPOINT nginx ; tor; cat /var/lib/tor/42_cyber/hostname
