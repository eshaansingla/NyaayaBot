# ⚖️ NyaayaBot — The Indian Tenancy Law Assistant

**NyaayaBot** is a smart AI-powered chatbot built to assist users with **tenant–landlord disputes and rental law guidance in India**.  
It uses **Google Gemini API** for reasoning and natural language understanding, and **Gradio** for a simple and elegant chat-based interface.  

This project was developed by **Eshaan Singla**, a 3rd-year CSE student at **Thapar Institute of Engineering and Technology, Patiala**, as a practical and socially impactful application of AI in law and governance.

---

## 🧠 Overview

Tenancy disputes in India often confuse both tenants and landlords due to vague communication and complex legal jargon.  
**NyaayaBot** bridges this gap by acting as a conversational legal guide — offering explanations, summaries, and actionable steps based on Indian tenancy laws.

You can:
- 💬 Ask questions about rent, eviction, lease, deposits, or tenant rights.
- 📄 Upload rent agreements or legal notices in **PDF format** for analysis.
- ⚖️ Receive responses grounded in **Indian tenancy/rental clauses**.
- 🚫 Get polite refusals for non-tenancy topics (bot strictly focuses on this domain).

---

## ✨ Features

✅ **Tenant–Landlord Domain Expertise** — Handles tenancy law topics only.  
✅ **PDF Support** — Extracts and analyzes text from uploaded PDF documents.  
✅ **Conversational Memory** — Maintains up to 10 previous exchanges for context.  
✅ **Gemini API Integration** — Uses Google’s advanced LLM for reasoning.  
✅ **Dataset-Driven** — Built upon a filtered subset of the Indian Law dataset (`viber1/indian-law-dataset`).  
✅ **Modern UI** — Implemented using Gradio Blocks for a clean and responsive layout.  

---

## 🗂️ Project Structure
``` bash
NyaayaBot/
│
├── app.py # Main backend and Gradio interface
├── tenancy_dataset.json # Filtered tenancy law clauses from dataset
├── requirements.txt # Python dependencies
├── .env # API key file (not pushed to GitHub)
├── README.md # Project documentation
└── assets/
└── nyaaya.ico # App favicon
```

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/eshaansingla/NyaayaBot.git
cd NyaayaBot
source venv/bin/activate
```

### 2️⃣ Clone the repository
``` bash
python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate   # On macOS/Linux
```
### 3️⃣ Install dependencies
``` bash
pip install -r requirements.txt
```
### 4️⃣ Add your Gemini API key
``` bash
Create a .env file in the project root:
GEMINI_API_KEY=your_api_key_here
```
### 5️⃣ Run the application
``` bash
python app.py
```
### Demo Images

<p align="center"> <img src="media/demo1.png" width="350"> <img src="media/demo2.png" width="350"> <img src="media/demo3.png" width="350"> </p>
### 👤 Author

Eshaan Singla
🎓 B.E. Computer Science and Engineering
🏫 Thapar Institute of Engineering and Technology, Patiala
💡 Interests: DSA, Machine Learning, AI, and Web Systems
📬 eshaansingla2807@gmail.com

### 🚀 Future Enhancements

🔊 Add voice query support using Speech Recognition

🌐 Add Hindi and Punjabi language support

📘 Expand scope to cover consumer protection and civil disputes

🧾 Include legal document summarization and case law retrieval

### ⚖️ Legal Disclaimer

NyaayaBot provides general informational guidance and not professional legal advice.
Users are encouraged to consult a certified lawyer for specific cases.
