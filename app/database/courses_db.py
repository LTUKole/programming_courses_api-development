from database.database_connection import DatabaseConnection
from database.data_models import (
    Course,
    CourseRating,
    CourseComment,
    CourseFaq,
    CourseTagAssign,
    Lecture,
    Test,
    Assignment,
    CourseUpdate,
    CourseFaqUpdate,
    LectureUpdate,
    TestUpdate,
)
import sqlalchemy as db
from sqlalchemy import text, update


class CoursesDb(DatabaseConnection):
    def update_test(self, test_id: int, test: TestUpdate) -> dict:
        with self.db_engine.connect() as connection:
            my_table = db.Table("test", self.metadata, autoload_with=connection)
            stmt = (
                update(my_table)
                .where(my_table.c.id == test_id)
                .values(
                    material=test.material if test.material else None,
                    name=test.name if test.name else None,
                    courses_id=test.course_id if test.course_id else None,
                    score=test.score if test.score else None,
                )
            )
            connection.execute(stmt)
            connection.commit()
        return {"message": "Done!"}

    def update_lecture(self, lecture_id: int, lecture: LectureUpdate) -> dict:
        with self.db_engine.connect() as connection:
            my_table = db.Table("lecture", self.metadata, autoload_with=connection)
            stmt = (
                update(my_table)
                .where(my_table.c.id == lecture_id)
                .values(
                    material=lecture.material if lecture.material else None,
                    name=lecture.name if lecture.name else None,
                    courses_id=lecture.course_id if lecture.course_id else None,
                )
            )
            connection.execute(stmt)
            connection.commit()
        return {"message": "Done!"}

    def update_course_faq(self, course_id: int, faq: CourseFaqUpdate) -> dict:
        with self.db_engine.connect() as connection:
            my_table = db.Table("course_faq", self.metadata, autoload_with=connection)
            stmt = (
                update(my_table)
                .where(my_table.c.id == course_id)
                .values(
                    material=faq.material if faq.material else None,
                    courses_id=faq.course_id if faq.courses_id else None,
                )
            )
            connection.execute(stmt)
            connection.commit()
        return {"message": "Done!"}

    def update_course(self, course_id: int, course: CourseUpdate) -> dict:
        with self.db_engine.connect() as connection:
            my_table = db.Table("courses", self.metadata, autoload_with=connection)
            stmt = (
                update(my_table)
                .where(my_table.c.id == course_id)
                .values(
                    course_name=course.course_name if course.course_name else None,
                    creation_date=course.creation_date
                    if course.creation_date
                    else None,
                    update_date=course.update_date if course.update_date else None,
                    description=course.description if course.description else None,
                    level=course.level if course.level else None,
                )
            )
            connection.execute(stmt)
            connection.commit()
        return {"message": "Done!"}

    def get_courses(
        self, course_name, creation_date, update_date, description, level
    ) -> dict:
        with self.db_engine.connect() as connection:
            my_table = db.Table("courses", self.metadata, autoload_with=connection)
            query = db.select(my_table).where(my_table.c.id != None)
            if course_name:
                query = query.where(my_table.c.course_name == course_name)
            if creation_date:
                query = query.where(my_table.c.creation_date == creation_date)
            if update_date:
                query = query.where(my_table.c.update_date == update_date)
            if description:
                query = query.where(my_table.c.description == description)
            if level:
                query = query.where(my_table.c.level == level)
            result = connection.execute(query)
        return [users._asdict() for users in result.fetchall()]

    def get_course_faq(self, course_id: int) -> dict:
        with self.db_engine.connect() as connection:
            my_table = db.Table("course_faq", self.metadata, autoload_with=connection)
            query = db.select(my_table).where(my_table.c.id != None)
            if course_id:
                query = query.where(my_table.c.course_id == course_id)
            result = connection.execute(query)
        return [users._asdict() for users in result.fetchall()]

    def get_course_tests(self, name: str, courses_id: int, score: int) -> dict:
        with self.db_engine.connect() as connection:
            my_table = db.Table("tests", self.metadata, autoload_with=connection)
            query = db.select(my_table).where(my_table.c.id != None)
            if name:
                query = query.where(my_table.c.name == name)
            if courses_id:
                query = query.where(my_table.c.courses_id == courses_id)
            if score:
                query = query.where(my_table.c.score == score)
            result = connection.execute(query)
        return [users._asdict() for users in result.fetchall()]

    def get_course_lectures(self, name: str, courses_id: int) -> dict:
        with self.db_engine.connect() as connection:
            my_table = db.Table("lecture", self.metadata, autoload_with=connection)
            query = db.select(my_table).where(my_table.c.id != None)
            if name:
                query = query.where(my_table.c.name == name)
            if courses_id:
                query = query.where(my_table.c.courses_id == courses_id)
            result = connection.execute(query)
        return [users._asdict() for users in result.fetchall()]

    def get_lectures_assignments(self, name: str, lecture_id: int) -> dict:
        with self.db_engine.connect() as connection:
            my_table = db.Table("assignments", self.metadata, autoload_with=connection)
            query = db.select(my_table).where(my_table.c.id != None)
            if name:
                query = query.where(my_table.c.name == name)
            if lecture_id:
                query = query.where(my_table.c.lecture_id == lecture_id)
            result = connection.execute(query)
        return [users._asdict() for users in result.fetchall()]

    def create_course(self, course: Course) -> dict:
        with self.db_engine.connect() as connection:
            procedure_call = text(
                "CALL sp_InsertCourse(:course_name, :creation_date, :update_date, :description, :level)"
            )
            params = {
                "course_name": course.course_name,
                "creation_date": course.creation_date,
                "update_date": course.update_date,
                "description": course.description,
                "level": course.level,
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "Course created successfully!"}

    def rate_course(self, course_rating: CourseRating) -> dict:
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_InsertRating(:rating, :user_id, :course_id)")
            params = {
                "rating": course_rating.rating,
                "user_id": course_rating.user_id,
                "course_id": course_rating.course_id,
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "Course rated successfully!"}

    def comment_course(self, course_comment: CourseComment) -> dict:
        with self.db_engine.connect() as connection:
            procedure_call = text(
                "CALL sp_InsertComment(:comment, :user_id, :course_id)"
            )
            params = {
                "comment": course_comment.comment,
                "user_id": course_comment.user_id,
                "course_id": course_comment.course_id,
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "Course commented successfully!"}

    def create_course_faq(self, course_faq: CourseFaq) -> dict:
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_InsertCourseFaq(:material, :course_id)")
            params = {
                "material": course_faq.material,
                "course_id": course_faq.course_id,
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "Course faq created successfully!"}

    def assign_course_tag(self, assign_course_tag: CourseTagAssign) -> dict:
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_InsertCourseTags(:tag_id, :course_id)")
            params = {
                "tag_id": assign_course_tag.tag_id,
                "course_id": assign_course_tag.course_id,
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "Course tag assigned successfully!"}

    def create_lecture(self, lecture: Lecture) -> dict:
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_InsertLecture(:material, :name, :course_id)")
            params = {
                "material": lecture.material,
                "name": lecture.name,
                "course_id": lecture.course_id,
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "Lecture created successfully!"}

    def create_test(self, test: Test) -> dict:
        with self.db_engine.connect() as connection:
            procedure_call = text(
                "CALL sp_InsertTest(:material, :name, :course_id, :score)"
            )
            params = {
                "material": test.material,
                "name": test.name,
                "course_id": test.course_id,
                "score": test.score,
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "Test created successfully!"}

    def create_assignment(self, assingment: Assignment) -> dict:
        with self.db_engine.connect() as connection:
            procedure_call = text(
                "CALL sp_InsertAssignment(:name, :material, :lecture_id, :course_id)"
            )
            params = {
                "name": assingment.name,
                "material": assingment.material,
                "lecture_id": assingment.lecture_id,
                "course_id": assingment.course_id,
            }
            connection.execute(procedure_call, params)
            connection.commit()
        return {"message": "Assignment created successfully!"}

    def delete_course(self, course_id: int):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_DeleteCourse(:course_id)")
            connection.execute(procedure_call, {"course_id": course_id})
            connection.commit()
        return {"message": "Course deleted successfully!"}

    def delete_rating(self, course_id: int, user_id: int):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_DeleteRating(:user_id, :course_id)")
            connection.execute(
                procedure_call, {"course_id": course_id, "user_id": user_id}
            )
            connection.commit()
        return {"message": "Rating deleted successfully!"}

    def delete_comment(self, course_id: int, user_id: int):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_DeleteComment(:user_id, :course_id)")
            connection.execute(
                procedure_call, {"course_id": course_id, "user_id": user_id}
            )
            connection.commit()
        return {"message": "Comment deleted successfully!"}

    def delete_course_faq(self, faq_id: int):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_DeleteCourseFaq(:faq_id)")
            connection.execute(procedure_call, {"course_id": faq_id})
            connection.commit()
        return {"message": "Course FAQ deleted successfully!"}

    def delete_course_tag(self, course_id: int, tag_id: int):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_DeleteCourseTag(:tag_id, :course_id)")
            connection.execute(
                procedure_call, {"course_id": course_id, "tag_id": tag_id}
            )
            connection.commit()
        return {"message": "Course Tag deleted successfully!"}

    def delete_lecture(self, lecture_id: int):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_DeleteLecture(:lecture_id)")
            connection.execute(procedure_call, {"lecture_id": lecture_id})
            connection.commit()
        return {"message": "Course Lecture deleted successfully!"}

    def delete_test(self, test_id: int):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_DeleteTest(:test_id)")
            connection.execute(procedure_call, {"test_id": test_id})
            connection.commit()
        return {"message": "Course Test deleted successfully!"}

    def delete_assignment(self, assignment_id: int):
        with self.db_engine.connect() as connection:
            procedure_call = text("CALL sp_DeleteAssignment(:assignment_id)")
            connection.execute(procedure_call, {"assignment_id": assignment_id})
            connection.commit()
        return {"message": "Course Assignment deleted successfully!"}
