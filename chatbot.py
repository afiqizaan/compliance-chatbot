import streamlit as st

# --- Simple knowledge base ---
faq = {
    "compliance deadline": "The compliance deadline is March 31st each year.",
    "reporting requirements": "You must submit an annual report, training certificate, and compliance attestation.",
    "policy access": "You can access the compliance policies at: https://intranet.company.com/policies",
    "contact info": "Contact the Compliance Team at compliance@yourcompany.com.",
    "training": "Yes, compliance training is mandatory and must be completed by February 15th.",
    "missed deadline": "Please contact Compliance immediately if you miss a deadline. Delays may result in escalation.",
    "data protection": "All data is stored securely and handled according to our Data Protection Policy."
}

def find_answer(user_input):
    user_input = user_input.lower()
    for key in faq:
        if key in user_input:
            return faq[key]
    return "I'm not sure about that. Please email compliance@yourcompany.com for help."

# --- Streamlit App ---
st.set_page_config(page_title="Compliance Chatbot", page_icon="💬")
st.title("💬 Compliance Chatbot")
st.write("Ask me about compliance policies, deadlines, and more.")

user_question = st.text_input("Your question:")
if user_question:
    answer = find_answer(user_question)
    st.markdown(f"**Answer:** {answer}")
