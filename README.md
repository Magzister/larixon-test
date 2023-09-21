To start the server you should run the following commands in a root directory:
1. <code>docker compose build</code>
2. <code>docker compose run --rm app sh -c "python manage.py createsuperuser"</code>
3. <code>docker compose up</code>
The server will be accessible via localhost:8000