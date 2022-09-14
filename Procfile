release: sh -c 'python manage.py migrate && python manage.py loaddata initial_wishlist_data.json'
web: gunicorn wishlist.wsgi --log-file -
