.PHONY:
start:
	docker compose up -d

.PHONY:
stop:
	docker compose stop

.PHONY:
reload:
	docker compose down
	docker compose build
	docker compose up -d

.PHONY:
shell:
	docker exec -it -u 1000:1000 python-workshop bash

.PHONY:
shell-root:
	docker exec -it -u root python-workshop bash
