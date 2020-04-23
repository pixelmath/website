from flask.cli import FlaskGroup
from app import create_app, db, bcrypt
from datetime import datetime, timedelta
import os
from flask import current_app

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command()
def recreate_db():
    if current_app.config.get('ENV') not in ('development', 'test', 'testing'):
       print("ERROR: recreate-db only allowed in development and testing env.")
       return
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command()
def seed_db():
    pass

if __name__ == '__main__':
    cli()
