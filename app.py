from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import ormConfig

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(ormConfig)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from models import models


    # 블루프린트 인스턴스 가져오기
    from routes import routes

    # 플라스크 앱에 등록하기
    app.register_blueprint(routes, url_prefix='/')

    # Home
    @app.route('/')
    def index():
        return "Welcome!"

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
