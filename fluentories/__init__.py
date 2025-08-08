from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_babel import Babel
import os

db = SQLAlchemy()
migrate = Migrate()
babel = Babel()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['BABEL_DEFAULT_LOCALE'] = 'ar'
    app.config['BABEL_SUPPORTED_LOCALES'] = ['ar', 'en']

    app.config['BABEL_TRANSLATION_DIRECTORIES'] = '/home/mohammed-almadhoun/Desktop/Folders/my work/fluentories_project_v2/translations'
    db.init_app(app)
    migrate.init_app(app, db)

    def get_locale():
        return session.get('lang', 'ar')

    babel.init_app(app, locale_selector=get_locale)

    from fluentories.routes import routes
    app.register_blueprint(routes)

    return app
