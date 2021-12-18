from typing import List
import os.path
from db.db import DB


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
            id_comando_atual = self.__buscar_id_proximo_comando(id_comando_atual)
        
        print(f'Finalizando execucao do projeto {self.id_projeto}')
        print(f'Ocorrencia: {self.id_execucao_projeto}')


    def __buscar_conteudo_comando(self) -> str:
        return "Comando Aleatorio"

    def __buscar_id_proximo_comando(self, id_comando_atual:int=None) -> int:

        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'OrquestradorComandos.db')

        db = DB(db_path)
        print(db_path)

        db.conectar()

        if id_comando_atual:
            comando = f'select id_comando_sucessora from OrdemExecucao where id_comando_predecessora = {id_comando_atual}'
        else:
            comando = 'select ' + \
                        f'case when (select count(*) from comando where Id_Projeto = {self.id_projeto}) = 1 ' + \
                        'then' + \
                        f'    (select Id_Comando from comando where Id_Projeto = {self.id_projeto})  ' + \
                        'else' + \
                        '    (select cm.Id_Comando from Comando cm' + \
                        '    inner join OrdemComando oc_pre' + \
                        '    on cm.id_comando = oc_pre.Id_Comando_Predecessor' + \
                        '    left join OrdemComando oc_suc' + \
                        '    on cm.Id_Comando = oc_suc.Id_Comando_Sucessor' + \
                        f'    where cm.Id_Projeto = {self.id_projeto} '+ \
                        '     and oc_suc.Id_Comando_Sucessor is null)  ' + \
                        'END Id_Comando;'
        resultado = db.exec_comando(comando)
        print(f'Retorno DB -> {resultado}')
        db.desconectar()

        return None