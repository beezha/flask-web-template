# flask-web-template
Flask Web Template

## Initializing the database
```python
from thermos import db
from thermos.models import User, Bookmark

db.create_all()
```

## Adding user record
```python
from thermos import db
from thermos.models import User

u=User(username="milagan", email="milagan@email.com")
db.session.add(u)
db.session.commit()
```

### Querying the table
```python
from thermos.models import User

User.query.get(1)
User.query.filter_by(username="milagan").all()
```

### Manage script
```shell script
python manage.py
python manage.py drop_db
python manage.py insert_data
python manage.py runserver
```

### DB migration
```shell script
python manage.py db init
python manage.py db migrate -m "initial"
```

### Upgrade database to latest version
```shell script
python manage.py db upgrade
python manage.py db downgrade
python manage.py db downgrade --tag initial
```
