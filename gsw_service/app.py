from flask import Flask
from blueprints import calc_bp


def run_server():
    app = Flask(__name__)

    calculation_bp = calc_bp.construct()
    app.register_blueprint(calculation_bp)
    app.config.update()

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    app.run(host="localhost", port=9998, debug=True)


if __name__ == '__main__':
    run_server()
