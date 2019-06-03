from application.resources.recommender.user_input import user_fields, upload_parser
from application.resources.recommender.feat_extraction import User
from flask_restplus import Resource
from application import api
from flask import request

recommender = api.namespace('giveRecommendation', description='Operations related to Recommendation')

@recommender.route('/', endpoint='/giveRecommendation')
class recommenderController(Resource):

    @api.expect(upload_parser, validate=False)
    def get(self):
        return 'Recommendation GET method Called'

    @api.expect(user_fields, validate=False)
    @api.doc(responses={
        200: 'Recommendation Given',
        400: 'Validation Error'
    })
    def post(self):
        json_data = request.get_json(force=True)
        user = User(json_data)
        data = user.preProcessing()
        print(data)
        return json_data
