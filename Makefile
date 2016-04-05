.PHONY: clean-pyc

help:
	@echo "migrate - makemigrations and migrate"
	@echo "clean - remove migrations folders and excute makemigrations and migrate"
	@echo "clean-all - remove migrations folders and excute makemigrations and migrate. Create Super User"

migrate:
	@echo "Start makemigrations"
	python3 manage.py makemigrations
	@echo "==============================================================================="
	@echo "Start migrate"
	python3 manage.py migrate

clean:
	@echo "Remove migrations folders and migrations files"
	rm -f fromleaf_*/migrations/000*
	rm -f darly/migrations/000*
	@echo "==============================================================================="
	@echo "Start makemigrations"
	python3 manage.py makemigrations
	@echo "==============================================================================="
	@echo "Start migrate"
	python3 manage.py migrate

clean-all:
	@echo "Remove migrations folders and migrations files"
	rm -f fromleaf_*/migrations/000*
	rm -f darly/migrations/000*
	@echo "Remove db.sqlite3"
	rm -f db.sqlite3
	@echo "==============================================================================="
	@echo "Start makemigrations"
	python3 manage.py makemigrations
	@echo "Start migrate"
	python3 manage.py migrate
	@echo "==============================================================================="
	@echo "Create Super User - Default: yoon"
	python3 manage.py createsuperuser --username yoon --email test@test.com
