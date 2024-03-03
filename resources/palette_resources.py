from flask.views import MethodView
from flask import  render_template
from flask_smorest import Blueprint

from openai import OpenAI
import os, logging
from schema import PaletteInputSchema, PaletteOutputSchema
from utility import ColorPalette


logger = logging.getLogger(__name__)
blp = Blueprint("Palette", __name__, description="Operation on Palette")

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


@blp.route("/")
class Index(MethodView):
    def get(self):
        return render_template("index.html")

@blp.route("/healthcheck")
class HealthCheck(MethodView):
    @blp.response(status_code=200)
    def get(self):
        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "assistant",
                    "content": "How are you?"
                }
            ],
            model="gpt-3.5-turbo",
            temperature=0.4,
            frequency_penalty=0
        )
        return response.choices[0].message.content
        return render_template("index.html")

@blp.route("/palette/")
class Palette(MethodView):
    @blp.arguments(schema=PaletteInputSchema, location='json')
    @blp.response(status_code=200)
    def post(self, palette_data):
        try:
            colors = ColorPalette.generate_color(prompt_qsn=palette_data.get("question"), api_key=OPENAI_API_KEY)
            return colors
        except Exception as e:
            logger.info(f"exception occur at {Palette.__name__} \t" + str(e))
            return []
