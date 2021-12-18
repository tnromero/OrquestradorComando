from flask_restful import Resource

class Executor(Resource):
    """Executor de comandos"""

    def get(self, id_projeto):

        print(f'ID_Projeto = {id_projeto}')

        return {'message': f'id_projeto={id_projeto}'}, 202