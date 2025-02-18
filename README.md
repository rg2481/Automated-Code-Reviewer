# Automated-Code-Reviewer

## Project Overview
This project aims to build an **AI-powered code reviewer** tool using **OpenAI Codex** (or Hugging Face's **CodeGen**) to automatically review Python code for syntax errors, logic issues, and code quality improvements. The tool helps developers improve their code by providing **instant feedback** and suggestions based on industry best practices.

---

## Key Features
- **Syntax Error Detection:** Identifies common syntax errors in Python code.
- **Logic Error Review:** Detects potential issues in the logic and flow of code.
- **Code Quality Suggestions:** Provides recommendations to improve readability, structure, and performance.
- **Real-time Feedback:** Provides feedback instantly after code submission.
- **Interactive UI:** User-friendly interface using **Streamlit/Gradio** for seamless interaction.
- **Deployment:** API deployed using **FastAPI** for backend handling.

---

## Tech Stack
- **Backend:**  
  - **FastAPI**: For serving API requests.
  - **Uvicorn**: ASGI server for handling real-time interactions.
  
- **Frontend:**  
  - **Streamlit** or **Gradio**: For building the web-based user interface.

- **AI Libraries:**  
  - **OpenAI API**: To interact with GPT models like **GPT-4o**.
  - **Hugging Face Transformers**: For model integration and code review.
  - **LangChain**: For creating structured pipelines in code review.
  - **spaCy**: For text processing and analysis.

- **Deployment:**  
  - **Docker**: For containerization and easy deployment.

- **Dataset Sources:**  
  - **Kaggle**  
  - **Hugging Face Hub**  
  - **UCI ML Repository**

---

## How It Works
1. **User Submits Code:** The user inputs Python code (via file upload or typing in the UI).
2. **Code Review Process:**  
   - The backend (FastAPI) sends the code to the AI model (OpenAI Codex or CodeGen).
   - The AI analyzes the code for **syntax errors**, **logical flaws**, and **code quality**.
3. **AI Suggestions:**  
   - The model generates feedback, suggesting **code fixes**, **optimization ideas**, and **improvements**.
4. **Interactive Output:** The results are displayed back to the user in an easy-to-understand format with code corrections and explanations.

---
