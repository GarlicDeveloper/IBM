
```markdown
# 🏋️‍♂️ AI Fitness & Diet Planner for Students (Local LLM + Streamlit)

This app generates personalized workout and diet plans for students using a locally hosted LLM via [Ollama](https://ollama.com/) and a Streamlit interface. It considers individual goals, cultural food habits, available equipment, and budget constraints.

---

## 🚀 Features

- Personalized fitness and meal plans
- Supports cultural and dietary preferences
- Works offline using local LLMs (e.g., LLaMA 3, Mistral, Gemma)
- Fast response, no API limits
- Simple Streamlit UI

---

## 🧠 Requirements

- Python 3.8+
- [Ollama](https://ollama.com/) installed and running
- A pulled model (e.g., `llama3`, `mistral`, `gemma`)
- Streamlit installed

---

## 🔧 Installation

```bash
# Install dependencies
pip install streamlit requests

# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull a model
ollama pull llama3
```

---

## ▶️ Run the App

```bash
# Start Ollama in background
ollama run llama3

# Launch Streamlit app
streamlit run app.py
```

---

## 📝 Customization

You can switch models by changing this line in `app.py`:

```python
OLLAMA_MODEL = "llama3"  # Options: mistral, gemma, phi3, etc.
```

To increase output length or tweak creativity:

```python
payload = {
    "model": OLLAMA_MODEL,
    "prompt": prompt,
    "stream": False,
    "options": {
        "temperature": 0.7,
        "top_p": 0.9,
        "max_tokens": 2048
    }
}
```

---

## 📦 File Structure

```
├── app.py          # Main Streamlit app
├── README.md       # Project documentation
```

---

## 📌 Notes

- This app runs entirely locally—no external API calls.
- Ideal for students, educators, or developers exploring LLMs for wellness use cases.
- You can extend it with PDF export, login system, or calorie tracking.

---

## 🧑‍💻 Author

Built by Vikrant using Streamlit + Ollama + LLaMA 3  
Optimized for clarity, performance, and personalization.

```

---

Let me know if you want to add screenshots, badges, or GitHub Actions to automate testing or deployment.
