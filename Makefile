build:
	docker build . -t dmd3eorg/mercure-munge-tags:latest

push: build
	docker push dmd3eorg/mercure-munge-tags
