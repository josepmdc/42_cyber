NAME ?= ft_onion

build:
	docker build -t ft_onion .

run:
	docker run -p 8080:80 -p 9050:9050 -d --name=$(NAME) --rm ft_onion:latest
	docker exec -it $(NAME) sh -c "cat /var/lib/tor/42_cyber/hostname"

stop:
	docker stop ft_onion
