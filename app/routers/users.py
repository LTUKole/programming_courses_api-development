from fastapi import APIRouter
from database.users_db import UsersDb
from typing import Optional
from datetime import datetime
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

router = APIRouter()


@router.put("/users/certificate/{certificate_id}", response_model=CertificateUpdate)
async def update_certificate(certificate_id: int, certificate: CertificateUpdate):
    db = UsersDb()
    return db.update_certificate(certificate_id, certificate)


@router.put(
    "/users/user_progress/{user_progress_id}", response_model=UserProgressUpdate
)
async def update_user_progress(
    user_progress_id: int, user_progress: UserProgressUpdate
):
    db = UsersDb()
    return db.update_user_progress(user_progress_id, user_progress)


@router.put("/users/sessions/{session_id}", response_model=SessionUpdate)
async def update_session(session_id: int, session: SessionUpdate):
    db = UsersDb()
    return db.update_session(session_id, session)


@router.put("/users/{user_id}", response_model=UserUpdate)
async def update_user(user_id: int, user: UserUpdate):
    db = UsersDb()
    return db.update_user(user_id, user)


@router.get("/users")
async def get_users(
    username: Optional[str] = None,
    password: Optional[str] = None,
    email: Optional[str] = None,
    country: Optional[str] = None,
):
    db = UsersDb()
    return db.get_users(username, password, email, country)


@router.get("/users/user_progress")
async def get_user_progress(
    courses_completed: Optional[int] = None,
    user_id: Optional[str] = None,
):
    db = UsersDb()
    return db.get_user_progress(courses_completed, user_id)


@router.get("/users/certificate")
async def get_certificates(
    user_id: Optional[int] = None,
    courses_id: Optional[int] = None,
):
    db = UsersDb()
    return db.get_certificates(user_id, courses_id)


@router.get("/sessions")
async def get_sessions(
    session_start: Optional[datetime] = None,
    session_end: Optional[datetime] = None,
    user_id: Optional[str] = None,
):
    db = UsersDb()
    return db.get_sessions(session_start, session_end, user_id)


@router.post("/users/")
async def create_user(user: User):
    db = UsersDb()
    return db.insert_users(user)


@router.post("/users/role/")
async def assign_user_role(user_role_id: RoleAssign):
    db = UsersDb()
    return db.assign_user_role(user_role_id)


@router.post("/users/user_progress/")
async def insert_user_progress(user_progress: UserProgress):
    db = UsersDb()
    return db.insert_user_progress(user_progress)


@router.post("/users/user_session/")
async def insert_user_session(user_session: UserSession):
    db = UsersDb()
    return db.insert_user_session(user_session)


@router.post("/users/course/")
async def assign_user_course(user_course: UserCourse):
    db = UsersDb()
    return db.assign_user_course(user_course)


@router.post("/users/course/test")
async def assign_user_test(user_test: UserTest):
    db = UsersDb()
    return db.assign_user_test(user_test)


@router.post("/users/course/assignment")
async def assign_user_assignment(user_assignment: UserAssignments):
    db = UsersDb()
    return db.assign_user_assignment(user_assignment)


@router.post("/users/certificate")
async def create_certificate(certificate: Certificate):
    db = UsersDb()
    return db.assign_user_assignment(certificate)


@router.post("/users/forum_thread")
async def assign_user_forum_thread(user_forum_thread: UserForumThread):
    db = UsersDb()
    return db.assign_user_forum_thread(user_forum_thread)


@router.post("/users/forum_thread/comment")
async def assign_user_forum_thread_comment(
    user_forum_thread_comment: UserForumThreadComment,
):
    db = UsersDb()
    return db.assign_user_forum_thread_comment(user_forum_thread_comment)


@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    db = UsersDb()
    return db.delete_user(user_id)


@router.delete("/users/{user_id}/roles/{role_id}")
async def delete_user_role(role_id: int, user_id: int):
    db = UsersDb()
    return db.delete_user_role(role_id, user_id)


@router.delete("/users/progress/{user_id}")
async def delete_user_progress(user_id: int):
    db = UsersDb()
    return db.delete_user_progress(user_id)


@router.delete("/users/{user_id}/forum_thread/{thread_id}/comment/{comment_id}")
async def delete_user_forum_thread_comment(
    user_id: int, thread_id: int, comment_id: int
):
    db = UsersDb()
    return db.delete_user_forum_thread_comment(user_id, thread_id, comment_id)


@router.delete("/users/user_session/{session_id}")
async def delete_user_session(session_id: int):
    db = UsersDb()
    return db.delete_user_session(session_id)


@router.delete("/users/{user_id}/course/{course_id}")
async def delete_user_course(user_id: int, course_id: int):
    db = UsersDb()
    return db.delete_user_course(user_id, course_id)


@router.delete("/users/{user_id}/course/{course_id}/tests/{test_id}")
async def delete_user_test(user_id: int, course_id: int, test_id: int):
    db = UsersDb()
    return db.delete_user_test(user_id, course_id, test_id)


@router.delete(
    "/users/{user_id}/course/{course_id}/lectures/{lecture_id}/assignments/{assignment_id}"
)
async def delete_user_assignment(
    user_id: int, course_id: int, lecture_id: int, assignment_id: int
):
    db = UsersDb()
    return db.delete_user_assignment(user_id, course_id, lecture_id, assignment_id)


@router.delete("/users/certificates/{certificate_id}")
async def delete_certificate(certificate_id: int):
    db = UsersDb()
    return db.delete_certificate(certificate_id)


@router.delete("/users/{user_id}/forum_thread/{thread_id}")
async def delete_user_forum_thread(user_id: int, thread_id: int):
    db = UsersDb()
    return db.delete_user_forum_thread(user_id, thread_id)
