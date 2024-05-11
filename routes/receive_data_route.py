from flask_restful import Resource, reqparse
from flask import jsonify
from utils.logger import logger

class ReceiveData(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('field1', type=str, required=True, help='Field 1 is required')
        parser.add_argument('field2', type=str, required=True, help='Field 2 is required')
        args = parser.parse_args()

        field1 = args['field1']
        field2 = args['field2']

        logger.info('Dados recebidos: %s, %s', field1, field2)

        return jsonify({"status": "success", "field1": field1, "field2": field2})