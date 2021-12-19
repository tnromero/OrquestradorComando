import sqlite3

class DB():

    def __init__(self, arquivo_db:str) -> None:
        self.arquivo_db = arquivo_db
    
    def conectar(self) -> None:
        self.conn = sqlite3.connect(self.arquivo_db)
    
    def desconectar(self) -> None:
        self.conn.close()
    
    def exec_comando(self, comando:str) -> str:
        self.conn.row_factory = sqlite3.Row
        cursor = self.conn.cursor()
        cursor.execute(comando)
        resultado = cursor.fetchall()
        cursor.close()
        return resultado