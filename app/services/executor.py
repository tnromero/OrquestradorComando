from typing import List
import os.path
import time
from db.db import DB


class ExecutorService():

    def __init__(self, id_projeto, id_execucao_projeto) -> None:
        self.id_projeto = id_projeto
        self.id_execucao_projeto = id_execucao_projeto

        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(base_dir, 'OrquestradorComandos.db')
    
    def exec_projeto(self):

        # O Sleep é apenas para evidenciar que a thread está em processamento após o retorno
        time.sleep(10)
        print(f'Iniciando execucao do projeto {self.id_projeto}')
        print(f'Ocorrencia: {self.id_execucao_projeto}')
        
        i = 1
        
        id_comando_atual = self.__buscar_id_proximo_comando()
        while id_comando_atual != None:
            
            comando = self.__buscar_conteudo_comando(id_comando_atual)

            print(f'Executando comando: {i}\n{comando}')
            
            i+=1
            id_comando_atual = self.__buscar_id_proximo_comando(id_comando_atual)
        
        print(f'Finalizando execucao do projeto {self.id_projeto}')
        print(f'Ocorrencia: {self.id_execucao_projeto}')


    def __buscar_conteudo_comando(self, id_comando:int) -> str:
        
        key_conteudo_comando = 'Conteudo_Comando'
        db = DB(self.db_path)

        db.conectar()
        comando = f'select {key_conteudo_comando} from Comando where Id_Comando = {id_comando}'
        resultado_row=db.exec_comando(comando)
        if len(resultado_row):
            value_conteudo_comando = resultado_row[0][key_conteudo_comando]
        else:
            value_conteudo_comando = None
        db.desconectar()

        return value_conteudo_comando


    def __buscar_id_proximo_comando(self, id_comando_atual:int=None) -> int:

        key_id_comando = "Id_Comando"
        db = DB(self.db_path)
        
        db.conectar()

        if id_comando_atual:
            comando = f'select Id_Comando_Sucessor as {key_id_comando} from OrdemComando where Id_Comando_Predecessor = {id_comando_atual}'
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
                        f'END {key_id_comando};'
        resultado_row = db.exec_comando(comando)
        print(f'Retorno DB -> {resultado_row}')
        print(f'Tamanho resultado_row: {len(resultado_row)}')
        if len(resultado_row):
            id_comando_proximo = resultado_row[0][key_id_comando]
        else:
            id_comando_proximo = None
        db.desconectar()

        return id_comando_proximo