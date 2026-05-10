import http from 'k6/http';
import { check, sleep } from 'k6';


export const options = {
    vus: 1000,
    duration: '60s',
};


const BASE_URL = 'http://localhost:8002';


function randomEmail(prefix = 'user') {
    return `${prefix}${Math.floor(Math.random() * 1000000)}@test.com`;
}


function randomPhone() {
    return `${Math.floor(1000000000 + Math.random() * 9000000000)}`;
}


function signupAndLogin() {

    const email = randomEmail();

    const password = '123456';


    const headers = {
        headers: {
            'Content-Type': 'application/json'
        }
    };


    // =========================
    // SIGNUP
    // =========================

    const signupResponse = http.post(
        `${BASE_URL}/admin/signup`,
        JSON.stringify({
            email: email,
            password: password,
            role: 'admin'
        }),
        headers
    );


    check(signupResponse, {
        'signup success': (r) =>
            r.status === 200 || r.status === 429
    });


    // =========================
    // LOGIN
    // =========================

    const loginResponse = http.post(
        `${BASE_URL}/admin/login`,
        JSON.stringify({
            email: email,
            password: password
        }),
        headers
    );


    check(loginResponse, {
        'login success': (r) =>
            r.status === 200 || r.status === 429
    });


    if (loginResponse.status !== 200) {
        return {
            headers: {}
        };
    }


    const token = loginResponse.json('access_token');


    return {
        headers: {
            Authorization: `Bearer ${token}`,
            'Content-Type': 'application/json'
        }
    };
}


export default function () {

    const authHeaders = signupAndLogin();


    // if login failed
    if (!authHeaders.headers.Authorization) {
        sleep(1);
        return;
    }


    // =========================
    // GET ALL ADMINS
    // =========================

    const adminsGet = http.get(
        `${BASE_URL}/admin/`,
        authHeaders
    );

    check(adminsGet, {
        'get admins': (r) =>
            r.status === 200 || r.status === 429
    });


    // =========================
    // CREATE COURSE
    // =========================

    const courseResponse = http.post(
        `${BASE_URL}/courses/`,
        JSON.stringify({
            course_name:
                `Course_${Math.floor(Math.random() * 1000000)}`
        }),
        authHeaders
    );


    check(courseResponse, {
        'create course': (r) =>
            r.status === 200 || r.status === 429
    });


    let courseId = null;

    try {
        courseId = courseResponse.json('id');
    }
    catch (e) {}


    // =========================
    // GET COURSES
    // =========================

    const coursesGet = http.get(
        `${BASE_URL}/courses/`,
        authHeaders
    );

    check(coursesGet, {
        'get courses': (r) =>
            r.status === 200 || r.status === 429
    });


    // =========================
    // GET COURSE BY ID
    // =========================

    if (courseId) {

        const courseById = http.get(
            `${BASE_URL}/courses/${courseId}`,
            authHeaders
        );

        check(courseById, {
            'get course by id': (r) =>
                r.status === 200 || r.status === 429
        });
    }


    // =========================
    // CREATE STUDENT
    // =========================

    const studentResponse = http.post(
        `${BASE_URL}/students/`,
        JSON.stringify({
            student_name: 'John Doe',
            email: randomEmail('student'),
            phone_number: randomPhone(),
            gender: 'male'
        }),
        authHeaders
    );


    check(studentResponse, {
        'create student': (r) =>
            r.status === 200 || r.status === 429
    });


    let studentId = null;

    try {
        studentId = studentResponse.json('id');
    }
    catch (e) {}


    // =========================
    // GET STUDENTS
    // =========================

    const studentsGet = http.get(
        `${BASE_URL}/students/`,
        authHeaders
    );

    check(studentsGet, {
        'get students': (r) =>
            r.status === 200 || r.status === 429
    });


    // =========================
    // GET STUDENT BY ID
    // =========================

    if (studentId) {

        const studentById = http.get(
            `${BASE_URL}/students/${studentId}`,
            authHeaders
        );

        check(studentById, {
            'get student by id': (r) =>
                r.status === 200 || r.status === 429
        });
    }


    // =========================
    // CREATE FACULTY
    // =========================

    const facultyResponse = http.post(
        `${BASE_URL}/faculties/`,
        JSON.stringify({
            faculty_name: 'Dr Smith',
            email: randomEmail('faculty'),
            phone_number: randomPhone(),
            gender: 'male'
        }),
        authHeaders
    );


    check(facultyResponse, {
        'create faculty': (r) =>
            r.status === 200 || r.status === 429
    });


    let facultyId = null;

    try {
        facultyId = facultyResponse.json('id');
    }
    catch (e) {}


    // =========================
    // GET FACULTIES
    // =========================

    const facultiesGet = http.get(
        `${BASE_URL}/faculties/`,
        authHeaders
    );

    check(facultiesGet, {
        'get faculties': (r) =>
            r.status === 200 || r.status === 429
    });


    // =========================
    // GET FACULTY BY ID
    // =========================

    if (facultyId) {

        const facultyById = http.get(
            `${BASE_URL}/faculties/${facultyId}`,
            authHeaders
        );

        check(facultyById, {
            'get faculty by id': (r) =>
                r.status === 200 || r.status === 429
        });
    }


    // =========================
    // CREATE ENROLLMENT
    // =========================

    let enrollmentId = null;

    if (studentId && courseId) {

        const enrollmentResponse = http.post(
            `${BASE_URL}/enrollments/`,
            JSON.stringify({
                student_id: studentId,
                course_id: courseId
            }),
            authHeaders
        );


        check(enrollmentResponse, {
            'create enrollment': (r) =>
                r.status === 200 || r.status === 429
        });


        try {
            enrollmentId = enrollmentResponse.json('id');
        }
        catch (e) {}
    }


    // =========================
    // GET ENROLLMENTS
    // =========================

    const enrollmentsGet = http.get(
        `${BASE_URL}/enrollments/`,
        authHeaders
    );

    check(enrollmentsGet, {
        'get enrollments': (r) =>
            r.status === 200 || r.status === 429
    });


    // =========================
    // GET ENROLLMENT BY ID
    // =========================

    if (enrollmentId) {

        const enrollmentById = http.get(
            `${BASE_URL}/enrollments/${enrollmentId}`,
            authHeaders
        );

        check(enrollmentById, {
            'get enrollment by id': (r) =>
                r.status === 200 || r.status === 429
        });
    }


    sleep(1);
}