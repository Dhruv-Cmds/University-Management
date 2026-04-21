const BASE_URL = "http://127.0.0.1:8000";

let token = "";
let lastStudentId = null;
let lastCourseId = null;

function showMessage(text, type = "success") {
    const box = document.getElementById("message");
    box.textContent = text;
    box.className = `message ${type}`;
}

// AUTH
async function signup() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const role = document.getElementById("role").value;

    console.log({ email, password, role });

    const res = await fetch("http://127.0.0.1:8000/auth/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            email: email,
            password: password,
            role: role
        })
    });

    const data = await res.json();
    console.log("Response:", data);

    if (res.ok) {
        showMessage("Signup success");
    } else {
        showMessage(`${JSON.stringify(data)}`, "error");
    }
}

async function login() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const res = await fetch(`${BASE_URL}/auth/login`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ email, password })
    });

    const data = await res.json();

    if (res.ok) {
        token = data.access_token;
        showMessage("Logged in successfully");
    } else {
        showMessage(`${data.detail}`, "error");
    }
}

// COURSE
async function createCourse() {
    const course_name = document.getElementById("course_name").value;

    const res = await fetch(`${BASE_URL}/courses/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({ course_name })
    });

    const data = await res.json();

    if (res.ok) {
        lastCourseId = data.id;
        showMessage("Course created");
    } else {
        showMessage(`${data.detail}`, "error");
    }
}

// STUDENT
async function createStudent() {
    const student_name = document.getElementById("student_name").value;
    const email = document.getElementById("student_email").value;
    const phone_number = document.getElementById("phone").value;
    const gender = document.getElementById("gender").value;

    const res = await fetch(`${BASE_URL}/students/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({
            student_name,
            email,
            phone_number,
            gender
        })
    });

    const data = await res.json();

    if (res.ok) {
        lastStudentId = data.id;
        showMessage(" Student created");
    } else {
        showMessage(`${data.detail}`, "error");
    }
}

// FACULTY
async function createFaculty() {
    const faculty_name = document.getElementById("faculty_name").value;
    const email = document.getElementById("faculty_email").value;
    const phone_number = document.getElementById("faculty_phone").value;
    const gender = document.getElementById("faculty_gender").value;

    const res = await fetch(`${BASE_URL}/faculties/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({
            faculty_name,
            email,
            phone_number,
            gender
        })
    });

    const data = await res.json();

    if (res.ok) {
        showMessage("Faculty created");
    } else {
        showMessage(`${data.detail}`, "error");
    }
}

// ENROLL
async function enroll() {
    if (!lastStudentId || !lastCourseId) {
        showMessage("Create student and course first", "error");
        return;
    }

    const res = await fetch(`${BASE_URL}/enrollment/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({
            student_id: lastStudentId,
            course_id: lastCourseId
        })
    });

    const data = await res.json();

    if (res.ok) {
        showMessage("Enrollment successful");
    } else {
        showMessage(`${data.detail}`, "error");
    }
}