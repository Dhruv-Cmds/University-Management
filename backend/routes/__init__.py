from .auth import (
    create_admin,
    login,
    get_admin_by_id,
    get_all_admin,
    delete_admin_by_id
)

from .courses import (
    create_course,
    get_all_courses,
    get_course_by_id,
    delete_course
)

from .enrollments import (

    create_enrollment,
    get_all_enrollments,
    get_enrollment_by_id,
    delete_enrollment
)

from .faculty import (
    create_faculty,
    get_faculty_by_id,
    get_all_faculties,
    delete_faculty
)

from .students import (
    create_student,
    get_student_by_id,
    get_all_students,
    delete_student
)