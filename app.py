import os
from datasets import load_dataset
from dotenv import load_dotenv
import google.generativeai as genai
from PyPDF2 import PdfReader
import gradio as gr

# =======================
# Load environment variables
# =======================
load_dotenv()

# =======================
# Load tenancy dataset
# =======================
print("Loading dataset...")
dataset = load_dataset("viber1/indian-law-dataset")
keywords = ['tenant', 'rent', 'landlord', 'lease', 'eviction', 'rental', 'agreement', 'deposit', 'notice']

tenancy_clauses = []
for item in dataset['train']:
    text = item['Instruction'].lower()
    if any(keyword in text for keyword in keywords):
        tenancy_clauses.append({
            'clause': item['Instruction'],
            'guidance': "PLACEHOLDER: Write plain-language guidance here",
            'source': item.get('Response', '')
        })
print(f"Filtered {len(tenancy_clauses)} tenancy/rental clauses.")

# =======================
# Configure Gemini API
# =======================
gemini_key = os.getenv("GEMINI_API_KEY")
if not gemini_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")
genai.configure(api_key=gemini_key)
model = genai.GenerativeModel('gemini-2.0-flash-lite')

# =======================
# Conversation state
# =======================
chat_history = []

# =======================
# Helper functions
# =======================
def get_gemini_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            full_text += page_text + "\n"
    return full_text.strip()

def find_relevant_clause(user_question):
    question = user_question.lower()
    for item in tenancy_clauses:
        if any(keyword in question for keyword in keywords):
            return item['clause']
    return None

# =======================
# Main processing function
# =======================
def process_input(user_input=None, pdf_file=None):
    global chat_history
    content = ""

    # Extract content from input
    if user_input:
        content = user_input.strip()
    elif pdf_file:
        content = extract_text_from_pdf(pdf_file.name)

    if not content:
        return "Please provide some input."

    # Build conversation history for context
    history_text = ""
    for chat in chat_history[-10:]:
        history_text += f"User: {chat['user']}\nNyaayaBot: {chat['bot']}\n"

    # Construct prompt
    prompt = f"""
You are NyaayaBot, a highly experienced, witty, and authoritative Indian tenancy law assistant. You are assisting clients (landlords, tenants, students, or lawyers) regarding tenancy/rental disputes in India.

Tone & Style:

Speak in simple, clear, and conversational language, as if explaining to someone without legal training.

Be friendly, approachable, and witty, e.g., "Hello! Did you know you have rights as a tenant?" or "Hey there! Ready to learn about your tenancy rights?"

Do not wait for abusive language to respond; if any disrespectful or abusive words are used, respond politely but firmly and redirect the conversation to legal advice.

Behavior & Approach:

Only handle tenancy/rental law-related queries. Politely refuse unrelated topics.

Be thorough and precise: summarize relevant clauses, explain why they matter, and give step-by-step actions. Include any deadlines, timelines, or statutory provisions that may apply.

Maximize the client’s advantage: Provide relevant past legal cases, precedents, or rulings to strengthen the client’s position and show applicability to their situation.

Always give practical, actionable guidance that clients can follow to assert their rights or protect themselves legally.

End every response with a polite caution or note, reminding the user to act within legal limits, without overemphasizing politeness unnecessarily.

Example Response Structure:

Greeting: witty and relevant.

Clause explanation: summarize, why it matters, step-by-step actions.

Deadlines/Timelines: if applicable.

Past cases / legal precedents: cite relevant cases and explain their relevance.

Polite caution: reminder to act legally, protect rights, or consult a lawyer if needed.

Additional Instructions:

Be confident.

Avoid filler; every sentence should add value.

If a user’s query lacks clarity, ask concise clarifying questions without deviating from tenancy law.

Provide responses that are concise yet thorough enough to maximize legal leverage in the context of the question.
Conversation history:
{history_text}

Current user input:
{content}
"""

    bot_response = get_gemini_response(prompt)
    chat_history.append({"user": content, "bot": bot_response})
    return bot_response

# =======================
# Gradio Chat Interface
# =======================
with gr.Blocks(title="NyaayaBot - Tenancy Assistant", css="footer {display: none !important;}") as demo:
    gr.Markdown("<h2 style='text-align:center'>NyaayaBot - Your Indian Tenancy Law Assistant</h2>")

    with gr.Row():
        with gr.Column(scale=1):
            user_input = gr.Textbox(
                label="Type your question here...",
                placeholder="Ask about rent, eviction, notice, etc.",
                lines=2,
            )
            pdf_file = gr.File(label="Upload PDF", file_types=['.pdf'])
            send_button = gr.Button("Send", variant="primary")
        chatbot = gr.Chatbot(label="NyaayaBot Chat", height=700)
    def submit_message(user_message, pdf, chat_history_ui):
        response = process_input(user_message, pdf)
        chat_history_ui.append((user_message if user_message else "[PDF Uploaded]", response))
        return "", None, chat_history_ui

    send_button.click(
        submit_message,
        [user_input, pdf_file, chatbot],
        [user_input, pdf_file, chatbot]
    )

    user_input.submit(
        submit_message,
        [user_input, pdf_file, chatbot],
        [user_input, pdf_file, chatbot]
    )

demo.launch(show_api=False)
