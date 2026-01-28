import streamlit as st
from src.ui.layout import Layout

def load_layout():
    """
    This function loads the layout of the application. 
    User selections are stored in the session state.
    User selections are validated.
    """
    layout = Layout()
    user_selections = layout.render()
    
    if not user_selections:
        st.error("Error: User selections are not valid")
        return

    user_input = st.chat_input("Ask a question ...")
    print(user_input)

    
