import sqlalchemy as db
from dotenv import load_dotenv
import os


class DatabaseConnection:
    def __init__(self) -> None:
        self.get_db_creds()
        self.db_engine = self.create_connection()
        self.metadata = self.get_metadata()

    def get_db_creds(self) -> None:
        load_dotenv()

    def create_connection(self) -> object:
        db_engine = db.create_engine(
            f"mysql+pymysql://{os.getenv('USERNAME')}:{os.getenv('PASSWORD')}@{os.getenv('HOST')}/{os.getenv('DATABASE')}"
        )
        return db_engine

    def get_metadata(self) -> db.MetaData:
        return db.MetaData()
