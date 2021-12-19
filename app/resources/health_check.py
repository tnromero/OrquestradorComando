from flask_restful import Resource


class HealthCheckResource(Resource):
    """Health Check"""

    def get(self):

        mensagem = {
            'conteudo': 'Serviço ativo'
        }

        return mensagem, 202