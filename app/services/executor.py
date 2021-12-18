from typing import List


class ExecutorService():

    def __init__(self, id_projeto, id_execucao_projeto) -> None:
        self.id_projeto = id_projeto
        self.id_execucao_projeto = id_execucao_projeto
    
    def exec_projeto(self):
        print(f'executando projeto: {self.id_projeto}')
        self.__buscar_ordem_execucao()

    
    def __buscar_ordem_execucao(self) -> List[int]:
        pass