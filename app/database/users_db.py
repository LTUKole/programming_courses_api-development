from database.database_connection import DatabaseConnection
from database.data_models import (
    User,
    RoleAssign,
    UserProgress,
    UserSession,
    UserCourse,
    UserTest,
    UserAssignments,
    Certificate,
    UserForumThread,
    UserForumThreadComment,
    UserUpdate,
    SessionUpdate,
    UserProgressUpdate,
    CertificateUpdate,
)
import sqlalchemy as db
from sqlalchemy import text, update


class UsersDb(DatabaseConnection):
    def update_certificate(
        self, certificate_id: int, certificate_data: CertificateUpdate
    ) -> dict:
        with self.db_engine.connect() as connection:
            my_table = db.Table("certificates", self.metadata, autoload_with=connection)
            stmt = (
                update(my_table)
                .where(my_table.c.id == certificate_id)
                .values(
                    certificate=certificate_data.certificate
                    if certificate_data.certificate
                    else None,
                    users_id=certificate_data.user_id
                    if certificate_data.user_id
                    else None,
                    courses_id=certificate_data.course_id
                    if certificate_data.course_id
                    else None,
                )
            )
            connection.execute(stmt)
            connection.commit()
        return {"message": "Done!"}

    def update_user_progress(
        self, user_progress_id: int, user_progress: UserProgressUpdate
    ) -> dict:
        with self.db_engine.connect() as connection:
            my_table = db.Table(
                "user_progress", self.metadata, autoload_with=connection
            )
            stmt = (
                update(my_table)
                .where(my_table.c.id == user_progress_id)
                .values(
                    courses_completed=user_progress.courses_completed
                    if user_progress.courses_completed
                    else None,
                    user_id=user_progress.user_id if user_progress.user_id else None,
                )
            )
            connection.execute(stmt)
            connection.commit()
        return {"message": "Done!"}

    def update_session(self, session_id: int, session: SessionUpdate) -> dict:
        with self.db_engine.connect() as connection:
            my_table = db.Table("session", self.metadata, autoload_with=connection)
            stmt = (
                update(my_table)
                .where(my_table.c.id == session_id)
                .values(
                    session_start=session.session_start
                    if session.session_start
                    else None,
                    session_end=session.session_end if session.session_end else None,
                    user_id=session.user_id if session.user_id else None,
                )
            )
            connection.execute(stmt)
            connection.commit()
        return {"message": "Done!"}

    def update_user(self, user_id: int, user: UserUpdate) -> dict:
        with self.db_engine.connect() as connection:
            my_table = db.Table("users", self.metadata, autoload_with=connection)
            stmt = (
                update(my_table)
                .where(my_table.c.id == user_id)
                .values(
                    username=user.username if user.username else None,
                    password=user.password if user.password else None,
                    email=user.email if user.email else None,
                    country=user.country if user.country else None,
                )
            )
            connection.execute(stmt)
            connection.commit()
        return {"message": "Done!"}

    def get_users(self, username, password, email, country) -> dict:
        with self.db_engine.connect() as connection:
            my_table = db.Table("users", self.metadata, autoload_with=connection)
            query = db.select(my_table).where(my_table.c.id != None)
            if username:
                query = query.where(my_table.c.username == username)
            if password:
                query = query.where(my_table.c.password == password)
            if email:
                query = query.where(my_table.c.email == email)
            if country:
                query = query.where(my_table.c.country == country)
            result = connection.execute(query)
        return [users._asdict() for users in result.fetchall()]

    def get_sessions(self, session_start, session_end, user_id) -> dict:
        with self.db_engine.connect() as connection:
            my_table = db.Table("session", self.metadata, autoload_with=connection)
            query = db.select(my_table).where(my_table.c.id != None)
            if session_start:
                query = query.where(my_table.c.session_start == session_start)
            if session_end:
                query = query.where(my_table.c.session_end == session_end)
            if user_id:
                query = query.where(my_table.c.user_id == user_id)
            result = connection.execute(query)
        return [users._asdict() for users in result.fetchall()]

    def get_user_progress(self, courses_completed, user_id) -> dict:
        with self.db_engine.connect() as connection:
            my_table = db.Table(
                "user_progress", self.metadata, autoload_with=connection
            )
            query = db.select(my_table).where(my_table.c.id != None)
            if courses_completed:
                query = query.where(my_table.c.courses_completed == courses_completed)
            if user_id:
                query = query.where(my_table.c.user_id == user_id)
            result = connection.execute(query)
        return [users._asdict() for users in result.fetchall()]

    def get_certificates(self, user_id, courses_id) -> dict:
        with self.db_engine.connect() as connection:
            my_table = db.Table("certificates", self.metadata, autoload_with=connection)
            query = db.select(my_table).where(my_table.c.id != None)
            if user_id:
                query = query.where(my_table.c.user_id == user_id)
            if courses_id:
                query = query.where(my_table.c.courses_id == courses_id)
            result = connection.execute(query)
        return [users._asdict() for users in result.fetchall()]

    def insert_users(self, user: User) -> dict:
        with self.db_engine.connect() as connection:
            procedure_call = text(
                "CALL sp_InsertUser(:username, :password, :email, :country)"
            )
            params = {
                "username": user.username,
                "password": user.password,
                "email": user.email,
                "country": user.country,
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "User created successfully!"}

    def assign_user_role(self, user_role_id: RoleAssign):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_InsertUserRole(:role_id, :user_id)")
            params = {
                "role_id": user_role_id.role_id,
                "user_id": user_role_id.user_id,
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "Role assigned successfully!"}

    def insert_user_progress(self, user_progress: UserProgress):
        with self.db_engine.connect() as connection:
            procedure_call = text(
                "CALL sp_InsertUserProgress(:courses_completed, :user_id)"
            )
            params = {
                "courses_completed": user_progress.courses_completed,
                "user_id": user_progress.user_id,
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "User Progress inserted successfully!"}

    def insert_user_session(self, user_session: UserSession):
        with self.db_engine.connect() as connection:
            procedure_call = text(
                "CALL sp_InsertSession(:session_start, :session_end, :user_id)"
            )
            params = {
                "session_start": user_session.session_start,
                "session_end": user_session.session_end,
                "user_id": user_session.user_id,
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "User Session inserted successfully!"}

    def assign_user_course(self, user_course: UserCourse):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_InsertUserCourse(:course_id, :user_id)")
            params = {
                "course_id": user_course.course_id,
                "user_id": user_course.user_id,
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "User Course assigned successfully!"}

    def assign_user_test(self, user_test: UserTest):
        with self.db_engine.connect() as connection:
            procedure_call = text(
                "CALL sp_InsertUserTests(:user_id, :course_id, :test_id)"
            )
            params = {
                "user_id": user_test.user_id,
                "course_id": user_test.course_id,
                "test_id": user_test.test_id,
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "User Test assigned successfully!"}

    def assign_user_assignment(self, user_assignment: UserAssignments):
        with self.db_engine.connect() as connection:
            procedure_call = text(
                "CALL sp_InsertUserAssignments(:user_id, :assignment_id, :lecture_id, :course_id)"
            )
            params = {
                "user_id": user_assignment.user_id,
                "assignment_id": user_assignment.assignment_id,
                "lecture_id": user_assignment.lecture_id,
                "course_id": user_assignment.course_id,
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "User Assignment assigned successfully!"}

    def create_certificate(self, certificate: Certificate):
        with self.db_engine.connect() as connection:
            procedure_call = text(
                "CALL sp_InsertCertificate(:certificate, :user_id, :course_id)"
            )
            params = {
                "certificate": certificate.certificate,
                "user_id": certificate.user_id,
                "course_id": certificate.course_id,
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "Created certificate successfully!"}

    def assign_user_forum_thread(self, user_forum_thread: UserForumThread):
        with self.db_engine.connect() as connection:
            procedure_call = text(
                "CALL sp_InsertCertificate(:certificate, :user_id, :course_id)"
            )
            params = {
                "user_id": user_forum_thread.user_id,
                "thread_id": user_forum_thread.thread_id,
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "User forum thread assigned successfully!"}

    def assign_user_forum_thread_comment(
        self, user_forum_thread_comment: UserForumThreadComment
    ) -> dict:
        with self.db_engine.connect() as connection:
            procedure_call = text(
                "CALL sp_InsertUserForumThreadComment(:user_id, :comment_id, :thread_id)"
            )
            params = {
                "user_id": user_forum_thread_comment.user_id,
                "comment_id": user_forum_thread_comment.comment_id,
                "thread_id": user_forum_thread_comment.thread_id,
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "Forum Thread Comment assigned to User successfully!"}

    def delete_user(self, user_id: int):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_DeleteUser(:user_id)")
            connection.execute(procedure_call, {"user_id": user_id})
            connection.commit()
        return {"message": "User deleted successfully!"}

    def delete_user_role(self, role_id: int, user_id: int):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_DeleteUserRole(:role_id, :user_id)")
            connection.execute(procedure_call, {"role_id": role_id, "user_id": user_id})
            connection.commit()
        return {"message": "User role deleted successfully!"}

    def delete_user_progress(self, user_id: int):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_DeleteUserProgress(:user_id)")
            connection.execute(procedure_call, {"user_id": user_id})
            connection.commit()
        return {"message": "User progress deleted successfully!"}

    def delete_user_forum_thread_comment(
        self, user_id: int, thread_id: int, comment_id: int
    ):
        with self.db_engine.connect() as connection:
            procedure_call = text(
                "CALL sp_DeleteUserForumThreadComment(:user_id, :comment_id, :thread_id)"
            )
            connection.execute(
                procedure_call,
                {"user_id": user_id, "thread_id": thread_id, "comment_id": comment_id},
            )
            connection.commit()
        return {"message": "User Forum Thread Comment deleted successfully!"}

    def delete_user_session(self, session_id: int):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_DeleteSession(:session_id)")
            connection.execute(procedure_call, {"session_id": session_id})
            connection.commit()
        return {"message": "User session deleted successfully!"}

    def delete_user_course(self, user_id: int, course_id: int):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_DeleteUserCourse(:course_id, :user_id)")
            connection.execute(
                procedure_call, {"user_id": user_id, "course_id": course_id}
            )
            connection.commit()
        return {"message": "User course deleted successfully!"}

    def delete_user_test(self, user_id: int, course_id: int, test_id: int):
        with self.db_engine.connect() as connection:
            procedure_call = text(
                "CALL sp_DeleteUserTest(:user_id, :course_id, :test_id)"
            )
            connection.execute(
                procedure_call,
                {"user_id": user_id, "course_id": course_id, "test_id": test_id},
            )
            connection.commit()
        return {"message": "User test deleted successfully!"}

    def delete_user_assignment(
        self, user_id: int, course_id: int, lecture_id: int, assignment_id: int
    ):
        with self.db_engine.connect() as connection:
            procedure_call = text(
                "CALL sp_DeleteUserAssignment(:user_id, :assignment_id, :lecture_id, :course_id)"
            )
            connection.execute(
                procedure_call,
                {
                    "user_id": user_id,
                    "assignment_id": assignment_id,
                    "lecture_id": lecture_id,
                    "course_id": course_id,
                },
            )
            connection.commit()
        return {"message": "User Assingment deleted successfully!"}

    def delete_certificate(self, certificate_id: int):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_DeleteCertificate(:certificate_id)")
            connection.execute(procedure_call, {"certificate_id": certificate_id})
            connection.commit()
        return {"message": "User Certificate deleted successfully!"}

    def delete_user_forum_thread(self, user_id: int, thread_id: int):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_DeleteUserForumThread(:user_id, :thread_id)")
            connection.execute(
                procedure_call, {"user_id": user_id, "thread_id": thread_id}
            )
            connection.commit()
        return {"message": "User Forum thread deleted successfully!"}
