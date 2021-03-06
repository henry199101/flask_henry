import os
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, Follow, Role, Permission, Post, Comments

app = create_app(os.getenv('FLASKY_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
	return dict(db=db, User=User, Follow=Follow, Role=Role,
				Permission=Permission, Post=Post, Comments=Comments)


@app.cli.command()
def test():
	"""Run the unit test."""
	import unittest
	tests = unittest.TestLoader().dicover('tests')
	unittest.TextTestRunner(verbosity=2).run(tests)