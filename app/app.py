from flask import Flask
from flask_restful import Api
from resources.health_check import HealthCheckResource

from resources.executor import ExecutorResource


app = Flask(__name__)
app.config["DEBUG"] = True
app.config["ENV"] = "Development"

api = Api(app=app)
api.add_resource(HealthCheckResource, '/')
api.add_resource(ExecutorResource, '/executor/<int:id_projeto>')

app.run(host="0.0.0.0", port=5001)