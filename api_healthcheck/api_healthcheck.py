from flask import Blueprint, jsonify

health_check = Blueprint('health_check', __name__)

@health_check.route('/healthcheck')
def health():
    # Lógica para verificar a saúde do seu aplicativo
    health_status = True
    if health_status:
        return jsonify({"status": "ok"})
    else:
        return jsonify({"status": "error"})
