# Automated-Code-Reviewer

## Project Overview
An AI-powered code reviewer built using **FastAPI** and **Streamlit**, leveraging **OpenAI GPT-4** for analyzing Python code and providing feedback on syntax, logic errors, and best practices. This tool is designed to assist developers by automating the review process, enhancing code quality, and saving time.

## Features
- FastAPI backend to handle code review requests
- Streamlit frontend for easy user interaction
- OpenAI GPT-4 for intelligent code analysis and suggestions
- Supports real-time feedback on syntax, structure, and logic errors
- Easy to deploy and integrate into existing workflows
- Provides best practices and optimizations for better code quality

## Technologies Used
- **FastAPI** - Backend API framework for high-performance processing
- **Streamlit** - Interactive frontend framework for seamless user experience
- **OpenAI GPT-4** - AI-powered code analysis for generating meaningful insights
- **Transformers (Hugging Face)** - NLP support for enhancing language understanding
- **Spacy & NLTK** - Additional NLP tools for processing textual content
- **Uvicorn** - ASGI server for running FastAPI applications efficiently


## How It Works
1. **User Submits Code:** The user inputs Python code (via file upload or typing in the UI).
2. **Code Review Process:**  
   - The backend (FastAPI) sends the code to the AI model (OpenAI Codex or CodeGen).
   - The AI analyzes the code for **syntax errors**, **logical flaws**, and **code quality**.
3. **AI Suggestions:**  
   - The model generates feedback, suggesting **code fixes**, **optimization ideas**, and **improvements**.
4. **Interactive Output:** The results are displayed back to the user in an easy-to-understand format with code corrections and explanations.

---
