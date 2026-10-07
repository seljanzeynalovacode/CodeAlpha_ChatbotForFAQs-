# 🤖 IoT Assistant Chatbot (FAQ Retrieval System)

A modern, intelligent, and responsive Retrieval-Based Chatbot built to answer Frequently Asked Questions (FAQs) about the Internet of Things (IoT). This project was developed as part of the **CodeAlpha** internship tasks. It uses Natural Language Processing (NLP) techniques to match user queries with the most relevant answers from a predefined knowledge base.

## ✨ Features

* **🧠 Smart Query Matching:** Uses **TF-IDF Vectorization** and **Cosine Similarity** to accurately understand and match user questions with the closest FAQ.
* **🌓 Dark/Light Mode:** A modern, sleek UI featuring gradient themes and a fully functional dark/light mode toggle that saves user preferences in local storage.
* **⚡ Lightweight API:** Powered by a fast and simple Python Flask backend.
* **🎨 Modern UI/UX:** Built with pure HTML/CSS/JS, featuring smooth animations, custom scrollbars, and FontAwesome icons.
* **📡 No Database Required:** Uses a simple, easily updatable `faqs.json` file as its knowledge base.

## 🛠️ Tech Stack

* **Backend:** Python, Flask, Flask-CORS
* **Machine Learning / NLP:** `scikit-learn` (TfidfVectorizer, cosine_similarity), `nltk`
* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Icons:** FontAwesome

## 📁 Project Structure

```text
CodeAlpha_ChatbotForFAQs/
│
├── Backend/
│   ├── app.py                 # Main Flask server and API endpoints
│   ├── chatbot_logic.py       # NLP logic, TF-IDF, and Cosine Similarity functions
│   ├── faqs.json              # Knowledge base containing IoT questions and answers
│
│
└── Frontend/
    ├── index.html             # Chatbot UI structure
    ├── style.css              # Styling, animations, and Dark/Light mode gradients
    └── script.js              # API communication and UI interactions
```
# 🚀 How to Run the Project Locally

Follow these step-by-step instructions to get the chatbot running on your local machine.

## 1. Clone the Repository

```bash
git clone https://github.com/seljanzeynalovacode/CodeAlpha_ChatbotForFAQs-.git
cd CodeAlpha_ChatbotForFAQs
```

## 2. Set Up the Backend

Navigate to the `Backend` directory and set up a virtual environment:

```bash
cd Backend
python -m venv venv
```

Activate the virtual environment:

- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

Install the required Python packages:
>
> ```bash
> pip install flask flask-cors scikit-learn
> ```

## 3. Start the Server

Run the Flask API server:

```bash
python app.py
```

The backend server should now be running at `http://127.0.0.1:5000`. **Keep this terminal open!**

## 4. Launch the Frontend

1. Open the `Frontend` folder.
2. Simply double-click the `index.html` file to open it in your default web browser (or use VS Code's "Live Server" extension).
3. Type a question like *"What is IoT?"* or *"What is edge computing?"* and enjoy chatting with your assistant!

## 💡 Usage Notes

- **Customizing FAQs:** To change the chatbot's topic, simply edit the `Backend/faqs.json` file with your own questions and answers. **Important:** Restart the Flask server after modifying the JSON file so the NLP model can re-train on the new data.
- **Theme Toggle:** Click the Moon/Sun icon in the top right corner of the chat window to switch between Light and Dark mode.
