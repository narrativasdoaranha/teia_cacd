.PHONY: dev build push deploy

dev:
	docker-compose up

build:
	docker-compose build

push:
	git push origin master

deploy:
	ssh usuario@seu-servidor "cd /caminho/para/aplicacao && ./deploy.sh"

update: push deploy