// Use the local FastAPI server during development and the reverse-proxied API in production.
const BASE_URL = window.location.hostname === "ums.dhruvcore.com"
    ? `${window.location.origin}/api`
    : "http://127.0.0.1:8000";

let token = localStorage.getItem("ums_access_token") || "";
let lastStudentId = null;
let lastCourseId = null;

function showMessage(text, type = "success") {
    const box = document.getElementById("message");
    if (!box) return;

    box.textContent = text;
    box.className = `message ${type}`;
    box.hidden = false;
}

async function request(path, options = {}) {
    try {
        const response = await fetch(`${BASE_URL}${path}`, options);
        const data = await response.json().catch(() => ({}));

        if (!response.ok) {
            throw new Error(data.detail || "The request could not be completed.");
        }
        return data;
    } catch (error) {
        if (error instanceof TypeError) {
            throw new Error("Cannot reach the backend. Start FastAPI and try again.");
        }
        throw error;
    }
}

function authHeaders() {
    if (!token) throw new Error("Please log in before using the dashboard.");
    return {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`
    };
}

async function signup() {
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;
    const role = document.getElementById("role").value;

    try {
        await request("/admin/signup", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password, role })
        });
        showMessage("Account created. You can now log in.");
    } catch (error) {
        showMessage(error.message, "error");
    }
}

async function login() {
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;

    try {
        const data = await request("/admin/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });

        token = data.access_token;
        localStorage.setItem("ums_access_token", token);
        window.location.href = "dashboard.html";
    } catch (error) {
        showMessage(error.message, "error");
    }
}

async function createStudent() {
    try {
        const data = await request("/students/", {
            method: "POST",
            headers: authHeaders(),
            body: JSON.stringify({
                student_name: document.getElementById("student-name").value.trim(),
                email: document.getElementById("student-email").value.trim(),
                phone_number: document.getElementById("student-phone-number").value.trim(),
                gender: document.getElementById("student-gender").value
            })
        });
        lastStudentId = data.id;
        showMessage(`Student created (ID: ${data.id}).`);
    } catch (error) {
        showMessage(error.message, "error");
    }
}

async function createFaculty() {
    try {
        const data = await request("/faculties/", {
            method: "POST",
            headers: authHeaders(),
            body: JSON.stringify({
                faculty_name: document.getElementById("faculty-name").value.trim(),
                email: document.getElementById("faculty-email").value.trim(),
                phone_number: document.getElementById("faculty-phone-number").value.trim(),
                gender: document.getElementById("faculty-gender").value
            })
        });
        showMessage(`Faculty member created (ID: ${data.id}).`);
    } catch (error) {
        showMessage(error.message, "error");
    }
}

async function createCourse() {
    try {
        const data = await request("/courses/", {
            method: "POST",
            headers: authHeaders(),
            body: JSON.stringify({
                course_name: document.getElementById("course-name").value.trim()
            })
        });
        lastCourseId = data.id;
        showMessage(`Course created (ID: ${data.id}).`);
    } catch (error) {
        showMessage(error.message, "error");
    }
}

async function enroll() {
    const studentInput = document.getElementById("enrollment-student-id");
    const courseInput = document.getElementById("enrollment-course-id");
    const student_id = Number(studentInput?.value || lastStudentId);
    const course_id = Number(courseInput?.value || lastCourseId);

    if (!student_id || !course_id) {
        showMessage("Enter a student ID and course ID, or create both first.", "error");
        return;
    }

    try {
        const data = await request("/enrollments/", {
            method: "POST",
            headers: authHeaders(),
            body: JSON.stringify({ student_id, course_id })
        });
        showMessage(`Enrollment created (ID: ${data.id}).`);
    } catch (error) {
        showMessage(error.message, "error");
    }
}

document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("signupBtn")?.addEventListener("click", signup);
    document.getElementById("loginBtn")?.addEventListener("click", login);
    document.getElementById("createStudentBtn")?.addEventListener("click", createStudent);
    document.getElementById("createFacultyBtn")?.addEventListener("click", createFaculty);
    document.getElementById("createCourseBtn")?.addEventListener("click", createCourse);
    document.getElementById("enrollBtn")?.addEventListener("click", enroll);
});
