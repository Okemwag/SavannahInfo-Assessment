build:
	docker compose build

run:
	docker compose up -d --force-recreate

down:
	docker compose down

restart:
	docker compose restart

logs:
	docker compose logs -f

migrate:
	docker compose run --rm backend sh -c "python manage.py makemigrations"
	docker compose run --rm backend sh -c " python manage.py migrate"

createsuperuser:
	docker compose run --rm backend sh -c "python manage.py createsuperuser"

test:
	docker compose run --rm backend sh -c "python manage.py test"

shell:
	docker compose run --rm backend sh -c "python manage.py shell"

delete-volume:
	docker compose down
	docker volume rm postgres_data

