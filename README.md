# flask-web-template
Flask Web Template

## Initializing the database
```
>>> from thermos.thermos import db
>>> from thermos.models import User, Bookmark
>>> db.create_all()
```

## Adding user record
```
>>> u=User(username="milagan", email="milagan@email.com")
>>> db.session.add(u)
>>> db.session.commit()
```

### Querying the table
```
>>> User.query.get(1)
>>> User.query.filter_by(username="milagan").all()
```

### Manage script
```
$ python manage.py
$ python manage.py dropdb
$ python manage.py initdb
$ python manage.py runserver
```