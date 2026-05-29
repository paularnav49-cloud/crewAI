import os
from crewai import Agent, Task, Crew

# 1. Define our AI agent without custom LLM objects (it will read the environment)
researcher = Agent(
    role="Tech Researcher",
    goal="Give me a simple, mind-blowing tech fact from 2026.",
    backstory="You are a futuristic researcher looking for cool insights.",
    verbose=True
)

# 2. Define the task
task = Task(
    description="Find one interesting tech fact and explain why it matters.",
    expected_output="A short 2-sentence explanation.",
    agent=researcher
)

# 3. Assemble and start the automation
crew = Crew(
    agents=[researcher], 
    tasks=[task],
    memory=False  # Keeps execution minimal and safe
)

result = crew.kickoff()

print("\n--- GEMINI AGENT OUTPUT ---")
print(result)
print("---------------------------\n")
