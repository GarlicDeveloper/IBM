import streamlit as st
import requests

OLLAMA_MODEL = "llama3"  # or mistral, gemma, etc.
OLLAMA_URL = f"http://localhost:11434/api/generate"

st.title("🏋️‍♂️ Local AI Fitness & Diet Planner")

goal = st.selectbox("Fitness Goal", ["Lose Weight", "Build Muscle", "Stay Fit"])
diet = st.selectbox("Diet Preference", ["Vegetarian", "Vegan", "Non-Vegetarian", "Jain", "Other"])
budget = st.slider("Monthly Budget (INR)", 500, 10000, 3000, step=500)
equipment = st.multiselect("Available Equipment", ["None", "Dumbbells", "Resistance Bands", "Yoga Mat", "Cycle", "Treadmill"])
culture = st.text_input("Cultural Food Habits", "e.g., prefers South Indian meals, avoids beef")

submit = st.button("Generate Plan")

if submit:
    prompt = f"""
    Create a personalized weekly workout and diet plan for a student:
    - Goal: {goal}
    - Diet: {diet}
    - Budget: ₹{budget}
    - Equipment: {', '.join(equipment) if equipment else 'None'}
    - Cultural Preferences: {culture}
    Include:
    - 5-day workout routine (home-based if no equipment)
    - 7-day meal plan with breakfast, lunch, dinner
    - Tips for staying consistent and motivated
    Ensure it's practical, budget-friendly, and effective.
    """

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        result = response.json()
        st.success("Here's your personalized plan:")
        st.markdown(result['response'])
    else:
        st.error("Local LLM call failed.")
        st.write(response.text)
