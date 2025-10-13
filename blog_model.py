import sqlite3
from datetime import datetime
from database import DatabaseConnection

class BlogModel: 

    def __init__(self):
        self.db_conn = DatabaseConnection()
        self._create_table()

    def usuarios(self):
        self.db_conn.connect()
        self.db_conn.cursor.execute(
            """"
            CREATE TABLE IF NOT EXISTS usuario (
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,

            );
        """
        )

    def tabela_blogs(self):
        self.db_conn.connect()
        self.db_conn.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS blog (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            conteudo TEXT NOT NULL,
            data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
            data_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP
            id_user 
            );
        """
        )
        self.db_conn.close()