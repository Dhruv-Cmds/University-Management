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
    const role = document.getElementById("role").value.toLowerCase(); // FIX

    const res = await fetch(`${BASE_URL}/admin/signup`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password, role })
    });

    const data = await res.json();
    console.log("SIGNUP RESPONSE:", data);

    if (res.ok) {
        showMessage("Signup success");
    } else {
        showMessage(data.detail || "Signup failed", "error");
    }
}

async function login() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    try {
        const res = await fetch(`${BASE_URL}/admin/login`, {  // ✅ FIXED ENDPOINT
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });

        const data = await res.json(); // ✅ FIXED
        console.log("LOGIN RESPONSE:", data);

        if (res.ok) {
            token = data.access_token;
            showMessage("Logged in successfully");
        } else {
            showMessage(data.detail || "Login failed", "error");
        }

    } catch (err) {
        console.error("LOGIN ERROR:", err);
        showMessage("Something went wrong", "error");
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
        showMessage(data.detail, "error");
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
        showMessage("Student created");
    } else {
        showMessage(data.detail, "error");
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
        showMessage(data.detail, "error");
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
        showMessage(data.detail, "error");
    }
}