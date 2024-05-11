from flask_restful import Resource, reqparse
from flask import jsonify
from utils.logger import logger

class Index(Resource):
    def get(self):
        logger.info('Solicitação GET recebida em /')
        return "Bem-vindo à API!"
