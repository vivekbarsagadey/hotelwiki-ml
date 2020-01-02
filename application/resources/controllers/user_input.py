from flask_restplus import fields
from application import api

user_fields = api.model('Text Generation', {
    'Input Data': fields.String(required=False)
})
download_fields = api.model('Download Model', {
    'Model Name': fields.String(required=False)
})
