from flask_restplus import fields
from application import api
from werkzeug.datastructures import FileStorage

user_fields = api.model('Text Generation', {
    'Input Data': fields.String(required=False)
})
download_fields = api.model('Download Model', {
    'Model Name': fields.String(required=False)
})

upload_parser = api.parser()
upload_parser.add_argument('file', location='files',type=FileStorage)