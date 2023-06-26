from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserUpdate(BaseModel):
    username: str = None
    password: str = None
    email: EmailStr = None
    country: str = None


class User(BaseModel):
    username: str
    password: str
    email: EmailStr
    country: str


class CourseUpdate(BaseModel):
    course_name: str = None
    creation_date: datetime = None
    update_date: datetime = None
    description: str = None
    level: str = None


class Course(BaseModel):
    course_name: str
    creation_date: datetime
    update_date: datetime
    description: str
    level: str


class TagUpdate(BaseModel):
    tag_name: str = None


class Tag(BaseModel):
    tag_name: str


class Role(BaseModel):
    role_type: str


class ForumThread(BaseModel):
    name: str
    content: str


class ForumThreadComment(BaseModel):
    content: str
    thread_id: int


class UserForumThreadComment(BaseModel):
    user_id: int
    comment_id: int
    thread_id: int


class RoleAssign(BaseModel):
    role_id: int
    user_id: int


class UserProgress(BaseModel):
    courses_completed: int
    user_id: int


class UserProgressUpdate(BaseModel):
    courses_completed: int = None
    user_id: int = None


class UserSession(BaseModel):
    session_start: datetime
    session_end: datetime
    user_id: int


class SessionUpdate(BaseModel):
    session_start: datetime = None
    session_end: datetime = None
    user_id: int = None


class UserCourse(BaseModel):
    course_id: int
    user_id: int


class CourseRating(BaseModel):
    rating: int
    user_id: int
    course_id: int


class CourseComment(BaseModel):
    comment: str
    user_id: int
    course_id: int


class CourseFaq(BaseModel):
    material: str
    course_id: int


class CourseFaqUpdate(BaseModel):
    material: str = None
    course_id: int = None


class CourseTagAssign(BaseModel):
    tag_id: int
    course_id: int


class Lecture(BaseModel):
    material: str
    name: str
    course_id: int


class LectureUpdate(BaseModel):
    material: str = None
    name: str = None
    course_id: int = None


class Test(BaseModel):
    material: str
    name: str
    course_id: int
    score: int


class TestUpdate(BaseModel):
    material: str = None
    name: str = None
    course_id: int = None
    score: int = None


class UserTest(BaseModel):
    user_id: int
    course_id: int
    test_id: int


class Assignment(BaseModel):
    name: str
    material: str
    lecture_id: int
    course_id: int


class UserAssignments(BaseModel):
    user_id: int
    assignment_id: int
    lecture_id: int
    course_id: int


class Certificate(BaseModel):
    certificate: str
    user_id: int
    course_id: int


class CertificateUpdate(BaseModel):
    certificate: str = None
    user_id: int = None
    course_id: int = None


class UserForumThread(BaseModel):
    user_id: int
    thread_id: int
