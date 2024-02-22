from openai import OpenAI
import logging

logger = logging.getLogger(__name__)


class ColorPalette:
    @staticmethod
    def generate_color(prompt_qsn, api_key) -> list:
        """
        This function generates the color by providing the question in the prompt
        :param prompt_qsn: The question passed from user
        :param api_key: OpenAI API key
        :return: list of colors in Hex code
        """
        try:
            prompt = f"""
                        You are a color palette-generating assistant that responds to text prompts for color palettes.
                        You should generate color palettes that fit the theme, mood, or instructions in the prompt.
                        The palettes should be between 2 and 8 colors.

                        Q: Convert the verbal description of a color palette into a list of colors: a beautiful sunset
                        A: ['#FF6F40', '#FF8A40', '#FFAA40', '#FFC040', '#FFDE40']

                        Q: Convert the verbal description of a color palette into a list of colors: tropical ocean
                        A: ["#0FBCEB", "#1A92B6", "#164D57", "#02456A"]

                        Q: Convert the verbal description of a color palette into a list of colors: {prompt_qsn}
                        A: 
                        """
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                messages=[
                    {
                        "role": "assistant",
                        "content": prompt
                    }
                ],
                model="gpt-3.5-turbo",
            )
            colors = response.choices[0].message.content
            return eval(colors)
        except Exception as e:
            logger.info("Exception occurs in generate_color \t" + str(e))
            return []
