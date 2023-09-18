from marshmallow import Schema, fields, pre_dump, post_load, validates_schema, ValidationError
from models import Round, Game

class RoundSchema(Schema):
    __model__ = Round
    id = fields.Str()
    min_value = fields.Int()
    max_value = fields.Int()
    guess = fields.Int()
    status = fields.String()
    
class GameSchema(Schema):
    __model__ = Game
    id = fields.Str(dump_only = True)
    min_value = fields.Int(required=True, load_only = True)
    max_value = fields.Int(required=True, load_only = True)
    secret_number = fields.Int(dump_only = True)
    is_over = fields.Boolean(dump_only = True)
    current_round = fields.Nested(RoundSchema, dump_only = True)
    rounds = fields.Nested(RoundSchema, many=True, dump_only = True)
    
    # Compute list of rounds prior to serialization
    @pre_dump()
    def get_data(self, data, **kwargs):
        data.rounds = data.get_rounds()
        data.current_round = data.get_current_round()
        return data
    
    @validates_schema
    def validate_numbers(self, data, **kwargs):
        min_val = data["min_value"]
        max_val = data["max_value"]
        if min_val >= max_val:
            raise ValidationError(f"min_value {min_val} must be less than max_value {max_val}.")
    
class GameUpdateSchema(Schema):
    guess = fields.Int(required=True)
