from flask import Flask
from flask_restful import Api
from api_routes import ReceiveData, Index
from api_healthcheck import health_check

app = Flask(__name__)

# Configuração do healthcheck
app.register_blueprint(health_check)

api = Api(app)

api.add_resource(ReceiveData, '/api/receive_data')
api.add_resource(Index, '/')

if __name__ == '__main__':
    app.run(debug=True)
