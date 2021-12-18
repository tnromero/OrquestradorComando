from flask import Flask
from flask_restful import Api

from resources.executor import ExecutorResource


app = Flask(__name__)
app.config["DEBUG"] = True
app.config["ENV"] = "Development"

api = Api(app=app)
api.add_resource(ExecutorResource, '/executor/<int:id_projeto>')

app.run(port=5000)