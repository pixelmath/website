import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# instantiate the extensions
db = SQLAlchemy()
toolbar = DebugToolbarExtension()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app(script_info=None):
  app = Flask(__name__)
  app_settings = os.getenv('APP_SETTINGS')
  app.config.from_object(app_settings)
  db.init_app(app)
  migrate.init_app(app, db)
  bcrypt.init_app(app)
  login_manager.init_app(app)

  from app.views.main import main
  app.register_blueprint(main)

  from app.api.api import api
  app.register_blueprint(api)

  @app.shell_context_processor
  def ctx():
    return {'app': app, 'db': db}
  return app
