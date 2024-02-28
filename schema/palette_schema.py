from marshmallow import Schema, fields


class PaletteInputSchema(Schema):
    """
    This class is used to take query parameter of color palette generation
    """
    question = fields.Str(required=True)



class PaletteOutputSchema(Schema):
    """
    This class is defining the response body of color generations
    """
    colors = fields.List(fields.Str, required=True)
