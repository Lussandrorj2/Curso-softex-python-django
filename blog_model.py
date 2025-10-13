import sqlite3
from datetime import datetime
from database import DatabaseConnection

class BlogModel: 

    def __init__(self):
        self.db_conn = DatabaseConnection()
        self.tabela_blogs()

    def tabela_blogs(self):
        self.db_conn.connect()
        self.db_conn.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS blogs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            conteudo TEXT NOT NULL,
            data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
            data_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP
            id_user (criar chave estrangeiro em processo... )
            );
        """
        )
        self.db_conn.close()