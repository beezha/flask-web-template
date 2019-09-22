#! /usr/bin/env python
from flask_migrate import Migrate, MigrateCommand

from thermos import app, db
from thermos.models import User, Bookmark, Tag
from flask_script import Manager, prompt_bool

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


# noinspection PyArgumentList
@manager.command
def insert_data():
    first_user = User(username="milagan", email="milagan@example.com", password="test")
    db.session.add(first_user)

    def add_bookmark(url, description, tags):
        db.session.add(Bookmark(url=url, description=description, user=first_user, tags=tags))

    for name in ["python", "flask", "webdev", "programming", "training", "news", "orm", "databases", "emacs", "gtd",
                 "django"]:
        db.session.add(Tag(name=name))
    db.session.commit()

    add_bookmark("http://www.pluralsight.com", "Pluralsight. Hardcore developer training.",
                 "training,programming,python,flask,webdev")
    add_bookmark("http://www.python.org", "Python - my favorite language", "python")
    add_bookmark("http://flask.pocoo.org", "Flask: Web development one drop at a time.", "python,flask,webdev")
    add_bookmark("http://www.reddit.com", "Reddit. Frontpage of the internet", "news,coolstuff,fun")
    add_bookmark("http://www.sqlalchemyorg", "Nice ORM framework", "python,orm,databases")

    second_user = User(username="milagan1", email="milagan1@example.com", password="test")
    db.session.add(second_user)
    db.session.commit()
    print('Initialized the database')


@manager.command
def drop_db():
    """
    Drops the database.
    """
    if prompt_bool("Are you sure you want to lose all your data"):
        db.drop_all()
        print('Dropped the database')


if __name__ == '__main__':
    manager.run()
