from sqlalchemy import Table, MetaData, select, insert, update, delete
from app.config.database import Database

class UserModel(): 
    def __init__(self):
        self.db = Database()
        self.engine = self.db.get_connection()
        self.metadata = MetaData()

        # definisi table 
        self.user = Table('pde_user', self.metadata, autoload_with=self.engine)

    def get_all_user(self):
        with self.engine.connect() as connection:
            query = select(self.user)
            result = connection.execute(query)
            return result.fetchall()
        
        
            

