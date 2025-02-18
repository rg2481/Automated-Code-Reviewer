#pip install fastapi uvicorn openai torch transformers spacy nltk streamlit
 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables
openai.api_key = os.getenv("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")

# Initialize FastAPI
app = FastAPI()

# Allow frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeInput(BaseModel):
    code: str

@app.post("/review")
def review_code(input_data: CodeInput):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert Python code reviewer. Analyze the given code for syntax, logic errors, and best practices."},
                {"role": "user", "content": input_data.code},
            ],
        )
        return {"review": response["choices"][0]["message"]["content"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

import uvicorn
import asyncio

if __name__ == "__main__":
    config = uvicorn.Config(app, host="0.0.0.0", port=8000)
    server = uvicorn.Server(config)

    if asyncio.get_event_loop().is_running():
        asyncio.ensure_future(server.serve())
    else:
        asyncio.run(server.serve())




import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/review"

def main():
    st.title("Automated Code Reviewer")
    st.write("Enter Python code to review for errors and best practices.")
    
    code = st.text_area("Paste your Python code here:")
    if st.button("Review Code"):
        if code.strip():
            response = requests.post(API_URL, json={"code": code})
            if response.status_code == 200:
                st.subheader("Review Output:")
                st.write(response.json()["review"])
            else:
                st.error("Error: " + response.json()["detail"])
        else:
            st.warning("Please enter some code to review.")

if __name__ == "__main__":
    main()
