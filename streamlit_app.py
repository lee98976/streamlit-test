import sendRequest
import streamlit as st

"""
Dungeons & Dragons.
"""

startingPrompt = "You are a D&D host. If there are more instructions, read those and continue the story as the player responds. If there are not, guide the player in a new D&D journey by making their character, setting the world, and so on. Teach the player when they ask. Instructions: "

userMessage = st.text_input("Message")
isPressed = st.button("Send")

if (isPressed):
    sendRequest.sendResponseWithHistory(userMessage)
    
    for message in sendRequest.chatHistory:
        st.write(message["role"] + ": " + message["content"])
    
    if (len(sendRequest.chatHistory) >= 25):
        sendRequest.summarizeCurrentStory(startingPrompt)
    