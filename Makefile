.PHONY: clean-pyc

help:
	@echo "insertuser - execute manage.py shell < insert_user_data.py"
	@echo "==============================================================================="
	@echo "migrate - execute manage migrate"
	@echo "migrateall - execute manage migrate about all database"
	@echo "migrateothers - execute manage migrate about others database except default database"
	@echo "makemigrations - execute manage makemigrations"
	@echo "supermigrate - execute manage makemigrations and migrate"
	@echo "removemigrations - remove migration folders"
	@echo "clean - remove migrations folders and excute makemigrations and migrate"
	@echo "superclean - remove migrations folders and excute makemigrations and migrate. Create Super User"
	@echo "==============================================================================="


pyc-clean:
	@echo *.pyc file remove
	find . -name '*.pyc' -delete

migrateall:
	@echo manage migrate all database
	python3 manage.py migrate
	python3 manage.py migrate --database=darly
	python3 manage.py migrate --database=ourhockey

migrateothers:
	@echo "Remove others database file"
	rm -f database/darly.db.sqlite3
	@echo manage migrate all database
	python3 manage.py migrate --database=darly

insertuser:
	@echo "if you want to insert user data to database, you have to execute superclean"
	make superclean
	@echo "insert user data to database"
	python3 manage.py shell < insert_user_data.py

makemigrations:
	@echo "Start makemigrations"
	python3 manage.py makemigrations

migrate:
	@echo "Start migrate"
	python3 manage.py migrate

supermigrate:
	@echo "==============================================================================="
	make makemigrations
	@echo "==============================================================================="
	make migrate

removemigrations:
	@echo "Remove migrations folders and migrations files"
	rm -f fromleaf_*/migrations/000*
	rm -f fromleaf_playing/darly/migrations/000*
	rm -f fromleaf_playing/ourhockey/migrations/000*

clean:
	make removemigrations
	@echo "==============================================================================="
	make makemigrations
	@echo "==============================================================================="
	make migrate

superclean:
	make clean
	@echo "Remove default.db.sqlite3"
	rm -f database/default.db.sqlite3
	@echo "==============================================================================="
	make makemigrations
	@echo "==============================================================================="
	make migrate
	@echo "==============================================================================="
	@echo "Create Super User - Default: yoon"
	python3 manage.py createsuperuser --username yoon --email test@test.com
