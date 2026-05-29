import os
from crewai import Agent, Task, Crew, LLM

# Pass the AQ key explicitly to the native Google provider
gemini_llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.environ.get("GEMINI_API_KEY")
)

# Define our AI agent
researcher = Agent(
    role="Tech Researcher",
    goal="Give me a simple, mind-blowing tech fact from 2026.",
    backstory="You are a futuristic researcher looking for cool insights.",
    llm=gemini_llm,
    verbose=True # This displays exactly what the agent is thinking in the logs
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
    memory=False # Disables the memory database to prevent OpenAI fallback errors
)

result = crew.kickoff()

print("\n--- GEMINI AGENT OUTPUT ---")
print(result)
print("---------------------------\n")
