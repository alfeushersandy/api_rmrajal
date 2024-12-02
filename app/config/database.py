import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# load environtment variable 
load_dotenv()

class Database():
    def __init__(self):
        self.host = os.getenv('DB_HOST')
        self.port = os.getenv('DB_PORT')
        self.name = os.getenv('DB_NAME')
        self.user = os.getenv('DB_USERNAME')
        self.password = os.getenv('DB_PASSWORD')
        self.driver = os.getenv('DB_DRIVER')

        # membuat connection string 
        self.connection_string = (
            f'mssql+pyodbc://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}'
            f'?driver={self.driver}'
        )

        self.engine = create_engine(self.connection_string)
        self.session = scoped_session(sessionmaker(bind=self.engine))

        try: 
            connection = self.engine.connect()
            print('Berhasil Connect ke database')
            connection.close()
        except Exception as e:
            print(f'Gagal Koneksi Ke database : {e}')

    def get_connection(self):
        return self.engine
    
    def get_session(self):
        return self.session

