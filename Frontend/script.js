// Theme Toggle Logic
const themeToggleBtn = document.getElementById('theme-toggle');
// Brauzer yaddaşından rejimi yoxlayırıq
const currentTheme = localStorage.getItem('theme') || 'light';

if (currentTheme === 'dark') {
    document.documentElement.setAttribute('data-theme', 'dark');
    themeToggleBtn.textContent = '☀️';
}

themeToggleBtn.addEventListener('click', () => {
    const theme = document.documentElement.getAttribute('data-theme');
    if (theme === 'dark') {
        document.documentElement.removeAttribute('data-theme');
        localStorage.setItem('theme', 'light');
        themeToggleBtn.textContent = '🌙';
    } else {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
        themeToggleBtn.textContent = '☀️';
    }
});

// Chat Logic
async function sendMessage() {
    const inputField = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");
    const message = inputField.value.trim();

    if (message === "") return;

    // Add user message to UI
    chatBox.innerHTML += `<div class="message user-message">${message}</div>`;
    inputField.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        // Send POST request to backend
        const response = await fetch("http://127.0.0.1:5000/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        });

        const data = await response.json();
        
        // Add bot response to UI
        chatBox.innerHTML += `<div class="message bot-message">${data.answer}</div>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    } catch (error) {
        // Error message in English
        chatBox.innerHTML += `<div class="message bot-message" style="color: #ff4d4d; font-weight: bold;">Error. Could not connect to the server.</div>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}

// Send message on Enter key press
document.getElementById("user-input").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});