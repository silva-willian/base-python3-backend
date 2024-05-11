from flask import Flask
from flask_restful import Api
from routes import index_route, receive_data_route
from api_healthcheck.api_healthcheck import health_check

app = Flask(__name__)

# Configuração do healthcheck
app.register_blueprint(health_check)

api = Api(app)

api.add_resource(receive_data_route.ReceiveData, '/api/receive_data')
api.add_resource(index_route.Index, '/')

if __name__ == '__main__':
    app.run(debug=True)
