NAME ?= ft_onion
PASSWORD ?= ft_onion

build:
	docker build --build-arg PASSWORD=$(PASSWORD) -t ft_onion .

run:
	docker run -p 8080:80 -p 9050:9050 -p 4242:4242 -d --name=$(NAME) --rm ft_onion:latest
	docker exec -it $(NAME) sh -c "cat /var/lib/tor/42_cyber/hostname"

stop:
	docker kill ft_onion

status:
	docker ps -f name=$(NAME)

logs:
	docker logs $(NAME)

onion:
	docker exec -it $(NAME) sh -c "cat /var/lib/tor/42_cyber/hostname"
