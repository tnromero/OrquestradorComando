import uuid
from threading import Thread

from flask_restful import Resource

from services.executor import ExecutorService


class ExecutorResource(Resource):
    """Executor de comandos"""

    def get(self, id_projeto):

        id_execucao_projeto = uuid.uuid4()

        mensagem = {
            'id_projeto': id_projeto,
            'id_execucao_projeto': str(id_execucao_projeto)
        }

        exec = ExecutorService(id_projeto, id_execucao_projeto)
        Thread(target=exec.exec_projeto()).start()

        return mensagem, 202