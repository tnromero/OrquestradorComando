from flask import Flask
from flask_restful import Api

from resources.executor import Executor


app = Flask(__name__)
app.config["DEBUG"] = True
app.config["ENV"] = "Development"

api = Api(app=app)
api.add_resource(Executor, '/executor/<int:id_projeto>')

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

app.run(port=5000)