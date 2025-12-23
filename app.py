from crewai import Agent, Task, Crew
from langchain_community.llms import Ollama

# Connect to the Brain you installed in Step 1
local_llm = Ollama(model="llama3.2")

# Define the PawnBroker's Identity
pawn_broker = Agent(
  role='Senior Pawn Appraiser',
  goal='Accurately value items and calculate loan risks',
  backstory='Expert in jewelry, electronics, and local pawn laws.',
  llm=local_llm
)

# Define the First Task
appraisal_task = Task(
  description='Assess a used MacBook Pro M2 with 16GB RAM for a 30-day loan.',
  expected_output='A suggested loan amount and a list of risk factors.',
  agent=pawn_broker
)

# Start the Agent
pawn_crew = Crew(agents=[pawn_broker], tasks=[appraisal_task])
result = pawn_crew.start()
print(result)