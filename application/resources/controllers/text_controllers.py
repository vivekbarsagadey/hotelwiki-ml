from application.resources.recommender.user_input import user_fields, download_fields
from application.resources.generator.text_generator import interact_model
from application.resources.generator.download_model import download_model
from flask_restplus import Resource
from application import api
from flask import request

downloader = api.namespace('downloadmodel', description='Operations to download Model')
generater = api.namespace('generatetext', description='Operations related to Text Generation')


@generater.route('/', endpoint='/generatetext/<string:todo_id>')
class RecommenderController(Resource):
    def get(self):
        return 'Generation GET method Called'

    @api.expect(user_fields, validate=False)
    @api.doc(responses={
        200: 'Words Generated',
        400: 'Validation Error'
    })
    def post(self):
        json_data = request.get_json(force=True)
        out = json_data['Input Data']
        print(type(out))
        genrated_data = interact_model(out)
        print(genrated_data)
        return genrated_data


@downloader.route('/', endpoint='/downloadmodel')
class DownloadController(Resource):

    @api.expect(download_fields, validate=False)
    @api.doc(responses={
        200: 'Model Downloaded',
        400: 'Validation Error'
    })
    def post(self):
        json_data = request.get_json(force=True)
        out = json_data['Model Name']
        return download_model(out)
