from database.database_connection import DatabaseConnection
from database.data_models import Tag, Role, TagUpdate
from sqlalchemy import text, update
import sqlalchemy as db


class SysDb(DatabaseConnection):
    def update_tags(self, tags_id: int, tags: TagUpdate) -> dict:
        with self.db_engine.connect() as connection:
            my_table = db.Table("tags", self.metadata, autoload_with=connection)
            stmt = (
                update(my_table)
                .where(my_table.c.id == tags_id)
                .values(
                    tag_name=tags.tag_name if tags.tag_name else None,
                )
            )
            connection.execute(stmt)
            connection.commit()
        return {"message": "Done!"}

    def get_roles(self, role_type: str) -> dict:
        with self.db_engine.connect() as connection:
            my_table = db.Table("roles", self.metadata, autoload_with=connection)
            query = db.select(my_table).where(my_table.c.id != None)
            if role_type:
                query = query.where(my_table.c.role_type == role_type)
            result = connection.execute(query)
        return [users._asdict() for users in result.fetchall()]

    def get_tags(self, tag_name: str) -> dict:
        with self.db_engine.connect() as connection:
            my_table = db.Table("tags", self.metadata, autoload_with=connection)
            query = db.select(my_table).where(my_table.c.id != None)
            if tag_name:
                query = query.where(my_table.c.tag_name == tag_name)
            result = connection.execute(query)
        return [users._asdict() for users in result.fetchall()]

    def create_tag(self, tag: Tag):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_InsertTag(:tag)")
            params = {
                "tag": tag.tag_name,
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "Tag created successfully!"}

    def create_role(self, role: Role):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_InsertRole(:role_type)")
            params = {
                "role_type": role.role_type,
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "Role created successfully!"}

    def delete_tag(self, tag_id: int):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_DeleteTag(:tag_id)")
            connection.execute(procedure_call, {"tag_id": tag_id})
            connection.commit()
        return {"message": "Tag deleted successfully!"}

    def delete_role(self, role_id: int):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_DeleteRole(:role_id)")
            connection.execute(procedure_call, {"role_id": role_id})
            connection.commit()
        return {"message": "Role deleted successfully!"}
