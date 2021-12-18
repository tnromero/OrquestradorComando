from typing import List


class ExecutorService():

    def __init__(self, id_projeto, id_execucao_projeto) -> None:
        self.id_projeto = id_projeto
        self.id_execucao_projeto = id_execucao_projeto
    
    def exec_projeto(self):
        print(f'Iniciando execucao do projeto {self.id_projeto}')
        print(f'Ocorrencia: {self.id_execucao_projeto}')
        
        i = 1
        
        id_comando_atual = self.__buscar_id_proximo_comando()
        while id_comando_atual != None:
            print(f'executando comando {i}:\n')
            comando = self.__buscar_conteudo_comando(id_comando_atual)

            print(f'Executando comando: {i}\n{comando}')
            
            i+=1
            id_comando_atual = self.__buscar_id_proximo_comando()
        
        print(f'Finalizando execucao do projeto {self.id_projeto}')
        print(f'Ocorrencia: {self.id_execucao_projeto}')


    def __buscar_conteudo_comando(self) -> str:
        return "Comando Aleatorio"

    def __buscar_id_proximo_comando(self, id_comando_atual:int=None) -> int:
        return None