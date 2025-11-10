# ai-chatbox-hf
# Django + DRF Chatbot Setup Guide

This project demonstrates a Django + DRF chatbot with Hugging Face local model integration (unlimited practice) and optional OpenAI provider.

---

## 1. Environment Setup
- Create a virtual environment:
  python -m venv .venv
  .venv\Scripts\activate   (Windows)
  source .venv/bin/activate   (macOS/Linux)

- Install dependencies:
  pip install django djangorestframework transformers torch
  pip install openai   (optional, for cloud provider)

---

## 2. Project Scaffold
- Start Django project:
  django-admin startproject chatbox .
- Create app:
  python manage.py startapp conversations

---

## 3. Settings
- Add to INSTALLED_APPS in chatbox/settings.py:
  rest_framework
  conversations

---

## 4. URLs
- chatbox/urls.py:
  path("api/", include("conversations.urls"))

- conversations/urls.py:
  path("chat/", chat, name="chat")

---

## 5. Local Hugging Face Service
- conversations/services/local_hf.py:
  from transformers import pipeline
  generator = pipeline("text-generation", model="distilgpt2")
  def generate_reply(prompt): return generator(prompt)[0]["generated_text"]

---

## 6. Optional OpenAI Service
- conversations/services/openai_provider.py:
  import openai
  def generate_reply_cloud(prompt): return openai.ChatCompletion.create(...)

---

## 7. View
- conversations/views.py:
  USE_LOCAL = True
  if USE_LOCAL: from .services.local_hf import generate_reply
  else: from .services.openai_provider import generate_reply_cloud as generate_reply

  @api_view(["POST"])
  def chat(request):
      message = request.data.get("message")
      reply = generate_reply(message)
      return Response({"reply": reply})

---

## 8. Run Server
- Apply migrations:
  python manage.py migrate
- Start server:
  python manage.py runserver

---

## 9. Test with Postman
- POST http://127.0.0.1:8000/api/chat/
- Headers: Content-Type: application/json
- Body: { "message": "Explain what a cat is in simple words." }

---

## 10. GitHub Workflow
- Initialize repo:
  git init
  git add .
  git commit -m "Initial commit: Django chatbot project"
  git branch -M main
  git remote add origin https://github.com/<username>/<repo>.git
  git push -u origin main

---

## Notes
- Local Hugging Face pipeline runs offline, unlimited practice.
- OpenAI provider requires API key and billing after free credits.
- Use .gitignore to exclude .venv, __pycache__, *.pyc, db.sqlite3.
