SHELL := /bin/bash
setup_dev:
	@echo ----------------------------------------------Create Dev Containers------------------------------------------
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml build
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml run django-app ./wait-for-postgres.sh python3 manage.py migrate

run_dev:
	@echo ----------------------------------------------Start Development Server------------------------------------------
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up

migrate:
	@echo ----------------------------------------------RUNNING DJANGO MIGRATIONS PROD----------------------------------------
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml build
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml run django-app python3 manage.py migrate

prod_makemigrations:
	@echo ----------------------------------------------CREATING DJANGO MIGRATIONS PROD----------------------------------------
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml build
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml run django-app python3 manage.py makemigrations

prod_shell:
	@echo ----------------------------------------------DJANGO SHELL PROD----------------------------------------
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml build
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml run django-app python3 manage.py shell

debug_shell:
	@echo ----------------------------------------------STARTING DEBUG----------------------------------------
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml build
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml run django-app python3 manage.py shell

default_objects:
	@echo ----------------------------------------------CREATING SAMPLE OBJECTS----------------------------------------
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml run django-app python3 manage.py create_default_overlays
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml run django-app python3 manage.py get_latest_usgs

debug:
	@echo ----------------------------------------------STARTING DEBUG----------------------------------------
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml build
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up

test: 
	@echo ----------------------------------------------STARTING TESTS----------------------------------------
	@echo -e "\e[46mWant to debug a single test? - don't want to rebuild docker container?\nSee the readme: https://github.com/ISPToolbox/ISPToolbox#debugging-django-tests-with-vscode \e[0m"
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml build
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml run django-app ./wait-for-postgres.sh python3 manage.py test --noinput

static_prod:
	@echo ----------------------------------------------BUIDLING STATIC FILES \& PUSHING TO PROD \(S3\)----------------------------------------
	docker-compose -f docker-compose.yml -f webserver/static/docker-compose.static-prod.yml build
	docker-compose -f docker-compose.yml -f webserver/static/docker-compose.static-prod.yml run static
	@echo This next step may take 5-10 minutes, hashing static files and pushing to S3, commit the new staticfiles.json to git, feel free to try to improve this push step
	docker-compose -f docker-compose.yml -f webserver/static/docker-compose.static-prod.yml run django-app python3 manage.py collectstatic --noinput