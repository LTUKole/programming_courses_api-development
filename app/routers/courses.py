from fastapi import APIRouter
from database.courses_db import CoursesDb
from typing import Optional
from datetime import datetime
from database.data_models import (
    Course,
    CourseRating,
    CourseComment,
    CourseFaq,
    CourseTagAssign,
    Lecture,
    Assignment,
    Test,
    CourseUpdate,
    CourseFaqUpdate,
    LectureUpdate,
    TestUpdate,
)

router = APIRouter()


@router.put("/course/tests/{tests_id}", response_model=TestUpdate)
async def update_test(tests_id: int, test: TestUpdate):
    db = CoursesDb()
    return db.update_test(tests_id, test)


@router.put("/course/lectures/{lecture_id}", response_model=LectureUpdate)
async def update_lecture(lecture_id: int, lecture: LectureUpdate):
    db = CoursesDb()
    return db.update_lecture(lecture_id, lecture)


@router.put("/course/faq/{faq_id}", response_model=CourseFaqUpdate)
async def update_course_faq(course_id: int, faq: CourseUpdate):
    db = CoursesDb()
    return db.update_course_faq(course_id, faq)


@router.put("/course/{courses_id}", response_model=CourseUpdate)
async def update_course(course_id: int, course: CourseUpdate):
    db = CoursesDb()
    return db.update_course(course_id, course)


@router.get("/courses")
async def get_courses(
    course_name: Optional[str] = None,
    creation_date: Optional[datetime] = None,
    update_date: Optional[datetime] = None,
    description: Optional[str] = None,
    level: Optional[str] = None,
):
    db = CoursesDb()
    return db.get_courses(course_name, creation_date, update_date, description, level)


@router.get("/courses/faq")
async def get_course_faq(
    courses_id: Optional[int] = None,
):
    db = CoursesDb()
    return db.get_course_faq(courses_id)


@router.get("/courses/lectures")
async def get_course_lectures(
    name: Optional[str] = None,
    courses_id: Optional[int] = None,
):
    db = CoursesDb()
    return db.get_course_lectures(name, courses_id)


@router.get("/courses/lectures/assignments")
async def get_lectures_assignments(
    name: Optional[str] = None,
    lecture_id: Optional[int] = None,
):
    db = CoursesDb()
    return db.get_lectures_assignments(name, lecture_id)


@router.get("/courses/tests")
async def get_course_tests(
    name: Optional[str] = None,
    courses_id: Optional[datetime] = None,
    score: Optional[datetime] = None,
):
    db = CoursesDb()
    return db.get_course_tests(name, courses_id, score)


@router.post("/courses/")
async def create_course(course: Course):
    db = CoursesDb()
    return db.create_course(course)


@router.post("/courses/rating")
async def rate_course(course_rating: CourseRating):
    db = CoursesDb()
    return db.rate_course(course_rating)


@router.post("/courses/comment")
async def comment_course(course_comment: CourseComment):
    db = CoursesDb()
    return db.comment_course(course_comment)


@router.post("/courses/faq")
async def create_course_faq(course_faq: CourseFaq):
    db = CoursesDb()
    return db.create_course_faq(course_faq)


@router.post("/courses/tag")
async def assign_course_tag(assign_course_tag: CourseTagAssign):
    db = CoursesDb()
    return db.assign_course_tag(assign_course_tag)


@router.post("/courses/lectures")
async def create_lecture(lecture: Lecture):
    db = CoursesDb()
    return db.create_lecture(lecture)


@router.post("/courses/lectures/assignments")
async def create_assignment(assingment: Assignment):
    db = CoursesDb()
    return db.create_assignment(assingment)


@router.post("/courses/tests")
async def create_test(test: Test):
    db = CoursesDb()
    return db.create_test(test)


@router.delete("/courses/{course_id}")
async def delete_user(course_id: int):
    db = CoursesDb()
    return db.delete_course(course_id)


@router.delete("/courses/{course_id}/users/{user_id}/ratings")
async def delete_rating(course_id: int, user_id: int):
    db = CoursesDb()
    return db.delete_rating(course_id, user_id)


@router.delete("/courses/{course_id}/users/{user_id}/comments")
async def delete_comment(course_id: int, user_id: int):
    db = CoursesDb()
    return db.delete_comment(course_id, user_id)


@router.delete("/courses/faq/{faq_id}/")
async def delete_course_faq(faq_id: int):
    db = CoursesDb()
    return db.delete_course_faq(faq_id)


@router.delete("/courses/{course_id}/tags/{tag_id}/")
async def delete_course_tag(course_id: int, tag_id: int):
    db = CoursesDb()
    return db.delete_course_tag(course_id, tag_id)


@router.delete("/courses/lectures/{lecture_id}/")
async def delete_lecture(lecture_id: int):
    db = CoursesDb()
    return db.delete_lecture(lecture_id)


@router.delete("/courses/tests/{test_id}/")
async def delete_test(test_id: int):
    db = CoursesDb()
    return db.delete_test(test_id)


@router.delete("/courses/assignments/{assignment_id}/")
async def delete_assignment(assignment_id: int):
    db = CoursesDb()
    return db.delete_assignment(assignment_id)
