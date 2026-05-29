import os
from crewai import Agent, Task, Crew, LLM

# Configure the Gemini LLM using the environment endpoint setup
gemini_llm = LLM(
    model="openai/gemini-2.5-flash",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.environ.get("GEMINI_API_KEY")
)

# Define a simple researcher agent
researcher = Agent(
    role="Tech Researcher",
    goal="Give me a simple, mind-blowing tech fact from 2026.",
    backstory="You are a futuristic researcher looking for cool insights.",
    llm=gemini_llm
)

# Define the task
task = Task(
    description="Find one interesting tech fact and explain why it matters.",
    expected_output="A short 2-sentence explanation.",
    agent=researcher
)

# Assemble the crew and kick it off
crew = Crew(agents=[researcher], tasks=[task])
result = crew.kickoff()

print("\n--- GEMINI AGENT OUTPUT ---")
print(result)
print("---------------------------\n")
