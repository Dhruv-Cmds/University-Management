const BASE_URL = "http://127.0.0.1:8002";

console.log("APP JS LOADED 🚀");

let token = "";
let lastStudentId = null;
let lastCourseId = null;

function showMessage(text, type = "success") {
    const box = document.getElementById("message");
    box.textContent = text;
    box.className = `message ${type}`;
}

// ================= AUTH =================
async function signup() {
    console.log("SIGNUP FUNCTION RUNNING 🚀");

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const role = document.getElementById("role").value.toLowerCase();

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
    console.log("LOGIN FUNCTION RUNNING 🚀");

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const res = await fetch(`${BASE_URL}/admin/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password })
    });

    const data = await res.json();

    console.log("LOGIN RESPONSE:", data);
    console.log("STATUS:", res.status);

    if (res.ok) {
        token = data.access_token;
        console.log("TOKEN:", token);
        showMessage("Logged in successfully");
    } else {
        showMessage(data.detail || "Login failed", "error");
    }
}

// ================= COURSE =================
async function createCourse() {
    console.log("CREATE COURSE 🚀");

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

// ================= STUDENT =================
async function createStudent() {
    console.log("CREATE STUDENT 🚀");

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

// ================= FACULTY =================
async function createFaculty() {
    console.log("CREATE FACULTY 🚀");

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

// ================= ENROLL =================
async function enroll() {
    console.log("ENROLL 🚀");

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

// ================= EVENT BINDING (IMPORTANT) =================
document.getElementById("signupBtn").addEventListener("click", signup);
document.getElementById("loginBtn").addEventListener("click", login);
document.getElementById("courseBtn").addEventListener("click", createCourse);
document.getElementById("studentBtn").addEventListener("click", createStudent);
document.getElementById("facultyBtn").addEventListener("click", createFaculty);
document.getElementById("enrollBtn").addEventListener("click", enroll);

console.log("EVENTS BOUND ✅");