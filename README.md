# 🤖 Your Personal AI Virtual Assistant

It is a **Python-based AI virtual assistant** that can perform a wide range of smart tasks — from answering queries, browsing the internet, summarizing or correcting text, translating languages, controlling system apps, and even capturing screenshots — all using **voice commands**.  

It’s like having your own mini **Jarvis**, built entirely in Python 🧠💻

---

## 🌟 Features

### 🗣️ Voice Interaction
- Wake Ema with **“Wake up”** and put her to sleep with **“Go to sleep.”**
- Responds conversationally to greetings and questions.
- Uses **Google Speech Recognition** and **pyttsx3** for text-to-speech & speech-to-text.

---

### 🌐 Smart Search
- **Google Search** – Searches and reads out summaries.
- **YouTube Search & Play** – Opens and plays videos directly.
- **Wikipedia Search** – Fetches short summaries of topics.

---

### 🧠 AI-Powered NLP Tools
- **Text Summarization** using `sumy` (LSA algorithm).
- **Grammar Correction** using `TextBlob`.
- **Text Translation** to any language using `googletrans` + `gTTS`.
- **WolframAlpha Integration** for factual or mathematical queries.

---

### 📰 News & Weather
- Fetches the latest **news headlines** in categories like Business, Health, Sports, and more.
- Retrieves **current temperature and weather** data using web scraping (BeautifulSoup).

---

### 💻 System & App Control
- Open and close popular apps like Chrome, Paint, Word, Excel, VS Code, etc.
- Open or close browser tabs and websites.
- Take screenshots or even **click your photo** using the system camera.
- Adjust **system volume** using keyboard automation.

---

### ⚡ Additional Tools
- **Password Protection** – Secure access with a stored password in `password.txt`.
- **“Remember that” Memory Feature** – Stores custom notes or reminders.
- **Internet Speed Test** – Checks upload and download speed using `speedtest`.
- **Calculator Mode** – Solves arithmetic expressions through voice commands.

---

## 🧩 Technologies Used

| Category | Library / API |
|-----------|----------------|
| **Speech Recognition** | `speech_recognition`, `pyttsx3`, `gtts`, `playsound` |
| **Search & Info Retrieval** | `wikipedia`, `pywhatkit`, `webbrowser`, `requests`, `BeautifulSoup` |
| **AI & NLP** | `sumy`, `TextBlob`, `googletrans` |
| **System Control** | `os`, `pyautogui`, `pynput` |
| **Math & Logic** | `wolframalpha` |
| **Networking** | `speedtest` |
| **Utilities** | `datetime`, `time`, `json` |

---

Voice-Assistant/
│
├── Ai project.py          # Main script
├── password.txt          # Password storage
├── Remember.txt          # Memory file for saved notes
├── requirements.txt      # Dependencies list
└── README.md             # Project documentation

---


## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/AI-Virtual-Assistant.git
cd AI-Virtual-Assistant

👨‍💻 Author

Krushna Mane
🎓 B.E. in Computer Science  and Engineering(AI & ML)
📧 krushnamane2004@gmail.com
