// `window.UMS_API_URL` can be set before this file to override the API location.
// uses port 8000, so requests fall back to that port if Docker is not running.
const isLocalHost = ["localhost", "127.0.0.1"].includes(window.location.hostname);
const configuredApiUrl = window.UMS_API_URL?.replace(/\/$/, "");
const apiUrls = configuredApiUrl
    ? [configuredApiUrl]
    : isLocalHost || window.location.protocol === "file:"
        ? ["http://127.0.0.1:8002"]
        : [`${window.location.origin}/api`];

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

function getErrorMessage(detail) {
    if (typeof detail === "string") return detail;
    if (Array.isArray(detail)) {
        return detail.map((item) => item.msg || "Invalid input.").join(" ");
    }
    return "The request could not be completed.";
}

async function request(path, options = {}) {
    let networkError;

    for (const apiUrl of apiUrls) {
        try {
            const response = await fetch(`${apiUrl}${path}`, options);
            const data = await response.json().catch(() => ({}));

            if (!response.ok) {
                throw new Error(getErrorMessage(data.detail));
            }
            return data;
        } catch (error) {
            // Only try the next URL when the server could not be reached. Backend
            // errors (such as invalid credentials) should be shown immediately.
            if (!(error instanceof TypeError)) throw error;
            networkError = error;
        }
    }

    throw new Error(
        networkError
            ? "Cannot reach the backend. Start FastAPI and try again."
            : "The request could not be completed."
    );
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

    if (!email || !password) {
        showMessage("Enter an email address and password to sign up.", "error");
        return;
    }

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

    if (!email || !password) {
        showMessage("Enter your email address and password to log in.", "error");
        return;
    }

    try {
        const data = await request("/admin/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });

        token = data.access_token;
        localStorage.setItem("ums_access_token", token);
        window.location.assign("dashboard.html");
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
    const isDashboard = window.location.pathname.endsWith("/dashboard.html");
    if (isDashboard && !token) {
        window.location.replace("login.html");
        return;
    }

    document.getElementById("signupBtn")?.addEventListener("click", signup);
    document.getElementById("loginBtn")?.addEventListener("click", login);
    document.getElementById("createStudentBtn")?.addEventListener("click", createStudent);
    document.getElementById("createFacultyBtn")?.addEventListener("click", createFaculty);
    document.getElementById("createCourseBtn")?.addEventListener("click", createCourse);
    document.getElementById("enrollBtn")?.addEventListener("click", enroll);
});
