from flask import Flask
from flask_smorest import Api
from resources import PaletteBlueprint
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), 'src/.flaskenv')
load_dotenv(dotenv_path=dotenv_path)


# app = Flask(__name__, template_folder='templates')


# @app.route("/palette", methods=["POST"])
# def prompt_to_palette():
#     app.logger.info("inside palette")
#     return {"message": "success"}


# @app.route("/")
# def index():
#     response = client.chat.completions.create(
#         messages=[
#             {
#                 "role": "assistant",
#                 "content": "How are you?"
#             }
#         ],
#         model="gpt-3.5-turbo",
#     )
#     return response.choices[0].message.content
#     return render_template("index.html")


def create_app(db_url=None):
    app = Flask(__name__, template_folder='templates')
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Color palette REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    app.config["SQLALCHEMY_DATABASE_URI"] = '{engine}://{user}:{password}@{host}:{port}/{database}'.format(
        engine=os.environ.get("ENGINE"),
        user=os.environ.get("USER"),
        password=os.environ.get("PASSWORD"),
        host=os.environ.get("localhost"),
        port=os.environ.get("PORT"),
        database=os.environ.get("DATABASE")
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    api = Api(app)
    api.register_blueprint(PaletteBlueprint)
    return app
