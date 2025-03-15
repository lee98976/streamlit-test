import handler
import streamlit as st

"""
Dungeons & Dragons.
"""

startingPrompt = "You are a D&D host. If there are more instructions, read those and continue the story as the player responds. If there are not, guide the player in a new D&D journey by making their character, setting the world, and so on. Teach the player when they ask. Instructions: "

apiKey = st.text_input("API Key")
apiPress = st.button("Set client:")
if apiPress:
    if not "client" in st.session_state:
        st.session_state["client"] = handler.SendRequest(apiKey)


if "client" in st.session_state:
    userMessage = st.text_input("Message")
    isPressed = st.button("Send")

    if (isPressed):
        st.session_state["client"].sendResponseWithHistory(userMessage)
        
        for message in st.session_state["client"].chatHistory:
            st.write(message["role"] + ": " + message["content"])
        
        if (len(st.session_state["client"].chatHistory) >= 25):
            st.session_state["client"].summarizeCurrentStory(startingPrompt)
        