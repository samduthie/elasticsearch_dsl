To setup run the following commands:

docker-compose run web django-admin.py startproject esdsl .

./start/sh

To reindex use:

./manage.py search_index --rebuild

With thanks to

drf dsl documentation at: https://django-elasticsearch-dsl-drf.readthedocs.io/en/0.15/
pokemon list taken from: https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6

Nice search parameters:

wildcard searching http://0.0.0.0:8000/pokemon/?name__wildcard=*saur