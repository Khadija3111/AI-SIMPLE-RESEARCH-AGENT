import os
from dotenv import load_dotenv
from agents import Agent,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,WebSearchTool
load_dotenv()

gemini_api_key= os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)
agent =Agent(
    name="Research Assistant Agent",
    instructions= "You are a research assistant. "
        "When the user asks a question, perform a web search and summarize your findings "
        "in a structured format: Introduction, Key Findings (3 bullet points), Conclusion. "
        "If the information is unavailable, tell them honestly." ,
    model =model,
)

user_question = input("🔎 What topic should I research for you? ")
result=Runner.run_sync(agent,user_question)
print(result.final_output)
