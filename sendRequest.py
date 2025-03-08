from openai import OpenAI

keyFile = open("APIKey.txt", "r")
theKey = keyFile.readline()
keyFile.close()

client = OpenAI(
    api_key = theKey
)

# {"role" : "system", "content" : "sysPrompt"}
chatHistory = []

def setChatHistory(sysPrompt):
    global chatHistory
    chatHistory = [{"role" : "system", "content" : sysPrompt}]

def sendResponseWithHistory(userPrompt):
    global chatHistory
    chatHistory.append({"role" : "user", "content" : userPrompt})
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages = chatHistory
    )
    chatHistory.append({"role" : "assistant", "content" : response.choices[0].message.content})

    return response.choices[0].message.content

def summarizeCurrentStory(sysPrompt):
    newText = sendResponseWithHistory("Summarize the current character and storyline so far into text form, as you will have continue the story as a DND host without prior knowledge of the current events. Make sure to get all of the important parts of the character and story such as character stats, weapons, items as well as the current story line.")
    setChatHistory([{"role" : "system", "content" : sysPrompt + newText}])

startingPrompt = "You are a D&D host. If there are more instructions, read those and continue the story as the player responds. If there are not, guide the player in a new D&D journey by making their character, setting the world, and so on. Teach the player when they ask. Instructions: "
setChatHistory(startingPrompt)