import os
from crewai import Agent, Task, Crew, LLM

# Configure Gemini natively using your AQ key directly
gemini_llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.environ.get("GEMINI_API_KEY")
)

# Define our AI agent attached to Gemini
researcher = Agent(
    role="Tech Researcher",
    goal="Give me a simple, mind-blowing tech fact from 2026.",
    backstory="You are a futuristic researcher looking for cool insights.",
    llm=gemini_llm,
    verbose=True
)

# Define the task
task = Task(
    description="Find one interesting tech fact and explain why it matters.",
    expected_output="A short 2-sentence explanation.",
    agent=researcher
)

# Assemble and start the automation
crew = Crew(
    agents=[researcher], 
    tasks=[task],
    memory=False
)

result = crew.kickoff()

print("\n--- GEMINI AGENT OUTPUT ---")
print(result)
print("---------------------------\n")
