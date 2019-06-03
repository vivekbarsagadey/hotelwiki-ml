from flask_restplus import fields
from application import api
from werkzeug.datastructures import FileStorage

user_fields = api.model('FoodRecommendation', {
    'age': fields.Integer(required=False),
    'Group': fields.String(required=False),
    'Mood': fields.String(required=False),
    'Gender': fields.String(required=False),
    'Timing': fields.String(required=False),
    'Waiting Time': fields.Integer(required=False)
})


upload_parser = api.parser()
upload_parser.add_argument('file', location='files',type=FileStorage)