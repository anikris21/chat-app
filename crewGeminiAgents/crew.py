from crewai import Crew, Process
from tasks import research_task, writer_task
from agents import researcher, writer

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writer_task],
    process=Process.sequential
)

# start task execution
result = crew.kickoff(inputs={'topic': 'AI in Fintech'})
print(result)