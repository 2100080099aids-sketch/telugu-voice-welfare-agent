# Telugu Voice-Based Welfare Agent 🇮🇳🎙️

A **voice-first, agentic AI system** that helps users identify and apply for **government welfare schemes** using **Telugu** voice input and output.

This project is built as part of an AI/ML design assignment and demonstrates **end-to-end voice interaction**, **agentic reasoning**, **tool usage**, **memory**, and **failure handling** in a native Indian language.

---

## 🎯 Objective

Build a **voice-first AI agent** that:
- Understands Telugu voice input
- Identifies eligible government welfare schemes
- Uses tools to reason and decide
- Responds back in **Telugu voice**
- Handles incomplete or missing user information

---

## ✅ Key Features

- 🎙️ **Voice Input (Telugu)** using Whisper (Speech-to-Text)
- 🧠 **Agentic Workflow** (Planner → Executor → Evaluator)
- 🛠️ **Multiple Tools**
  - Eligibility checking tool
  - Scheme recommendation tool
- 🧾 **Conversation Memory**
- ⚠️ **Failure Handling** (missing age, incomplete info)
- 🔊 **Voice Output (Telugu)** using Text-to-Speech
- 💻 Runs fully on **CPU** (no GPU required)

---

## 🏗️ System Architecture

Telugu Voice Input (.wav)
↓
Speech-to-Text (Whisper)
↓
Agent (Plan → Execute → Evaluate)
↓
Tools (Eligibility + Scheme Logic)
↓
Text-to-Speech (Telugu)
↓
Spoken Output (.mp3)

yaml
Copy code

---

## 📁 Project Structure

telugu_welfare_agent/
│
├── app.py # Main execution pipeline
├── agent.py # Agent logic (planning & decision making)
├── tools.py # Eligibility & scheme tools
├── memory.py # Conversation memory
├── voice.py # STT (Whisper) & TTS
├── input.wav # Telugu voice input (example)
├── README.md
└── venv/ # Virtual environment (ignored in GitHub)

yaml
Copy code

---

## ⚙️ Setup Instructions (Windows)

### 1️⃣ Install Python
- Install **Python 3.10 (64-bit)**
- Download: https://www.python.org/downloads/release/python-31013/
- ✅ Check **Add Python to PATH**

---

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
bash
Copy code
pip install numpy==1.26.4
pip install torch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 --index-url https://download.pytorch.org/whl/cpu
pip install faster-whisper transformers gtts sounddevice
▶️ How to Run the Project
1️⃣ Record Telugu Voice Input
Use Windows Voice Recorder and say:

Copy code
నాకు ప్రభుత్వ పథకం కావాలి
Save the file as:

css
Copy code
input.wav
Place it inside the project folder.

2️⃣ Run the Application
bash
Copy code
python app.py
3️⃣ Output
Telugu text is printed in the terminal

Telugu voice response is generated as:

php-template
Copy code
output_<random_id>.mp3
Double-click the MP3 file to hear the response.

⚠️ Failure Handling Examples
Scenario	Agent Behavior
Age not provided	Asks user for age
Incomplete details	Requests missing information
Invalid input	Gracefully recovers

🎥 Demo Video
The demo video (5–7 minutes) demonstrates:

Voice-based Telugu interaction

Agent reasoning and tool calls

Conversation memory

Failure handling and recovery

(Demo video link provided in submission form)

✅ Assignment Requirements Checklist
 Voice-first interaction

 Native Indian language (Telugu)

 Agentic workflow

 Multiple tools

 Conversation memory

 Failure handling

 End-to-end runnable code

📌 Notes
Whisper model downloads automatically on first run

float16 → float32 warnings are expected on CPU

Audio files and virtual environment are excluded from GitHub

👤 Author
Karthik
