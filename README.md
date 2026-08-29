# 🎙️ Theory - Voice Controlled AI Assistant
Theory is a Python-based voice-controlled desktop assistant that can perform tasks using voice commands, inspired by JARVIS.
 
## 🚀 Features
- 🎤 Voice command recognition
- 👋 Wake word activation ("Hey Theory") — stays idle until called
- 🗣️ Text-to-speech response
- 🌐 Open websites (YouTube, Google, etc.)
- 🕒 Tell time and date
- 📸 Take screenshots
- 📰 Fetch latest news headlines
- 💾 Memory system (store & recall info)
- ⚙️ System controls (shutdown, restart, volume)
- 🤖 Local AI chatbot fallback (Ollama + Llama 3.2) — answers general questions that aren't a recognized command
## 🛠️ Tech Stack
- Python
- SpeechRecognition
- pyttsx3
- PyAutoGUI
- RapidFuzz
- Feedparser
- Requests
- PIL
- Ollama (local LLM — Llama 3.2)
## 🎥 Demo
[Watch Demo on LinkedIn](https://www.linkedin.com/posts/ayushverma-web_python-ai-machinelearning-activity-7446785696331292672-TeZh?utm_source=share&utm_medium=member_desktop&rcm=ACoAAF7JApoBqLjhWD7JIHQMcc-bPsxk9C9PeTo)
 
## About Project
This project was built to explore voice automation and create a simple personal assistant using Python.
 
## Future Improvements
- Add GUI interface
- Improve command understanding
## Author 
Ayush Verma
 
## ▶️ How to Run
Make sure [Ollama](https://ollama.com) is installed and running with Llama 3.2 pulled:
```bash
ollama run llama3.2
```
 
Then install dependencies and run:
```bash
pip install -r requirements.txt
python theory.py
```
 
Say **"Hey Theory"** to wake it up, then give your command.
 
