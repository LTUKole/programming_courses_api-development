from database.database_connection import DatabaseConnection
from database.data_models import ForumThread, ForumThreadComment
from sqlalchemy import text
import sqlalchemy as db


class ForumDb(DatabaseConnection):
    def forum_thread(self, name, content) -> dict:
        with self.db_engine.connect() as connection:
            my_table = db.Table(
                "forum_threads", self.metadata, autoload_with=connection
            )
            query = db.select(my_table).where(my_table.c.id != None)
            if name:
                query = query.where(my_table.c.name == name)
            if content:
                query = query.where(my_table.c.content == content)
            result = connection.execute(query)
        return [users._asdict() for users in result.fetchall()]

    def create_forum_thread(self, forum_thread: ForumThread) -> dict:
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_InsertForumThread(:name, :content)")
            params = {
                "name": forum_thread.name,
                "content": forum_thread.content,
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "Forum Thread created successfully!"}

    def insert_forum_thread_comment(
        self, forum_thread_comment: ForumThreadComment
    ) -> dict:
        with self.db_engine.connect() as connection:
            procedure_call = text(
                "CALL sp_InsertForumThreadComment(:content, :thread_id)"
            )
            params = {
                "content": forum_thread_comment.content,
                "thread_id": forum_thread_comment.thread_id,
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "Forum Thread Comment added successfully!"}

    def delete_forum_thread(self, forum_thread_id: int):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_DeleteForumThread(:forum_thread_id)")
            connection.execute(procedure_call, {"forum_thread_id": forum_thread_id})
            connection.commit()
        return {"message": "Forum Thread deleted successfully!"}

    def delete_forum_thread_comment(self, comment_id: int):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_DeleteForumThreadComment(:comment_id)")
            connection.execute(procedure_call, {"comment_id": comment_id})
            connection.commit()
        return {"message": "Forum Thread Comment deleted successfully!"}
